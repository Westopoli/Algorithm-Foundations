# Flight Route Optimization — Architecture & Planning

## 1. Problem Statement

**Domain:** Flight route optimization across ~20 major airports.

**Real-world framing:** An airline analyst needs to evaluate route connectivity, find cheapest itineraries between airports, and identify the minimum-cost backbone network that keeps all airports connected.

**Graph properties:**
- **Directed** — route A→B may exist without B→A, or at different costs
- **Weighted** — edge weights represent ticket cost (USD)
- Vertices: airports (identified by IATA code, e.g. ATL, ORD, LAX)
- Edges: direct flight routes with associated cost

**Why directed matters:** One-way pricing asymmetry is real (flying into a hub is often cheaper than flying out). This gives you a meaningful `to_undirected()` conversion step for MST, which is worth discussing in the report.

---

## 2. Project Structure

```
flight_optimizer/
├── graph.py            # Graph class (adjacency list)
├── algorithms.py       # BFS, DFS, Dijkstra, Kruskal
├── experiments.py      # Timing harness, graph variant generator
├── visualize.py        # matplotlib output for results section
├── data/
│   └── flights.json    # ~20-airport dataset
└── main.py             # Entry point — runs demos + experiments
```

**Principle:** Every algorithm is a standalone function that takes a Graph and returns data. No printing or side effects inside algorithm functions. All output/display logic lives in `main.py` and `visualize.py`.

---

## 3. Module Interfaces (Pseudocode)

### 3a. `graph.py` — Graph Class

```
CLASS Graph:
    INTERNAL: adj = dictionary mapping vertex → list of (neighbor, weight)

    add_vertex(v)
        Add v to adj with empty neighbor list if not present

    add_edge(u, v, weight)
        Add vertex u and v if not present
        Append (v, weight) to adj[u]
        NOTE: directed — does NOT add reverse edge

    remove_edge(u, v)
        Remove (v, *) from adj[u]

    neighbors(v) → list of (neighbor, weight)
        Return adj[v]

    get_weight(u, v) → weight or None
        Search adj[u] for v, return weight if found

    vertices() → list of vertex labels
        Return all keys in adj

    edges() → list of (u, v, weight)
        Iterate all adj entries, collect all edges

    vertex_count() → int
    edge_count() → int

    from_json(path) → Graph          [class method]
        Load flights.json, construct graph

    to_undirected() → Graph
        Return a NEW Graph where every directed edge u→v
        also produces v→u (keep the lower weight if both exist)
        PURPOSE: Kruskal requires undirected input
```

**Dataset format (`flights.json`):**
```
{
    "airports": ["ATL", "ORD", "DFW", ...],
    "routes": [
        {"from": "ATL", "to": "ORD", "cost": 180},
        {"from": "ORD", "to": "ATL", "cost": 210},
        ...
    ]
}
```

---

### 3b. `algorithms.py` — Four Algorithms

#### BFS — Breadth-First Search

```
FUNCTION bfs(graph, start) → dictionary {vertex: hop_distance}

    Initialize queue with start
    Initialize visited set with start
    Initialize distances = {start: 0}

    WHILE queue is not empty:
        current = dequeue
        FOR each (neighbor, weight) in graph.neighbors(current):
            IF neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = distances[current] + 1
                enqueue neighbor

    RETURN distances
```

**Use case:** "From hub ATL, how many connections to reach every other airport?"
**Time:** O(V + E)  |  **Space:** O(V)

---

#### DFS — Depth-First Search

```
FUNCTION dfs(graph, start) → list of vertices in visit order

    Initialize stack with start
    Initialize visited = empty set
    Initialize order = empty list

    WHILE stack is not empty:
        current = pop
        IF current not in visited:
            visited.add(current)
            order.append(current)
            FOR each (neighbor, weight) in graph.neighbors(current):
                IF neighbor not in visited:
                    push neighbor

    RETURN order
```

**Use case:** "Explore all reachable airports from a starting hub — path exploration and reachability check."
**Time:** O(V + E)  |  **Space:** O(V)

---

#### Dijkstra — Single-Source Shortest Path

```
FUNCTION dijkstra(graph, start) → (distances, predecessors)

    Initialize distances = {v: ∞ for all v}, distances[start] = 0
    Initialize predecessors = {v: None for all v}
    Initialize priority_queue with (0, start)

    WHILE priority_queue is not empty:
        (dist, current) = extract_min
        IF dist > distances[current]:
            CONTINUE  (stale entry)

        FOR each (neighbor, weight) in graph.neighbors(current):
            new_dist = dist + weight
            IF new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                predecessors[neighbor] = current
                insert (new_dist, neighbor) into priority_queue

    RETURN (distances, predecessors)
```

**Path reconstruction helper:**
```
FUNCTION reconstruct_path(predecessors, start, end) → list of vertices
    path = []
    current = end
    WHILE current is not None:
        prepend current to path
        current = predecessors[current]
    IF path[0] == start: RETURN path
    ELSE: RETURN []  (unreachable)
```

**Use case:** "What's the cheapest itinerary from TPA to SEA?"
**Time:** O((V + E) log V) with min-heap  |  **Space:** O(V)

---

#### Kruskal — Minimum Spanning Tree

```
FUNCTION kruskal(graph) → list of (u, v, weight) forming MST

    Convert graph to undirected (via graph.to_undirected())
    Collect all edges, sort by weight ascending
    Initialize Union-Find with all vertices
    Initialize mst = empty list

    FOR each (u, v, weight) in sorted edges:
        IF find(u) ≠ find(v):
            union(u, v)
            mst.append((u, v, weight))
        IF len(mst) == V - 1:
            BREAK

    RETURN mst

--- Union-Find (internal helper) ---

STRUCTURE UnionFind:
    parent = {v: v for all v}
    rank = {v: 0 for all v}

    find(x):
        IF parent[x] ≠ x:
            parent[x] = find(parent[x])  (path compression)
        RETURN parent[x]

    union(x, y):
        rx, ry = find(x), find(y)
        IF rx == ry: RETURN
        Attach smaller-rank tree under larger-rank root (union by rank)
```

**Use case:** "What's the cheapest set of routes that keeps all airports connected — minimal backbone network?"
**Time:** O(E log E) for sort  |  **Space:** O(V) for Union-Find

---

### 3c. `experiments.py` — Timing & Comparison

```
FUNCTION generate_variant(n_vertices, density, seed) → Graph
    Create n_vertices airports with random labels
    For each pair, add edge with probability = density
    Assign random weights in range [80, 500]
    Ensures graph is connected

FUNCTION time_algorithm(fn, *args, trials=100) → {mean_ms, min_ms, max_ms}
    Run fn(*args) for `trials` iterations
    Record wall-clock time for each via perf_counter
    Return stats

FUNCTION run_experiments() → results dict
    Test matrix:
        Graph sizes:    20 nodes (original), 50 nodes, 100 nodes
        Densities:      sparse (~15% edge probability), dense (~60% edge probability)
    
    For each (size, density) combination:
        Generate graph
        Time BFS, DFS, Dijkstra, Kruskal
        Record results

    Return structured results for visualize.py
```

---

### 3d. `visualize.py` — Charts & Tables

**Outputs needed for rubric Section 5:**
1. Bar chart — execution time per algorithm on the base 20-node graph
2. Line chart — execution time vs. graph size (20, 50, 100 nodes) per algorithm
3. Grouped bar chart — sparse vs. dense comparison at each graph size
4. Summary table — mean execution time in ms for all (algorithm × size × density) combos

All charts saved as PNG files for inclusion in the report.

---

## 4. Task Split Suggestion

| Task | Owner | Rubric Sections |
|------|-------|-----------------|
| Dataset design (`flights.json`) + `graph.py` | Member A | §1, §2 |
| `algorithms.py` (all four algorithms) | Member B | §3 |
| `experiments.py` + `visualize.py` | Member A | §5 |
| Complexity analysis writeup (pseudocode, Big-O) | Member B | §4 |
| Discussion & insights writeup | Both | §6 |
| Report assembly | Member A | §7 |

Adjust as needed — the key constraint is that both members need to present portions of the project, so both should understand the algorithms and results.

---

## 5. Open Decisions

- [ ] **Language lock-in:** Python recommended (matplotlib, heapq, clean pseudocode-to-code mapping). Confirm with teammate.
- [ ] **Airport selection:** Pick ~20 real US airports with plausible synthetic pricing, or go international? Real IATA codes help the presentation.
- [ ] **Bellman-Ford:** Spec says "Dijkstra **or** Bellman-Ford." Dijkstra is the right pick since all weights are positive. Could optionally implement both for extra comparison material in §5.
- [ ] **BFS vs DFS:** Spec says "BFS **and/or** DFS." Implementing both is minimal extra work and strengthens the traversal comparison.
- [ ] **Presentation tool:** Google Slides, PowerPoint, or something else?

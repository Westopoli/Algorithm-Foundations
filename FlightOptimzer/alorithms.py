# Algorithm implementations: BFS, DFS, Dijkstra, and Kruskal's MST.
# Each function takes a Graph (from graph.py) and returns data — no printing or side effects.
# Includes Union-Find helper used internally by Kruskal.
# Called by: main.py (for demos), experiments.py (for timing benchmarks)

def bfs(graph, start):
    visited = {start}       # tracks visited nodes
    queue = [start]         # dictionary of next nodes
    distances = {start: 0}  # depth tracking

    while queue:
        # This logic was the first try, ended up being flawed
        # node, node_depth = queue.pop(0)  # unpack first tuple
        # while node_depth > current_depth:
        #     current_depth += 1
        
        # if node not in path:
        #     visited.add(node)
        #     path.append(node)

        current = queue.pop(0)
        # _ for distance, we don't need it for BFS
        for (location, _) in graph.locations[current]:
            if location not in visited:
                visited.add(location)
                distances[location] = distances[current] + 1
                queue.append(location)

    return distances

def dfs(graph, start):
    # visited starts empty so start gets marked when popped, not pushed
    visited = set()
    stack = [start]
    order = []

    while stack:
        # pop from end, not front 
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            order.append(current)
            for (location, _) in graph.locations[current]:
                if location not in visited:
                    stack.append(location)

    return order


import heapq

def dijkstra(graph, start):
    # uses weights unlike bfs, distances tracks cost, not hops 
    distances = {v: float('inf') for v in graph.locations}
    distances[start] = 0
    predecessors = {v: None for v in graph.locations}
    # priority queue sorts by lowest cost automatically
    priority_queue = [(0, start)]

    while priority_queue:
        dist, current = heapq.heappop(priority_queue)
        # we've already found a cheaper path, skip stale entries
        if dist > distances[current]:
            continue
        for (location, weight) in graph.locations[current]:
            new_dist = dist + weight
            if new_dist < distances[location]:
                distances[location] = new_dist
                predecessors[location] = current
                heapq.heappush(priority_queue, (new_dist, location))

    return (distances, predecessors)


def reconstruct_path(predecessors, start, end):
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]
    if path[0] == start:
        return path
    return []


class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, x):
        # flatten tree so future lookups are faster
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        # attach smaller tree under larger tree
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1


def kruskal(graph):
    # convert to undirected, mst needs edges in both directions
    undirected = graph.to_undirected()
    edges = undirected.edges()
    edges.sort(key=lambda e: e[2])
    uf = UnionFind(undirected.locations)
    mst = []

    for (u, v, weight) in edges:
        # only add edge if it connects two separate components
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
        if len(mst) == len(undirected.locations) - 1:
            break

    return mst

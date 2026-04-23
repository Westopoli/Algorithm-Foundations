# Algorithm implementations: BFS, DFS, Dijkstra, and Kruskal's MST.
# Each function takes a Graph (from graph.py) and returns data — no printing or side effects.
# Includes Union-Find helper used internally by Kruskal.
# Called by: main.py (for demos), experiments.py (for timing benchmarks)

def bfs(graph, start):
    visited = {start}         # tracks visited nodes
    queue = [start]         # list of next nodes
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
        for  (location, _) in graph.locations(current):
            if location not in visited:
                visited.add(location)
                distances[location] = distances[current] + 1
                queue.append(location)

    return distances


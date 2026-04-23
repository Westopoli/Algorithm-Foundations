# Algorithm implementations: BFS, DFS, Dijkstra, and Kruskal's MST.
# Each function takes a Graph (from graph.py) and returns data — no printing or side effects.
# Includes Union-Find helper used internally by Kruskal.
# Called by: main.py (for demos), experiments.py (for timing benchmarks)

def bfs(graph, start):
    visited = set()     # tracks visited nodes
    queue = [start]     # list of next nodes
    parent = {}         # will track how we got to each node
    depth = 1

    while queue:
        node, depth = queue.pop(0)  # unpack first tuple

        
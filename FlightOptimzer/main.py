# Entry point — orchestrates the full flight optimizer pipeline.
# Loads the flight dataset via graph.py, runs algorithm demos from algorithms.py,
# executes timing experiments via experiments.py, and generates visualizations via visualize.py.
# All output and display logic lives here and in visualize.py.

from graph import AirportNetwork
from alorithms import bfs, dfs, dijkstra, kruskal, reconstruct_path
from experiments import run_experiments
import visualize


def demo_bfs(graph, start):
    print("\n=== BFS from " + start + " ===")
    distances = bfs(graph, start)
    for airport in distances:
        print("  " + airport + ": " + str(distances[airport]) + " hops")


def demo_dfs(graph, start):
    print("\n=== DFS from " + start + " ===")
    order = dfs(graph, start)
    print("  visit order: " + str(order))


def demo_dijkstra(graph, start, end):
    print("\n=== Dijkstra from " + start + " to " + end + " ===")
    distances, predecessors = dijkstra(graph, start)
    path = reconstruct_path(predecessors, start, end)
    if path:
        print("  cheapest path: " + " -> ".join(path))
        print("  total cost: $" + str(distances[end]))
    else:
        print("  no path found")


def demo_kruskal(graph):
    print("\n=== Kruskal MST ===")
    mst = kruskal(graph)
    total_cost = 0
    for (u, v, weight) in mst:
        print("  " + u + " -- " + v + " : $" + str(weight))
        total_cost += weight
    print("  total mst cost: $" + str(total_cost))


def main():
    # load the flight dataset
    graph = AirportNetwork.from_json("data/flights.json")
    print("loaded " + str(graph.vertex_count()) + " airports, "
          + str(graph.edge_count()) + " routes")

    # run algorithm demos on the real dataset
    demo_bfs(graph, "ATL")
    demo_dfs(graph, "ATL")
    demo_dijkstra(graph, "TPA", "SEA")
    demo_kruskal(graph)

    # run timing experiments across different graph sizes and densities
    print("\n=== running experiments ===")
    results = run_experiments()

    # generate charts and summary table
    print("\n=== generating visualizations ===")
    visualize.generate_all(results)


main()

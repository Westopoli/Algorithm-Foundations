# Timing harness and graph variant generator for benchmarking.
# Generates random graphs at different sizes and densities using graph.py's Graph class.
# Times each algorithm from algorithms.py across multiple trials.
# Produces structured results consumed by visualize.py for charts and tables.
# Called by: main.py

import time
import random
from graph import AirportNetwork
from alorithms import bfs, dfs, dijkstra, kruskal


def generate_variant(n_vertices, density, seed=None):
    if seed is not None:
        random.seed(seed)

    graph = AirportNetwork()

    # create airport labels like A0, A1, A2
    labels = []
    for i in range(n_vertices):
        labels.append("A" + str(i))

    for label in labels:
        graph.add_location(label)

    # connect all vertices in a chain so the graph is always connected
    for i in range(n_vertices - 1):
        cost = random.randint(80, 500)
        graph.add_connecting_flight(labels[i], labels[i + 1], cost)

    # add random edges based on density
    for i in range(n_vertices):
        for j in range(i + 2, n_vertices):
            if random.random() < density:
                cost = random.randint(80, 500)
                graph.add_connecting_flight(labels[i], labels[j], cost)

    return graph


def time_algorithm(fn, args, trials=100):
    times = []
    for t in range(trials):
        start = time.perf_counter()
        fn(*args)
        end = time.perf_counter()
        elapsed_ms = (end - start) * 1000
        times.append(elapsed_ms)

    times.sort()
    total = 0
    for t in times:
        total += t

    return {
        "mean_ms": total / len(times),
        "min_ms": times[0],
        "max_ms": times[len(times) - 1]
    }


def run_experiments():
    sizes = [20, 50, 100]
    densities = [
        ("sparse", 0.15),
        ("dense", 0.60)
    ]

    results = {}

    for size in sizes:
        for (density_name, density_value) in densities:
            label = str(size) + "_" + density_name
            graph = generate_variant(size, density_value, seed=42)
            start_vertex = "A0"

            print("timing " + label + "...")

            bfs_time = time_algorithm(bfs, [graph, start_vertex])
            dfs_time = time_algorithm(dfs, [graph, start_vertex])
            dijkstra_time = time_algorithm(dijkstra, [graph, start_vertex])
            kruskal_time = time_algorithm(kruskal, [graph])

            results[label] = {
                "size": size,
                "density": density_name,
                "bfs": bfs_time,
                "dfs": dfs_time,
                "dijkstra": dijkstra_time,
                "kruskal": kruskal_time
            }

    return results

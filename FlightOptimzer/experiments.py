# Timing harness for benchmarking.
# Builds test graphs at different sizes and densities by hand.
# Times each algorithm from algorithms.py across multiple trials.
# Produces structured results consumed by visualize.py for text output.
# Called by: main.py

import time
from graph import AirportNetwork
from alorithms import bfs, dfs, dijkstra, kruskal


def time_bfs(graph, start, trials=100):
    times = []
    for t in range(trials):
        begin = time.perf_counter()
        bfs(graph, start)
        end = time.perf_counter()
        times.append((end - begin) * 1000)
    total = 0
    for t in times:
        total += t
    return total / len(times)


def time_dfs(graph, start, trials=100):
    times = []
    for t in range(trials):
        begin = time.perf_counter()
        dfs(graph, start)
        end = time.perf_counter()
        times.append((end - begin) * 1000)
    total = 0
    for t in times:
        total += t
    return total / len(times)


def time_dijkstra(graph, start, trials=100):
    times = []
    for t in range(trials):
        begin = time.perf_counter()
        dijkstra(graph, start)
        end = time.perf_counter()
        times.append((end - begin) * 1000)
    total = 0
    for t in times:
        total += t
    return total / len(times)


def time_kruskal(graph, trials=100):
    times = []
    for t in range(trials):
        begin = time.perf_counter()
        kruskal(graph)
        end = time.perf_counter()
        times.append((end - begin) * 1000)
    total = 0
    for t in times:
        total += t
    return total / len(times)


def build_20_sparse():
    graph = AirportNetwork()
    for i in range(20):
        graph.add_location("N" + str(i))
    # chain to keep it connected
    graph.add_connecting_flight("N0", "N1", 120)
    graph.add_connecting_flight("N1", "N2", 200)
    graph.add_connecting_flight("N2", "N3", 150)
    graph.add_connecting_flight("N3", "N4", 300)
    graph.add_connecting_flight("N4", "N5", 180)
    graph.add_connecting_flight("N5", "N6", 250)
    graph.add_connecting_flight("N6", "N7", 90)
    graph.add_connecting_flight("N7", "N8", 310)
    graph.add_connecting_flight("N8", "N9", 140)
    graph.add_connecting_flight("N9", "N10", 220)
    graph.add_connecting_flight("N10", "N11", 170)
    graph.add_connecting_flight("N11", "N12", 260)
    graph.add_connecting_flight("N12", "N13", 100)
    graph.add_connecting_flight("N13", "N14", 340)
    graph.add_connecting_flight("N14", "N15", 130)
    graph.add_connecting_flight("N15", "N16", 190)
    graph.add_connecting_flight("N16", "N17", 280)
    graph.add_connecting_flight("N17", "N18", 110)
    graph.add_connecting_flight("N18", "N19", 240)
    # a few extra edges to make it sparse but not just a chain
    graph.add_connecting_flight("N0", "N5", 400)
    graph.add_connecting_flight("N3", "N10", 350)
    graph.add_connecting_flight("N7", "N14", 270)
    graph.add_connecting_flight("N12", "N19", 320)
    graph.add_connecting_flight("N1", "N8", 210)
    graph.add_connecting_flight("N6", "N13", 160)
    return graph


def build_20_dense():
    graph = AirportNetwork()
    for i in range(20):
        graph.add_location("N" + str(i))
    # chain
    graph.add_connecting_flight("N0", "N1", 120)
    graph.add_connecting_flight("N1", "N2", 200)
    graph.add_connecting_flight("N2", "N3", 150)
    graph.add_connecting_flight("N3", "N4", 300)
    graph.add_connecting_flight("N4", "N5", 180)
    graph.add_connecting_flight("N5", "N6", 250)
    graph.add_connecting_flight("N6", "N7", 90)
    graph.add_connecting_flight("N7", "N8", 310)
    graph.add_connecting_flight("N8", "N9", 140)
    graph.add_connecting_flight("N9", "N10", 220)
    graph.add_connecting_flight("N10", "N11", 170)
    graph.add_connecting_flight("N11", "N12", 260)
    graph.add_connecting_flight("N12", "N13", 100)
    graph.add_connecting_flight("N13", "N14", 340)
    graph.add_connecting_flight("N14", "N15", 130)
    graph.add_connecting_flight("N15", "N16", 190)
    graph.add_connecting_flight("N16", "N17", 280)
    graph.add_connecting_flight("N17", "N18", 110)
    graph.add_connecting_flight("N18", "N19", 240)
    # many extra edges to make it dense
    graph.add_connecting_flight("N0", "N3", 350)
    graph.add_connecting_flight("N0", "N5", 400)
    graph.add_connecting_flight("N0", "N7", 290)
    graph.add_connecting_flight("N0", "N10", 480)
    graph.add_connecting_flight("N0", "N15", 390)
    graph.add_connecting_flight("N1", "N4", 270)
    graph.add_connecting_flight("N1", "N6", 330)
    graph.add_connecting_flight("N1", "N9", 410)
    graph.add_connecting_flight("N1", "N12", 250)
    graph.add_connecting_flight("N2", "N5", 180)
    graph.add_connecting_flight("N2", "N8", 320)
    graph.add_connecting_flight("N2", "N11", 440)
    graph.add_connecting_flight("N2", "N14", 360)
    graph.add_connecting_flight("N3", "N6", 200)
    graph.add_connecting_flight("N3", "N9", 310)
    graph.add_connecting_flight("N3", "N12", 270)
    graph.add_connecting_flight("N3", "N16", 450)
    graph.add_connecting_flight("N4", "N7", 160)
    graph.add_connecting_flight("N4", "N10", 380)
    graph.add_connecting_flight("N4", "N13", 290)
    graph.add_connecting_flight("N5", "N8", 230)
    graph.add_connecting_flight("N5", "N11", 340)
    graph.add_connecting_flight("N5", "N14", 420)
    graph.add_connecting_flight("N6", "N9", 190)
    graph.add_connecting_flight("N6", "N12", 280)
    graph.add_connecting_flight("N6", "N15", 370)
    graph.add_connecting_flight("N7", "N10", 250)
    graph.add_connecting_flight("N7", "N13", 310)
    graph.add_connecting_flight("N7", "N16", 400)
    graph.add_connecting_flight("N8", "N11", 170)
    graph.add_connecting_flight("N8", "N14", 290)
    graph.add_connecting_flight("N8", "N17", 350)
    graph.add_connecting_flight("N9", "N12", 210)
    graph.add_connecting_flight("N9", "N15", 330)
    graph.add_connecting_flight("N9", "N18", 440)
    graph.add_connecting_flight("N10", "N13", 180)
    graph.add_connecting_flight("N10", "N16", 300)
    graph.add_connecting_flight("N10", "N19", 390)
    graph.add_connecting_flight("N11", "N14", 220)
    graph.add_connecting_flight("N11", "N17", 360)
    graph.add_connecting_flight("N12", "N15", 240)
    graph.add_connecting_flight("N12", "N18", 310)
    graph.add_connecting_flight("N13", "N16", 200)
    graph.add_connecting_flight("N13", "N19", 420)
    graph.add_connecting_flight("N14", "N17", 260)
    graph.add_connecting_flight("N15", "N18", 300)
    graph.add_connecting_flight("N16", "N19", 340)
    graph.add_connecting_flight("N17", "N19", 230)
    return graph


def build_50_sparse():
    graph = AirportNetwork()
    for i in range(50):
        graph.add_location("N" + str(i))
    # chain
    for i in range(49):
        graph.add_connecting_flight("N" + str(i), "N" + str(i + 1), 100 + (i * 7) % 400)
    # sparse extra edges
    graph.add_connecting_flight("N0", "N10", 350)
    graph.add_connecting_flight("N5", "N20", 280)
    graph.add_connecting_flight("N10", "N25", 310)
    graph.add_connecting_flight("N15", "N30", 420)
    graph.add_connecting_flight("N20", "N35", 190)
    graph.add_connecting_flight("N25", "N40", 260)
    graph.add_connecting_flight("N30", "N45", 340)
    graph.add_connecting_flight("N0", "N25", 480)
    graph.add_connecting_flight("N10", "N40", 370)
    graph.add_connecting_flight("N5", "N35", 290)
    graph.add_connecting_flight("N15", "N49", 410)
    graph.add_connecting_flight("N3", "N22", 330)
    graph.add_connecting_flight("N12", "N38", 250)
    graph.add_connecting_flight("N7", "N44", 390)
    return graph


def build_50_dense():
    graph = AirportNetwork()
    for i in range(50):
        graph.add_location("N" + str(i))
    # chain
    for i in range(49):
        graph.add_connecting_flight("N" + str(i), "N" + str(i + 1), 100 + (i * 7) % 400)
    # dense extra edges, connect many nodes across the graph
    for i in range(50):
        for j in range(i + 2, 50):
            if (i + j) % 3 == 0:
                graph.add_connecting_flight("N" + str(i), "N" + str(j), 80 + (i * j) % 420)
    return graph


def build_100_sparse():
    graph = AirportNetwork()
    for i in range(100):
        graph.add_location("N" + str(i))
    # chain
    for i in range(99):
        graph.add_connecting_flight("N" + str(i), "N" + str(i + 1), 100 + (i * 11) % 400)
    # sparse extra edges
    graph.add_connecting_flight("N0", "N20", 350)
    graph.add_connecting_flight("N10", "N40", 280)
    graph.add_connecting_flight("N20", "N50", 310)
    graph.add_connecting_flight("N30", "N60", 420)
    graph.add_connecting_flight("N40", "N70", 190)
    graph.add_connecting_flight("N50", "N80", 260)
    graph.add_connecting_flight("N60", "N90", 340)
    graph.add_connecting_flight("N0", "N50", 480)
    graph.add_connecting_flight("N25", "N75", 370)
    graph.add_connecting_flight("N10", "N60", 290)
    graph.add_connecting_flight("N35", "N85", 410)
    graph.add_connecting_flight("N5", "N55", 330)
    graph.add_connecting_flight("N15", "N65", 250)
    graph.add_connecting_flight("N45", "N95", 390)
    graph.add_connecting_flight("N0", "N99", 500)
    graph.add_connecting_flight("N33", "N66", 270)
    return graph


def build_100_dense():
    graph = AirportNetwork()
    for i in range(100):
        graph.add_location("N" + str(i))
    # chain
    for i in range(99):
        graph.add_connecting_flight("N" + str(i), "N" + str(i + 1), 100 + (i * 11) % 400)
    # dense extra edges
    for i in range(100):
        for j in range(i + 2, 100):
            if (i + j) % 3 == 0:
                graph.add_connecting_flight("N" + str(i), "N" + str(j), 80 + (i * j) % 420)
    return graph


def run_experiments():
    results = {}

    # 20 nodes sparse
    print("timing 20_sparse...")
    graph_20_sparse = build_20_sparse()
    results["20_sparse"] = {
        "bfs": time_bfs(graph_20_sparse, "N0"),
        "dfs": time_dfs(graph_20_sparse, "N0"),
        "dijkstra": time_dijkstra(graph_20_sparse, "N0"),
        "kruskal": time_kruskal(graph_20_sparse)
    }

    # 20 nodes dense
    print("timing 20_dense...")
    graph_20_dense = build_20_dense()
    results["20_dense"] = {
        "bfs": time_bfs(graph_20_dense, "N0"),
        "dfs": time_dfs(graph_20_dense, "N0"),
        "dijkstra": time_dijkstra(graph_20_dense, "N0"),
        "kruskal": time_kruskal(graph_20_dense)
    }

    # 50 nodes sparse
    print("timing 50_sparse...")
    graph_50_sparse = build_50_sparse()
    results["50_sparse"] = {
        "bfs": time_bfs(graph_50_sparse, "N0"),
        "dfs": time_dfs(graph_50_sparse, "N0"),
        "dijkstra": time_dijkstra(graph_50_sparse, "N0"),
        "kruskal": time_kruskal(graph_50_sparse)
    }

    # 50 nodes dense
    print("timing 50_dense...")
    graph_50_dense = build_50_dense()
    results["50_dense"] = {
        "bfs": time_bfs(graph_50_dense, "N0"),
        "dfs": time_dfs(graph_50_dense, "N0"),
        "dijkstra": time_dijkstra(graph_50_dense, "N0"),
        "kruskal": time_kruskal(graph_50_dense)
    }

    # 100 nodes sparse
    print("timing 100_sparse...")
    graph_100_sparse = build_100_sparse()
    results["100_sparse"] = {
        "bfs": time_bfs(graph_100_sparse, "N0"),
        "dfs": time_dfs(graph_100_sparse, "N0"),
        "dijkstra": time_dijkstra(graph_100_sparse, "N0"),
        "kruskal": time_kruskal(graph_100_sparse)
    }

    # 100 nodes dense
    print("timing 100_dense...")
    graph_100_dense = build_100_dense()
    results["100_dense"] = {
        "bfs": time_bfs(graph_100_dense, "N0"),
        "dfs": time_dfs(graph_100_dense, "N0"),
        "dijkstra": time_dijkstra(graph_100_dense, "N0"),
        "kruskal": time_kruskal(graph_100_dense)
    }

    return results

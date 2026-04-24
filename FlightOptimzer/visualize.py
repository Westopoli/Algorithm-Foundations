# Visualization module — prints timing results as text tables.
# Takes structured timing data produced by experiments.py.
# Called by: main.py


def generate_all(results):
    print("  BFS results:")
    if "20_sparse" in results:
        print("    20 sparse: " + format(results["20_sparse"]["bfs"], ".4f") + " ms")
    if "20_dense" in results:
        print("    20 dense:  " + format(results["20_dense"]["bfs"], ".4f") + " ms")
    if "50_sparse" in results:
        print("    50 sparse: " + format(results["50_sparse"]["bfs"], ".4f") + " ms")
    if "50_dense" in results:
        print("    50 dense:  " + format(results["50_dense"]["bfs"], ".4f") + " ms")
    if "100_sparse" in results:
        print("    100 sparse: " + format(results["100_sparse"]["bfs"], ".4f") + " ms")
    if "100_dense" in results:
        print("    100 dense:  " + format(results["100_dense"]["bfs"], ".4f") + " ms")

    print("")
    print("  DFS results:")
    if "20_sparse" in results:
        print("    20 sparse: " + format(results["20_sparse"]["dfs"], ".4f") + " ms")
    if "20_dense" in results:
        print("    20 dense:  " + format(results["20_dense"]["dfs"], ".4f") + " ms")
    if "50_sparse" in results:
        print("    50 sparse: " + format(results["50_sparse"]["dfs"], ".4f") + " ms")
    if "50_dense" in results:
        print("    50 dense:  " + format(results["50_dense"]["dfs"], ".4f") + " ms")
    if "100_sparse" in results:
        print("    100 sparse: " + format(results["100_sparse"]["dfs"], ".4f") + " ms")
    if "100_dense" in results:
        print("    100 dense:  " + format(results["100_dense"]["dfs"], ".4f") + " ms")

    print("")
    print("  Dijkstra results:")
    if "20_sparse" in results:
        print("    20 sparse: " + format(results["20_sparse"]["dijkstra"], ".4f") + " ms")
    if "20_dense" in results:
        print("    20 dense:  " + format(results["20_dense"]["dijkstra"], ".4f") + " ms")
    if "50_sparse" in results:
        print("    50 sparse: " + format(results["50_sparse"]["dijkstra"], ".4f") + " ms")
    if "50_dense" in results:
        print("    50 dense:  " + format(results["50_dense"]["dijkstra"], ".4f") + " ms")
    if "100_sparse" in results:
        print("    100 sparse: " + format(results["100_sparse"]["dijkstra"], ".4f") + " ms")
    if "100_dense" in results:
        print("    100 dense:  " + format(results["100_dense"]["dijkstra"], ".4f") + " ms")

    print("")
    print("  Kruskal results:")
    if "20_sparse" in results:
        print("    20 sparse: " + format(results["20_sparse"]["kruskal"], ".4f") + " ms")
    if "20_dense" in results:
        print("    20 dense:  " + format(results["20_dense"]["kruskal"], ".4f") + " ms")
    if "50_sparse" in results:
        print("    50 sparse: " + format(results["50_sparse"]["kruskal"], ".4f") + " ms")
    if "50_dense" in results:
        print("    50 dense:  " + format(results["50_dense"]["kruskal"], ".4f") + " ms")
    if "100_sparse" in results:
        print("    100 sparse: " + format(results["100_sparse"]["kruskal"], ".4f") + " ms")
    if "100_dense" in results:
        print("    100 dense:  " + format(results["100_dense"]["kruskal"], ".4f") + " ms")

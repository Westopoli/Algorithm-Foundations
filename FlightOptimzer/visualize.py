# Visualization module — prints timing results as text tables.
# Takes structured timing data produced by experiments.py.
# Called by: main.py


def generate_all(results):
    print("  BFS results:")
    if "20_sparse" in results:
        print("    20 sparse: " + format(results["20_sparse"]["bfs"]["mean_ms"], ".4f") + " ms")
    if "20_dense" in results:
        print("    20 dense:  " + format(results["20_dense"]["bfs"]["mean_ms"], ".4f") + " ms")
    if "50_sparse" in results:
        print("    50 sparse: " + format(results["50_sparse"]["bfs"]["mean_ms"], ".4f") + " ms")
    if "50_dense" in results:
        print("    50 dense:  " + format(results["50_dense"]["bfs"]["mean_ms"], ".4f") + " ms")
    if "100_sparse" in results:
        print("    100 sparse: " + format(results["100_sparse"]["bfs"]["mean_ms"], ".4f") + " ms")
    if "100_dense" in results:
        print("    100 dense:  " + format(results["100_dense"]["bfs"]["mean_ms"], ".4f") + " ms")

    print("")
    print("  DFS results:")
    if "20_sparse" in results:
        print("    20 sparse: " + format(results["20_sparse"]["dfs"]["mean_ms"], ".4f") + " ms")
    if "20_dense" in results:
        print("    20 dense:  " + format(results["20_dense"]["dfs"]["mean_ms"], ".4f") + " ms")
    if "50_sparse" in results:
        print("    50 sparse: " + format(results["50_sparse"]["dfs"]["mean_ms"], ".4f") + " ms")
    if "50_dense" in results:
        print("    50 dense:  " + format(results["50_dense"]["dfs"]["mean_ms"], ".4f") + " ms")
    if "100_sparse" in results:
        print("    100 sparse: " + format(results["100_sparse"]["dfs"]["mean_ms"], ".4f") + " ms")
    if "100_dense" in results:
        print("    100 dense:  " + format(results["100_dense"]["dfs"]["mean_ms"], ".4f") + " ms")

    print("")
    print("  Dijkstra results:")
    if "20_sparse" in results:
        print("    20 sparse: " + format(results["20_sparse"]["dijkstra"]["mean_ms"], ".4f") + " ms")
    if "20_dense" in results:
        print("    20 dense:  " + format(results["20_dense"]["dijkstra"]["mean_ms"], ".4f") + " ms")
    if "50_sparse" in results:
        print("    50 sparse: " + format(results["50_sparse"]["dijkstra"]["mean_ms"], ".4f") + " ms")
    if "50_dense" in results:
        print("    50 dense:  " + format(results["50_dense"]["dijkstra"]["mean_ms"], ".4f") + " ms")
    if "100_sparse" in results:
        print("    100 sparse: " + format(results["100_sparse"]["dijkstra"]["mean_ms"], ".4f") + " ms")
    if "100_dense" in results:
        print("    100 dense:  " + format(results["100_dense"]["dijkstra"]["mean_ms"], ".4f") + " ms")

    print("")
    print("  Kruskal results:")
    if "20_sparse" in results:
        print("    20 sparse: " + format(results["20_sparse"]["kruskal"]["mean_ms"], ".4f") + " ms")
    if "20_dense" in results:
        print("    20 dense:  " + format(results["20_dense"]["kruskal"]["mean_ms"], ".4f") + " ms")
    if "50_sparse" in results:
        print("    50 sparse: " + format(results["50_sparse"]["kruskal"]["mean_ms"], ".4f") + " ms")
    if "50_dense" in results:
        print("    50 dense:  " + format(results["50_dense"]["kruskal"]["mean_ms"], ".4f") + " ms")
    if "100_sparse" in results:
        print("    100 sparse: " + format(results["100_sparse"]["kruskal"]["mean_ms"], ".4f") + " ms")
    if "100_dense" in results:
        print("    100 dense:  " + format(results["100_dense"]["kruskal"]["mean_ms"], ".4f") + " ms")

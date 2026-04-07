"""
COT4400 Project 2 — Cybersecurity Algorithm Suite
Main entry point: runs all three algorithms with test cases and timing.

Person A: merge_sort.py, knapsack.py
Person B: activity_selection.py, main.py (this file), test data
"""

import time
from merge_sort import merge_sort
from activity_selection import activity_selection
from knapsack import knapsack


# ---------------------------------------------------------------------------
# Timing helper
# ---------------------------------------------------------------------------
def time_execution(func, *args):
    """Run func(*args), return (result, elapsed_ms)."""
    start = time.perf_counter()
    result = func(*args)
    elapsed_ms = (time.perf_counter() - start) * 1000
    return result, elapsed_ms


# ===========================================================================
# 1. MERGE SORT — Vulnerability Severity Ranker
# ===========================================================================
def run_merge_sort_tests():
    print("=" * 60)
    print("MERGE SORT — Vulnerability Severity Ranker")
    print("=" * 60)

    # Each vulnerability is (name, cvss_score).
    # We sort by CVSS descending so most critical appear first.
    test_cases = {
        "Small / Random": [
            ("CVE-2025-1001", 7.5),
            ("CVE-2025-1002", 9.8),
            ("CVE-2025-1003", 4.3),
            ("CVE-2025-1004", 6.1),
            ("CVE-2025-1005", 10.0),
        ],
        "Already sorted (descending)": [
            ("CVE-2025-2001", 10.0),
            ("CVE-2025-2002", 8.5),
            ("CVE-2025-2003", 7.0),
            ("CVE-2025-2004", 5.5),
            ("CVE-2025-2005", 3.0),
        ],
        "Reverse sorted (ascending)": [
            ("CVE-2025-3001", 1.0),
            ("CVE-2025-3002", 3.5),
            ("CVE-2025-3003", 5.0),
            ("CVE-2025-3004", 7.5),
            ("CVE-2025-3005", 9.9),
        ],
        "Edge — empty list": [],
        "Edge — single element": [
            ("CVE-2025-4001", 6.0),
        ],
    }

    for name, vulns in test_cases.items():
        scores = [v[1] for v in vulns]
        sorted_scores, ms = time_execution(merge_sort, scores)

        # Map back to names (descending order = most critical first)
        sorted_scores_desc = sorted_scores[::-1]
        score_to_vulns = {v[1]: v[0] for v in vulns}

        print(f"\nTest: {name}")
        print(f"  Input scores:  {scores}")
        print(f"  Sorted (desc): {sorted_scores_desc}")
        print(f"  Time: {ms:.4f} ms")

    # --- Benchmarking across input sizes ---
    import random
    print("\n--- Benchmark ---")
    print(f"{'Size':<10} {'Time (ms)':<15}")
    for size in [10, 100, 1000, 5000, 10000]:
        data = [random.uniform(0, 10) for _ in range(size)]
        _, ms = time_execution(merge_sort, data)
        print(f"{size:<10} {ms:<15.4f}")


# ===========================================================================
# 2. ACTIVITY SELECTION — Server Maintenance Window Planner
# ===========================================================================
def run_activity_selection_tests():
    print("\n" + "=" * 60)
    print("ACTIVITY SELECTION — Server Maintenance Window Planner")
    print("=" * 60)

    # Each activity: (name, start_hour, finish_hour)
    test_cases = {
        "Small / Normal": [
            ("Patch-A", 0, 2),
            ("Patch-B", 1, 3),
            ("Patch-C", 2, 5),
            ("Patch-D", 4, 6),
            ("Patch-E", 5, 7),
            ("Patch-F", 6, 8),
        ],
        "All overlapping": [
            ("Patch-X1", 0, 10),
            ("Patch-X2", 1, 9),
            ("Patch-X3", 2, 8),
        ],
        "No overlaps": [
            ("Patch-Y1", 0, 1),
            ("Patch-Y2", 2, 3),
            ("Patch-Y3", 4, 5),
            ("Patch-Y4", 6, 7),
        ],
        "Edge — empty list": [],
        "Edge — single window": [
            ("Patch-Z1", 3, 5),
        ],
    }

    for name, windows in test_cases.items():
        activities = [(w[1], w[2]) for w in windows]
        selected_indices, ms = time_execution(activity_selection, activities)

        selected_names = [windows[i][0] for i in selected_indices]
        print(f"\nTest: {name}")
        print(f"  Windows: {[(w[0], w[1], w[2]) for w in windows]}")
        print(f"  Selected: {selected_names}")
        print(f"  Count: {len(selected_indices)}")
        print(f"  Time: {ms:.4f} ms")

    # --- Benchmark ---
    import random
    print("\n--- Benchmark ---")
    print(f"{'Size':<10} {'Time (ms)':<15}")
    for size in [10, 100, 1000, 5000, 10000]:
        acts = []
        for _ in range(size):
            s = random.randint(0, 1000)
            f = s + random.randint(1, 50)
            acts.append((s, f))
        _, ms = time_execution(activity_selection, acts)
        print(f"{size:<10} {ms:<15.4f}")


# ===========================================================================
# 3. KNAPSACK — Firewall Rule Budget
# ===========================================================================
def run_knapsack_tests():
    print("\n" + "=" * 60)
    print("0/1 KNAPSACK — Firewall Rule Budget")
    print("=" * 60)

    # Each rule: (name, cpu_cost, threat_coverage_value)
    test_cases = {
        "Small / Normal": {
            "rules": [
                ("Block-SSH-Brute", 3, 60),
                ("DPI-Malware", 4, 80),
                ("Rate-Limit-DNS", 2, 40),
                ("Geo-Block", 5, 90),
                ("IDS-Signature", 1, 30),
            ],
            "capacity": 8,
        },
        "Edge — zero capacity": {
            "rules": [
                ("Rule-A", 2, 50),
                ("Rule-B", 3, 70),
            ],
            "capacity": 0,
        },
        "Edge — single item fits exactly": {
            "rules": [
                ("Rule-Solo", 5, 100),
            ],
            "capacity": 5,
        },
        "Edge — all items too heavy": {
            "rules": [
                ("Heavy-1", 10, 50),
                ("Heavy-2", 12, 60),
            ],
            "capacity": 5,
        },
        "Medium": {
            "rules": [
                ("R1", 2, 30), ("R2", 3, 45), ("R3", 4, 50),
                ("R4", 5, 70), ("R5", 1, 20), ("R6", 3, 55),
                ("R7", 6, 85), ("R8", 2, 35), ("R9", 4, 60),
                ("R10", 7, 100),
            ],
            "capacity": 15,
        },
    }

    for name, data in test_cases.items():
        weights = [r[1] for r in data["rules"]]
        values = [r[2] for r in data["rules"]]
        cap = data["capacity"]

        max_val, ms = time_execution(knapsack, weights, values, cap)

        print(f"\nTest: {name}")
        print(f"  Rules: {[(r[0], r[1], r[2]) for r in data['rules']]}")
        print(f"  Capacity: {cap}")
        print(f"  Max coverage value: {max_val}")
        print(f"  Time: {ms:.4f} ms")

    # --- Benchmark ---
    import random
    print("\n--- Benchmark ---")
    print(f"{'Items':<10} {'Capacity':<10} {'Time (ms)':<15}")
    for n_items in [10, 50, 100, 200]:
        cap = n_items * 3
        w = [random.randint(1, 10) for _ in range(n_items)]
        v = [random.randint(10, 100) for _ in range(n_items)]
        _, ms = time_execution(knapsack, w, v, cap)
        print(f"{n_items:<10} {cap:<10} {ms:<15.4f}")


# ===========================================================================
# RUN ALL
# ===========================================================================
if __name__ == "__main__":
    run_merge_sort_tests()
    run_activity_selection_tests()
    run_knapsack_tests()

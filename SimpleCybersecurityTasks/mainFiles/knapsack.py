"""
0/1 Knapsack — Firewall Rule Budget
Owner: Person A

Given firewall rules with CPU costs (weights) and threat-coverage
values, find the maximum total coverage achievable within a
processing budget (capacity) using dynamic programming.

DO NOT use a greedy approach — this MUST be DP.
"""


def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(values)

    if len(weights) != n:
        raise ValueError("weights and values must have the same length")
    if capacity < 0:
        raise ValueError("capacity must be non-negative")

    row = len(values)
    col = capacity + 1

    table = [[0] * col for _ in range(row)] # [0] * col gives [0,0,0,0,0,0,0] then we times that by row times

    for i in range(row):
        for j in range(col):
            table[i][j] = table[i - 1][j] if i > 0 else 0

            if weights[i] <= j:
                include = values[i] + (table[i - 1][j - weights[i]] if i > 0 else 0)
                table[i][j] = max(table[i][j], include)

    return table[row - 1][col - 1]




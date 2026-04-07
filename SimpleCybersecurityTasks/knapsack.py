"""
0/1 Knapsack — Firewall Rule Budget
Owner: Person A

Given firewall rules with CPU costs (weights) and threat-coverage
values, find the maximum total coverage achievable within a
processing budget (capacity) using dynamic programming.

DO NOT use a greedy approach — this MUST be DP.
"""


def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    """
    Solve the 0/1 knapsack problem via bottom-up DP.

    Args:
        weights:  list of item weights  (cpu costs)
        values:   list of item values   (threat coverage)
        capacity: maximum total weight   (processing budget)

    Returns:
        Maximum achievable value.
    """
    # TODO: Implement bottom-up DP with a 2D table.
    #
    # Steps:
    #   1. Let n = len(weights).
    #   2. Create a (n+1) x (capacity+1) table `dp` initialized to 0.
    #   3. For each item i from 1..n:
    #        For each weight w from 0..capacity:
    #          If weights[i-1] <= w:
    #            dp[i][w] = max(dp[i-1][w],
    #                          dp[i-1][w - weights[i-1]] + values[i-1])
    #          Else:
    #            dp[i][w] = dp[i-1][w]
    #   4. Return dp[n][capacity].
    #
    # Time:  O(n * capacity)
    # Space: O(n * capacity) for the 2D table
    #         (can be optimized to O(capacity) with 1D rolling array)
    pass

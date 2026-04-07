"""
Activity Selection — Server Maintenance Window Planner
Owner: Person B

Given a list of maintenance windows (start, finish), select the
maximum number of non-overlapping windows using a greedy approach.

You MAY use built-in sort here (it's not the D&C problem).
"""


def activity_selection(activities: list[tuple[int, int]]) -> list[int]:
    """
    Select the maximum set of non-overlapping activities.

    Args:
        activities: list of (start_time, finish_time) tuples.

    Returns:
        List of indices (relative to the ORIGINAL input order)
        of the selected activities.
    """
    # TODO: Implement greedy activity selection.
    #
    # Steps:
    #   1. If activities is empty, return [].
    #   2. Create an indexed list: [(start, finish, original_index), ...]
    #   3. Sort by finish time (ascending).
    #   4. Greedily pick the first activity, then keep picking
    #      the next activity whose start_time >= last picked finish_time.
    #   5. Return the list of original indices of selected activities.
    #
    # Time:  O(n log n) dominated by the sort
    # Space: O(n) for the indexed copy
    pass

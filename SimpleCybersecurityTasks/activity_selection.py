"""
Activity Selection — Server Maintenance Window Planner
Owner: Person B

Given a list of maintenance windows (start, finish), select the
maximum number of non-overlapping windows using a greedy approach.
"""

def activity_selection(activities: list[tuple[int, int]]) -> list[int]:
    """
    Select the maximum set of non-overlapping activities.
 
    Args:
        activities: list of (start_time, finish_time) tuples.
 
    Returns:
        List of indices (relative to the original input order)
        of the selected activities.
 
    Time:  O(n log n) dominated by the sort
    Space: O(n) for the indexed copy
    """
    # Base case
    if not activities:
        return []
 
    # Pair each activity with its original index so sorting doesn't lose it.
    indexed = [(start, finish, i) for i, (start, finish) in enumerate(activities)]
 
    # Greedy strategy: sort by finish time ascending.
    # Picking the earliest-finishing activity leaves the most room for future ones.
    indexed.sort(key=lambda a: a[1])
 
    # Take the first activity unconditionally
    selected_indices = [indexed[0][2]]
    last_finish = indexed[0][1]
 
    # Sweep through the rest. For each candidate, only one comparison is needed:
    # does it start at or after the last selected activity finished?
    for start, finish, original_index in indexed[1:]:
        if start >= last_finish:
            selected_indices.append(original_index)
            last_finish = finish
 
    return selected_indices
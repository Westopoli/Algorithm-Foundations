"""
Activity Selection — Server Maintenance Window Planner
Owner: Person B

Given a list of maintenance windows (start, finish), select the
maximum number of non-overlapping windows using a greedy approach.
"""

from merge_sort import merge_sort

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
    #
    # Design-mismatch note: Person A's merge_sort sorts by natural element comparison
    # and has no 'key' parameter so it cannot sort (start, finish, idx) tuples by finish
    # time directly. To bridge this gap without modifying merge_sort, I repacked each
    # tuple as (finish, start, orig_idx) so that merge_sort's < comparison sorts by
    # finish time first, which is exactly what the greedy algorithm requires.
    finish_first = [(finish, start, i) for start, finish, i in indexed]
    finish_first = merge_sort(finish_first)

    # Take the first activity unconditionally
    selected_indices = [finish_first[0][2]]
    last_finish = finish_first[0][0]

    # Sweep through the rest. For each candidate, only one comparison is needed:
    # does it start at or after the last selected activity finished?
    for finish, start, original_index in finish_first[1:]:
        if start >= last_finish:
            selected_indices.append(original_index)
            last_finish = finish
 
    return selected_indices
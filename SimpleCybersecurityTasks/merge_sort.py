"""
Merge Sort — Vulnerability Severity Ranker
Owner: Person A

Sorts a list of CVSS scores (floats) in ascending order using
the Merge Sort algorithm (divide & conquer).

DO NOT use any built-in sort functions.
"""


def merge_sort(arr: list) -> list:
    """
    Sort `arr` in ascending order via merge sort.

    Args:
        arr: list of numeric values (e.g. CVSS scores)

    Returns:
        A new sorted list.
    """
    # TODO: Implement recursive merge sort.
    #
    # Steps:
    #   1. Base case — if len(arr) <= 1, return a copy.
    #   2. Split arr into left and right halves.
    #   3. Recursively merge_sort each half.
    #   4. Merge the two sorted halves using the _merge helper.
    #
    # Time:  O(n log n) best / average / worst
    # Space: O(n) auxiliary for the merge buffer
    pass


def _merge(left: list, right: list) -> list:
    """
    Merge two sorted lists into one sorted list.

    Args:
        left:  sorted list
        right: sorted list

    Returns:
        Merged sorted list.
    """
    # TODO: Implement two-pointer merge.
    #
    # Steps:
    #   1. Initialize empty result list and two index pointers i, j = 0.
    #   2. While both pointers are in bounds, compare left[i] vs right[j],
    #      append the smaller one, advance that pointer.
    #   3. Append any remaining elements from whichever list isn't exhausted.
    #   4. Return result.
    pass

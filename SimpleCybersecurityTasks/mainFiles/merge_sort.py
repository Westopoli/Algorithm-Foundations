"""
Merge Sort — Vulnerability Severity Ranker
Owner: Person A

Sorts a list of CVSS scores (floats) in ascending order using
the Merge Sort algorithm (divide & conquer).

DO NOT use any built-in sort functions.
"""


def merge_sort(arr: list) -> list: # recursively splits the list in half and then call _merge to glue it back up in sorted order
    # base case
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2 # find midpoint
    left = arr[:mid] # sliced into left side
    right = arr[mid:] # sliced into right side

    left_sort = merge_sort(left)
    right_sort = merge_sort(right)

    return _merge(left_sort, right_sort)

     


# this method glues back the array together in a sorted order, takes in 2 sorted halves from the merge_sort method
def _merge(left: list, right: list) -> list:

    new_arr = [] # new array to store sorted elements
    i = 0 # tracks position in the left
    j = 0 # tracks position in the right

    while (i < len(left) and j < len(right)): # while loops to compare left side and right side elements
        if(left[i] < right[j]):
            new_arr.append(left[i])
            i+=1
        else:
            new_arr.append(right[j])
            j+=1

    while (i < len(left)): # for leftover elements from the left side that were not compared
        new_arr.append(left[i])
        i+=1

    while (j < len(right)): # for leftover elements from the right side that were not compared
        new_arr.append(right[j])
        j+=1

    return new_arr # returning the new sorted array


    


    

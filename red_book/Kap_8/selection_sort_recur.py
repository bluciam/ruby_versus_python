def sel_sort(aList, start = 0):
    """
    Function to perform recursively a selection sort of a list in place.
    It takes a list as input and returns the sorted list.
    """
    if len(aList) == start:
        return
    find_min_and_swap(aList, start)
    sel_sort(aList, start+1)
    return aList

def find_min_and_swap(aList, start):
    min_val = aList[start]
    for j in range(start, len(aList)):
        if aList[j] < min_val:
            min_val = aList[j]
            aList[j] = aList[start]
            aList[start] = min_val
    

print sel_sort( [ 4,7,2,5,6 ] )
print sel_sort( [ ] )
print sel_sort( [ 1 ] )

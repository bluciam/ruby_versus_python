def sel_sort(aList):
    """
    Function to perform iteratively a selection sort of a list in place.
    It takes a list as input and returns the sorted list.
    """
    print aList
    for i in range(0, len(aList)):
        min_val = aList[i]
        my_j = None
        for j in range(i+1, len(aList)):
            if aList[j] < min_val:
                min_val = aList[j]
                my_j = j
        if my_j != None:
            aList[my_j] = aList[i]
            aList[i] = min_val
    return aList

print sel_sort( [ 4,7,2,5,6 ] )
print sel_sort( [ ] )

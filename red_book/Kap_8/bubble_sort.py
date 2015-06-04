def bubble_sort(aList):
    """
    Brain-dead version of bubble sort, scanning everytime to the end of list.
    """
    print
    print aList
    swap = True
    while swap:
        swap = False
        for i in range(0, len(aList) - 1):
            if aList[i] > aList[i+1]:
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp
                swap = True
    return aList

print bubble_sort([8,6,5,3,4])
print bubble_sort([])
print bubble_sort([9])

def bubble_sort(aList):
    """
    Improved version of bubble sort, scanning everytime to the end of list.
    """
    print
    print aList
    stop = len(aList)
    swap = True
    while swap:
        stop -= 1
        swap = False
        print "Beginning of the for :" , aList
        for i in range(0, stop):
            if aList[i] > aList[i+1]:
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp
                swap = True
                print "In the for :" , aList
        print
    return aList

print bubble_sort([8,6,5,3,4])
print bubble_sort([])
print bubble_sort([9])
print bubble_sort( [ 9,8,6,5,4,0,1 ])

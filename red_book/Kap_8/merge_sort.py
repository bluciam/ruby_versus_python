def merge(aList, bList=[]):
    '''
    Merge two list, return an ordered list if inputs were sorted.
    '''
    newList = []
    a,b = 0,0
    while (a < len(aList)) and (b < len(bList)): 
#        print a, b, len(aList), len(bList), newList
        if aList[a] < bList[b]:
            newList.append(aList[a])
            a += 1
        else:
            newList.append(bList[b])
            b += 1
    while a < len(aList):
        newList.append(aList[a])
        a += 1
    while b < len(bList):
        newList.append(bList[b])
        b += 1
    return newList 


def merge_sort(aList):
    pivot = len(aList)/2
    if pivot == 0:
        return aList[pivot:pivot+1]
    left_list = aList[:pivot]
    right_list = aList[pivot:]

    return merge(merge_sort(left_list), merge_sort(right_list))

print "Just merging two list ordered or unordered:"
print
print merge( [1,3,5,5,9], [4,6,7] )
print merge( [5,3,1,9,5], [4,6,7] )
print merge( [2,5,3,1,9,5], [] )
print merge( [], [] )
print merge( [1], [] )
print merge( [], [1] )
print merge( [1, 5], [2] )

print
print "And now ordering a list using merge sort:"
print
print merge_sort( [5,3,1,9,4,6,5,4] )
print merge_sort( [5,3] )
print merge_sort( [8] )
print

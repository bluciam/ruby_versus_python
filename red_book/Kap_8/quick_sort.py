def quick_sort(aList):
    '''
    Quick sort recursively, returns sorted array
    '''
    pivot = len(aList)/2
    if pivot == 0:
        return aList[pivot:pivot+1]
    left_list = []
    right_list = []
    for i in range(0, len(aList)):
        if pivot == i:
            continue
        if aList[i] < aList[pivot]:
            left_list.append(aList[i])
        else:
            right_list.append(aList[i])
    return quick_sort(left_list) + aList[pivot:pivot+1] + quick_sort(right_list)


print quick_sort( [5,3,1,9,5] )
print quick_sort( [2,5,3,1,9,5] )
print quick_sort( [] )
print quick_sort( [1] )


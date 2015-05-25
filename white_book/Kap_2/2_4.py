def list_partition(aList, value):
    list_less = []
    list_greater_eq = []
    for n in aList:
        if n < value:
            list_less.append(n)
        else:
            list_greater_eq.append(n)
    return list_less + list_greater_eq


print list_partition([3,6,1,78,9,2,54,4,8,9], 10)

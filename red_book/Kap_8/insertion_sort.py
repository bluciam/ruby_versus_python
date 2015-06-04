def insert_sort(aList, elem):
    """ 
    Inserting one element at a time into a list. Return list.
    """
    if len(aList) == 0:
        aList.append(elem)
        print aList
        return aList
    for i in range(0, len(aList)):
        if elem < aList[i]:
            aList.insert(i, elem)
            print aList
            return aList
        i += 1
    aList.append(elem)
    print aList
    return aList


b = insert_sort([], 2)
b = insert_sort(b, 6)
b = insert_sort(b, 4)
b = insert_sort(b, 1)
b = insert_sort(b, 9)
b = insert_sort(b, 'l')

a = [5,6,9]
insert_sort(a, 3)
print a

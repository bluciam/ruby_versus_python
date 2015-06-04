def insert_sort(aList, elem):
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

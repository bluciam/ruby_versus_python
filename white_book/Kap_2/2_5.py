def adding_list_LE(aList, bList):
    if len(aList) > len(bList):
        for i in range(len(bList), len(aList)):
            bList.append(0)
            print bList
    elif len(aList) < len(bList):
        for i in range(len(aList), len(bList)):
            aList.append(0)
        
    a, b = 0, 0
    for i in range(0, len(aList)):
        a += aList[i] * 10**i
        b += bList[i] * 10**i
    r = a + b
    return list(str(r))

def adding_list_BE(aList, bList):
    if len(aList) > len(bList):
        for i in range(0, len(aList) - len(bList)):
            bList.insert(i,0)
            print bList
    elif len(aList) < len(bList):
        for i in range(0, len(bList) - len(aList)):
            aList.insert(i,0)
    print aList
    print bList
        
    a, b = 0, 0
    r_i = len(aList)
    for i in range(0, r_i):
        r_i -= 1
        a += aList[i] * 10**r_i
        b += bList[i] * 10**r_i
    r = a + b
    return list(str(r))

print adding_list_LE([1,3], [2,2])
print adding_list_LE([1,2,4], [9,9,9])
print adding_list_LE([1,2,4], [9,9,9,9])

print adding_list_BE([1,3], [2,2])
print adding_list_BE([1,2,4], [9,9,9])
print adding_list_BE([1,2,4], [9,9,9,9])

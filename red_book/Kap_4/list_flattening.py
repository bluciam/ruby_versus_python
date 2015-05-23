
def flat(aList, flatList = []):
    for item in aList:
        if type(item) is list:
            if len(item) == 1:
                flatList.append(item[0])
                print "Is a list with 1 item."
            else:
                flat(item, flatList)
                print "A list!"
        else:
            print "Is an ordinary down of the mill"
            flatList.append(item)
    return flatList


print flat([[1,2, ['a','b']], 3, 5, 7, ['z']])

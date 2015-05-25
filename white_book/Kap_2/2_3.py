def del_elem_by_val(aList, val):
    try:
        aList.remove(val)
        return aList
    except Exception, e:
        return e
#        return "Element not in list"


def del_elem_by_index(aList, index):
    try:
        aList.pop(index)
        return aList
    except Exception, e:
        return e

print del_elem_by_val([1,6,4,5,3], 4)
print del_elem_by_index([1,6,4,5,3], 4)
    

def reverse(string):
    rev_str = ''
    str_index = len(string) 
    while str_index > 0:
        str_index -= 1
        rev_str = rev_str + string[str_index] 
    return rev_str


def reverse_inplace(aList):
    print aList
    start = 0
    end = len(aList) - 1
    while end > start:
        temp = aList[start]
        aList[start] = aList[end]
        aList[end] = temp
        end -= 1
        start += 1
    return aList


print reverse('hello')
print reverse_inplace(list('hello'))
print reverse_inplace(list('abcdef'))
print reverse_inplace([])

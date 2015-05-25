def reverse(string):
    rev_str = ''
    str_index = len(string)
    while str_index > 0:
        str_index -= 1
        rev_str = rev_str + string[str_index]
    return list(rev_str)


def is_palindrome(aList):
    if isinstance(aList, str):
        myList = list(aList.lower())
    elif isinstance(aList, list):
        myList = list(''.join(aList).lower())
    else:
        return "Wrong data type, only string or list accepted."

    for item in myList[:]:
        if not item.isalnum():
            myList.remove(item)

    reverse_lst = reverse(myList)
    print reverse_lst
    print myList
    if reverse_lst == myList:
        return True
    else:
        return False


print is_palindrome(list('aa bbbaa'))
print is_palindrome(list('aa bbbaa ?'))
print is_palindrome("Was it a car or a cat I saw?")
print is_palindrome(235686)

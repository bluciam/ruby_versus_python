def reverse(string):
    rev_str = ''
    str_index = len(string) 
    while str_index > 0:
        str_index -= 1
        rev_str = rev_str + string[str_index] 
    return rev_str

print reverse('hello')

def are_repeated(string):
    for i,c in enumerate(string):
        print i, c
        for o in range(i+1,len(string)):
            if string[o] == c:
                return True
                break
    return False

def are_repeated2(string):
    a = list(set(string))
    b = list(string)
    if a == b:
        return False
    else:
        return True

print are_repeated('hello')
print are_repeated('helo')
print are_repeated2('hello')
print are_repeated2('helo')

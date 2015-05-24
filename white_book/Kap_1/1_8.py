def isSubstring(sub_s1, s1):
    if sub_s1 in s1:
        return True
    else:
        return False

def isRotation(s1, s2):
    c = s1[0]
    substr2_p1 = []
    substr2_p2 = []
    for i, value in enumerate(s2):
        if c != value:
            substr2_p1.append(value)
        else:
            for char_i in range(i,len(s2)):
                substr2_p2.append(s2[char_i])
            break
    return isSubstring(s1, ''.join(substr2_p2) + ''.join(substr2_p1))

def isRotationSimple(s1, s2):
    return isSubstring(s1, s2+s2)

print isRotation("hello", "lohel")
print isRotation("hello", "lohell")

print isRotationSimple("hello", "lohel")
print isRotationSimple("hello", "lohell")


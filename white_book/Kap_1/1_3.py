def is_permutation(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

print is_permutation("helo", "lohe")
print is_permutation("hello", "lohe")
print is_permutation("hello", "lohhee")


def non_repeated(string):
    used_chars = []
    i = 0
    while i < len(string):
        current_char = string[i]
        i += 1
        if current_char in used_chars:
            continue
        else:
            if i == len(string):
                print "Found it! "
                return current_char
            for j in range(i,len(string)):
                if current_char == string[j]:
                    used_chars.append(current_char)
                    break
            else:
                print "Found it! "
                return current_char
    print "There are no non-repeated chars. :-("


print non_repeated("")
print non_repeated("aab")
print non_repeated("Hello")
print non_repeated("a")
print non_repeated("eloHHelo")

                

def str_compresion(string):
    comp_str = ''
    index = 0
    while index < len(string):
        run_i = index
        count = 0
        while string[run_i] == string[index]:
            count += 1
            index += 1
            if index == len(string):
                break
        comp_str = comp_str + string[run_i] + str(count)

    if len(comp_str) > len(string):
        return string
    else:
        return comp_str

print str_compresion("hellllllllo")
print str_compresion("hello")

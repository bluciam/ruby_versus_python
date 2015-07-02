def fact_2_bin(num):
    if num <= 0 or num >= 1:
        return "Error, number out of bounds"

    str_frac = '.'
    while num > 0:
        print str_frac
        if len(str_frac) > 32:
            return "Error, frac too long"
        num = num * 2
#        print num
        if num >= 1:
            str_frac = str_frac + '1'
            num -= 1
        else:
            str_frac = str_frac + '0'

    print str_frac

    if num != 0:
        return "Error"
    else:
        return str_frac

print fact_2_bin(0.625)
print fact_2_bin(0.255)


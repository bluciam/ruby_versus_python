def string_char(string):
    number, exp = 0, len(string) - 1
    start, mult = 0, 1
    if string[0] is '-':
        start = 1
        mult = -1
        exp -= 1
    for i in range(start,len(string)):
        number += int(string[i]) * 10**exp
        exp -= 1
    return number * mult


def char_string(number):
    string = []
    temp = []

    if number is 0:
      return str(0)

    if number < 0:
        number *= -1
        string.append('-')

    while number != 0:
        digit = number % 10
#        print "digit" , digit
        number = number / 10
#        print "number" , number
        temp.append(str(digit))
#        print temp

    for i in reversed(range(0, len(temp))):
        string.append(temp[i])
    return ''.join(string)


print string_char('123')
print string_char('-9878')
print string_char('0')

print char_string(69)
print char_string(-2569)
print char_string(0)

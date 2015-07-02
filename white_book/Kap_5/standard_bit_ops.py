## The definition of i in to loose. Is it the ith bit or is it the bit
## in the ith position from the right, which starts counting at 0?
import sys

def test(func, expected):
    if func == expected:
        sys.stdout.write(".")
    else:
        sys.stdout.write("F")

def get_bit(num, i):
    my_num = 1 << i
    return (my_num & num) != (0)

def set_bit(num, i):
    my_num = 1 << i
    return (my_num | num)
    
def clear_bit(num, i):
    my_num1 = 0b11111111 << i
#    print "my_num1 ", bin(my_num1)
    my_num2 = 1 << i -1
    my_num2 -= 1
#    print "my_num2 ", bin(my_num2)
    my_num = my_num1 + my_num2
#    print "num ", bin(num)
#    print "my_num ", bin(my_num)
#    print  bin(my_num & num)
#    print ""
    return (my_num & num)

def clear_bits_i20(num, i):
    my_num = 0b11111111 << i
    return (my_num & num)
    
def clear_bits_m2i(num, i):
    my_num = 1 << i
    my_num -= 1
    return (my_num & num)
    

test( get_bit(0b0101, 3), False)
test( get_bit(0b1101, 3), True)
test( get_bit(0b1, 3), False)
test( get_bit(0b1, 0), True)
print ("")
test( set_bit(0b0101, 3), 0b1101)
test( set_bit(0b1100, 3), 0b1100)
test( set_bit(0b1, 3), 0b1001)
test( set_bit(0b0, 3), 0b1000)
test( set_bit(0b0, 0), 0b1)
print ("")
test( clear_bit(0b11110101, 3), 0b11110001)
test( clear_bit(0b0101, 3), 0b0001)
test( clear_bit(0b1100, 3), 0b1000)
test( clear_bit(0b1, 3), 0b0001)
test( clear_bit(0b0, 3), 0b0000)
test( clear_bit(0b1, 1), 0b0)
print ("")
test (clear_bits_i20(0b11111111, 4), 0b11110000)
test (clear_bits_i20(0b1111, 4), 0b0000)
test (clear_bits_i20(0b1111, 0), 0b1111)
test (clear_bits_i20(0b10101010, 4), 0b10100000)
print ("")
test (clear_bits_m2i(0b11111111, 4), 0b00001111)
test (clear_bits_m2i(0b1111, 4), 0b1111)
test (clear_bits_m2i(0b1111, 0), 0b0000)
test (clear_bits_m2i(0b10101010, 4), 0b00001010)
print ("")

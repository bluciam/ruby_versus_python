def get_prev(num):
    print "original ", bin(num), num
    ## Count the number of ones and zeros until the first non leading zero
    zeros = 0
    ones = 0
    c = num
    while ((c & 1) == 1) and c != 0:
        c >>= 1
        ones += 1
    while ((c & 1) == 0) and c != 0:
        c >>= 1
        zeros += 1

    print zeros, ones

    ## for a 32-bit number, return if cannot get a bigger number
    ## not working for other sizes, I would need the length of the number.
    if (zeros + ones == 32) or (zeros + ones == 0):
        return -1

    ## zero p and all bits to its right. 
    mask = ( 1 << 32 ) - 1
    mask <<= (ones + zeros + 1)
    new_num = num & mask

    ## create the bits to the left of p according to the numbers of 0 and 1
    ## perform an | to get the final number
    right = 0
    for i in range(0, ones+1):
        right <<= 1
        right |= 1
    for i in range(0, zeros-1):
        right <<= 1
    print "prev num ", bin(right | new_num), (right | new_num)



get_prev(13967)
print
get_prev(0b01100000)
print
get_prev(0b01100011)
print
get_prev(259)
print
get_prev(226)

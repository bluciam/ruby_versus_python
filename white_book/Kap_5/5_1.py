def m_in_n(n,m,i,j):
    m1 = m << i
    print "m1 ", bin(m1)
    n1 = 0b11111111111111 << j+1
    print "n1 ", bin(n1)
    n2 = (1 << i) - 1
    print "n2 ", bin(n2)
    n3 = n1 | n2
    print "n3 ", bin(n3)
    n4 = n3 & n
    print "n4 ", bin(n4)
    return bin(n4 | m1)


print m_in_n(0b10000000000, 0b10011, 2,6)

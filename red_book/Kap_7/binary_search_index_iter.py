def binary_search(my_array, value):
    low = 0
    high = l = len(my_array)
    if l is 0:
        print "Error, item not found."
        return 
    if l is 1:
        if value is my_array[0]:
            return 0
        else:
            print "Error, item not found."
            return

    while (high - low) > 0:
        print "*"
        index = low + (high-low)/2
        if value is my_array[index]:
            return index
        if value < my_array[index]:
            high = index
        else:
            low = index + 1

print binary_search([],1)
print []
print
print binary_search([1,4],1)
print [1,4],1
print
print binary_search([1,2,4],1)
print [1,2,4],1
print
print binary_search([1,4,5,6,7,8,9],1)
print [1,4,5,6,7,8,9], 1
print
print binary_search([1,4,5,6,7,8,9],4)
print [1,4,5,6,7,8,9], 4
print
print binary_search([1,4,5,6,7,8,9],5)
print [1,4,5,6,7,8,9], 5
print
print binary_search([1,4,5,6,7,8,9],6)
print [1,4,5,6,7,8,9], 6
print
print binary_search([1,4,5,6,7,8,9],7)
print [1,4,5,6,7,8,9], 7
print
print binary_search([1,4,5,6,7,8,9],8)
print [1,4,5,6,7,8,9], 8
print
print binary_search([1,4,5,6,7,8,9],9)
print [1,4,5,6,7,8,9], 9
print
print binary_search([1,4,5,6,7,8,9],2)
print [1,4,5,6,7,8,9], 2

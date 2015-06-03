def binary_search(my_array, value, low=0, high=None):
    if high is None:
        high = l = len(my_array)
    else:
        l = len(my_array[low:high])
    index = low + (high-low)/2
    print "*"
    if l is 0:
        print "Error, item not found."
        return 
    if l is 1:
        if value is my_array[index]:
            return index
        else:
            print "Error, item not found."
            return
    if value is my_array[index]:
        return index
    if value < my_array[index]:
        return binary_search(my_array, value, low, index)
    else:
        return binary_search(my_array, value, index + 1, high)

print binary_search([],1)
print []
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

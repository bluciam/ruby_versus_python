def binary_search(my_array, value):
    l = len(my_array)
    if l is 0:
        print "Error, array is empty!"
        return 
    if l is 1:
        if value is my_array[0]:
            return my_array[0]
        else:
            print "Error, item not found."
            return
    index = l/2
    if value is my_array[index]:
        return my_array[index]
    if value < my_array[index]:
        return binary_search(my_array[:(index)], value)
    else:
        return binary_search(my_array[(index + 1):], value)


    array_1 = my_array[:(index)]
    array_2 = my_array[(index + 1):]


    print my_array
    print (array_1)        
    print (array_2)        
    print len(array_1)        
    print len(array_2)        

print binary_search([],1)
print binary_search([1,4,5,6,7,8,9],1)
print binary_search([1,4,5,6,7,8,9],4)
print binary_search([1,4,5,6,7,8,9],5)
print binary_search([1,4,5,6,7,8,9],6)
print binary_search([1,4,5,6,7,8,9],7)
print binary_search([1,4,5,6,7,8,9],8)
print binary_search([1,4,5,6,7,8,9],9)
print binary_search([1,4,5,6,7,8,9],2)

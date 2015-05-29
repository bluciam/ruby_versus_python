from my_test import my_test
class Stack:
    def __init__(self, aList=[]):
        self.stack = aList
        self.minimum = self.find_new_min()

    def peek(self):
        return self.stack[0]

    def pop(self):
        try:
            popped = self.stack.pop()
        except Exception, e:
            print  e
            return e

        if popped == self.minimum:
#            print "Popped the min"
            self.minimum = self.find_new_min()
        return popped

    def push(self, elem):
        self.stack.append(elem)
        if elem < self.minimum:
            self.minimum = elem

    def __repr__(self):
        to_prt = "[ "
        for i in self.stack:
            to_prt += str(i) + " "
        to_prt += "]"
        return to_prt

    def find_new_min(self):
#        print "Need to find the new min"
        if self.stack == []:
            return
        minimum = self.stack[0]
        for elem in self.stack:
            if elem < minimum:
                minimum = elem
        return minimum


## Yes I know, I need to have real tests...
myStack = Stack()
my_test(not myStack, False)
my_test(myStack.stack, [])
my_test(myStack.minimum, None)
print

myStack = Stack([3,6,4,2,0])
my_test(myStack.minimum, 0)
myStack.push(0)
my_test(myStack.minimum, 0)
myStack.push(9)
my_test(myStack.minimum, 0)
myStack.pop()
myStack.pop()
myStack.pop()
my_test(myStack.minimum, 2)

print
myStack = Stack([4,2])
my_test(myStack.minimum, 2)
myStack.pop()
my_test(myStack.minimum, 4)
my_test(myStack.stack, [4] )
myStack.pop()
my_test(not myStack, False)
my_test(myStack.minimum, None)

'''
print myStack
print myStack.minimum
myStack.pop()
print myStack
print myStack.minimum
myStack.pop()
print myStack
print myStack.minimum

def my_test(function, expected):
    if function == expected:
        print '.' ,
    else:
        print 'F',
'''

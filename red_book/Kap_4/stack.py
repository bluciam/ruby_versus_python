class Stack:
    def __init__(self, aList):
        self.stack = aList

    def pop(self):
        self.stack.pop()

    def push(self, elem):
        self.stack.append(elem)

    def __repr__(self):
        to_prt = "[ "
        for i in self.stack:
            to_prt += str(i) + " "
        to_prt += "]"
        return to_prt

my_stack = Stack([1,3,5,7])
print my_stack
my_stack.push(11)
print my_stack
my_stack.pop()
print my_stack
my_stack.pop()
print my_stack

my_str_stack = Stack(['a','c','e'])
print my_str_stack
my_str_stack.push('z')
print my_str_stack
my_str_stack.pop()
print my_str_stack
my_str_stack.pop()
print my_str_stack

my_str_stack = Stack([[6,7,8],('a',1),('c',3),('e',5)])
print my_str_stack
my_str_stack.push('z')
print my_str_stack
my_str_stack.pop()
print my_str_stack
my_str_stack.pop()
print my_str_stack

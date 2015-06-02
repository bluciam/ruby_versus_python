class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, elem):
        self.stack.append(elem)

    def __repr__(self):
        to_prt = "[ "
        for i in self.stack:
            to_prt += str(i) + " "
        to_prt += "]"
        return to_prt

class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def is_leave(self):
        if self.value == None:
            return True
        else:
            return False

    def insert(self, value):
        if self.is_leave():
            self.value = value
            self.left = Node()
            self.right = Node()
        else:
            if value <= self.value:
                self.left.insert(value)
            else:
                self.right.insert(value)

    def height(self):
        if self.is_leave():
            return 0
        return 1 + max(self.left.height(), self.right.height())

    def ancestor(self, val1, val2):
        if self.is_leave():
            return None
        if val1 > val2:
            return self.ancestor(val2, val1)
        if val1 > self.value:
            return self.right.ancestor(val1, val2)
        if val2 < self.value:
            return self.left.ancestor(val1, val2)
        return self

    def traverse_pre(self):
        if not self.is_leave():
            print self.value
            self.left.traverse_pre()
            self.right.traverse_pre()

    def traverse_pre_stack(self):
        the_stack = Stack()
        the_stack.push(self)
        while len(the_stack.stack) > 0:
            curr = the_stack.pop()
            print curr.value
            if not curr.right.is_leave():
                the_stack.push(curr.right)
            if not curr.left.is_leave():
                the_stack.push(curr.left)

            
        
        
        

my_bsd = Node()
my_bsd.insert(5)
my_bsd.insert(4)
my_bsd.insert(6)
my_bsd.insert(1)
my_bsd.insert(1)
print my_bsd.value,
print my_bsd.left.value,
print my_bsd.right.value
print
print my_bsd.height()
print
print my_bsd.ancestor(1,6).value,
print my_bsd.ancestor(6,1).value,
print my_bsd.ancestor(4,4).value
print
#my_bsd.traverse_pre()
print
my_bsd.traverse_pre_stack()

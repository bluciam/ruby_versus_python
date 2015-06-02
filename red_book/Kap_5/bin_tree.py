class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.value is None

    def insert(self, value):
        if self.is_leaf():
            self.value = value
            self.left = Node()
            self.right = Node()
        elif value <= self.value:
            self.left.insert(value)
        else:
            self.right.insert(value)

    def traverse_in(self):
        if not self.is_leaf():
            self.left.traverse_in()
            print self.value,
            self.right.traverse_in()

    def traverse_pre(self):
        if not self.is_leaf():
            print self.value,
            self.left.traverse_pre()
            self.right.traverse_pre()

    def traverse_post(self):
        if not self.is_leaf():
            self.left.traverse_post()
            self.right.traverse_post()
            print self.value,

    def height(self):
        if self.is_leaf():
            return 0
        return 1 + max(self.left.height(), self.right.height())

    def find(self, value):
        if self.is_leaf():
            return None
        if value == self.value:
            return self
        if value < self.value:
            return self.left.find(value)
        return self.right.find(value)

    def find_ancestor(self, low_val, high_val):
        if self.is_leaf():
            return None
        if low_val > high_val:
            return self.find_ancestor(high_val, low_val)
        if high_val < self.value:
            return self.left.find_ancestor(low_val, high_val)
        if low_val > self.value:
            return self.right.find_ancestor(low_val, high_val)
        return self

    def leftmost_child(self):
        if self.is_leaf():
            return None
        if self.left.is_leaf():
            return self
        return self.left.leftmost_child()

    def rightmost_child(self):
        if self.is_leaf():
            return None
        if self.right.is_leaf():
            return self
        return self.right.rightmost_child()

    def __repr__(self):
        if self.is_leaf():
            return '*'
        return '<' + self.left.__repr__() + \
            str(self.value) + self.right.__repr__() + '>'
            


my_bst = Node()
my_bst.insert(6)
my_bst.insert(7)
my_bst.insert(7)
my_bst.insert(2)
my_bst.insert(1)

my_bst.traverse_in()
print
my_bst.traverse_post()
print
my_bst.traverse_pre()
print
print my_bst.height()

print my_bst

print my_bst.find(5)
print my_bst.find_ancestor(2,7).value
print my_bst.find_ancestor(1,2).value
print my_bst.find_ancestor(1,1).value
print my_bst.find_ancestor(7,2).value


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

    ## Needs verifying
    def leftmost_child(self):
        if self.is_leaf():
            return None
        if self.left.is_leaf():
            return self
        return self.left.leftmost_child()

    ## Needs verifying
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
            



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

    def is_empty(self):
        if len(self.stack) is 0:
            return True
        else:
            return False

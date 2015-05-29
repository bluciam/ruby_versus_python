class SetOfStack:
    def __init__(self, threshhold, elem):
        self.counter = 0
        self.threshhold = threshhold
        self.stacks = []
        self.stacks.append([])
        self.stacks[self.counter].append(elem)

    def push(self, elem):
        if len(self.stacks[self.counter]) == self.threshhold:
            self.counter += 1
            self.stacks.append([])
        self.stacks[self.counter].append(elem)

    def pop(self, which=None):
        if which is None:
            which = self.counter
            print self.counter
        try:
            self.stacks[which].pop()
            if not self.stacks[which]:
                del self.stacks[which]
                self.counter -= 1
                if self.counter < 0:
                    self.counter = 0
                    self.stacks.append([])
        except Exception, e:
            print e
            return e



my_set = SetOfStack(2, 5)
print my_set.stacks

my_set.push(3)
my_set.push(8)
my_set.push(5)
my_set.push(0)
my_set.push(1)
my_set.push(1)

print my_set.stacks

my_set.pop()
print my_set.stacks
my_set.pop(0)
print my_set.stacks
my_set.pop(0)
print my_set.stacks
my_set.pop()
print my_set.stacks

for i in range(0,5):
    my_set.pop()
    print my_set.stacks

my_set.push(8)
my_set.push(5)
my_set.push(0)
my_set.push(1)
print my_set.stacks

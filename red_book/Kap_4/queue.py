class Queue:
    def __init__(self, aList):
        self.queue = aList

    def dequeue(self):
        self.queue.pop(0)

    def enqueue(self, elem):
        self.queue.append(elem)

    def __repr__(self):
        to_prt = "[ "
        for i in self.queue:
            to_prt += str(i) + " "
        to_prt += "]"
        return to_prt

my_queue = Queue([1,3,5,7])
print my_queue
my_queue.enqueue(11)
print my_queue
my_queue.dequeue()
print my_queue
my_queue.dequeue()
print my_queue

my_str_queue = Queue(['a','c','e'])
print my_str_queue
my_str_queue.enqueue('z')
print my_str_queue
my_str_queue.dequeue()
print my_str_queue
my_str_queue.dequeue()
print my_str_queue

my_str_queue = Queue([[6,7,8],('a',1),('c',3),('e',5)])
print my_str_queue
my_str_queue.enqueue('z')
print my_str_queue
my_str_queue.dequeue()
print my_str_queue
my_str_queue.dequeue()
print my_str_queue

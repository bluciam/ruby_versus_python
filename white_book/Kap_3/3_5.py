from stack import Stack

class MyQueue:
    def __init__(self):
        self.stack_in  = Stack()
        self.stack_out = Stack()

    def enqueue(self, item):
        if not self.stack_in.is_empty():
            self.empty_stack(self.stack_in, self.stack_out)
        self.stack_in.push(item)

    def dequeue(self):
        if not self.stack_out.is_empty():
            self.empty_stack(self.stack_out, self.stack_in)
        return self.stack_in.pop()


    def empty_stack(self, stack1, stack2):
        '''
        Empty stack1 into stack2
        '''
        while not stack1.is_empty():
            stack2.push(stack1.pop())

    def print_mq(self):
        self.empty_stack(self.stack_in, self.stack_out)
        print self.stack_out

super_queue = MyQueue()
super_queue.print_mq()
super_queue.enqueue(3)
super_queue.print_mq()
super_queue.enqueue(5)
super_queue.print_mq()
super_queue.enqueue(7)
super_queue.print_mq()
super_queue.enqueue(4)
super_queue.print_mq()
print super_queue.dequeue()
super_queue.print_mq()
print super_queue.dequeue()
super_queue.print_mq()


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, value):
        if self.is_empty():
            self.stack1.append(value)
        else:
            for _ in self.stack1:
                # move all elements from stack 1 to stack 2
                self.stack2.append(self.stack1.pop())
            # enqueue the value to the end of the queue
            self.stack1.append(value)
            # move all elements back to stack1
            for _ in self.stack2:
                self.stack1.append(self.stack2.pop())
    def dequeue(self):
        if len(self.stack1) == 0:
            return None
        return self.stack1.pop()
                

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
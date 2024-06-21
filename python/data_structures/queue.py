class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        out = ""
        while temp is not None:
            out += str(temp.value) + '->'
            temp = temp.next
        print(out[:-2])

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
        else:
            self.last.next = new_node
        self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.first == None:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1 
        return temp

q = Queue(4)
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
q.print_queue()
print(q.dequeue().value)
print(q.dequeue().value)
print(q.dequeue())
q.print_queue()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.height += 1
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp
        

stack = Stack(10)
stack.push(9)
stack.push(8)
stack.print_stack()
print('\n', stack.pop().value, '\n')
stack.print_stack()

    


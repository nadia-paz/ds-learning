class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_dll(self):
        curr = self.head
        while curr:
            print(curr.value, end=" ")
            curr = curr.next
        print()

    def append(self, value):
        new_node = Node(value)
        # if self.length == 0:
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        
        
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        """
        Optimized for DLL, can move forward and backwards
        """
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            # print("next")
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                # print("prev")
                temp = temp.prev
        return temp


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.prepend(0)
dll.print_dll()
print(dll.get(2).value)
# dll.print_dll()
# print(dll.pop_first().value)
# dll.print_dll()
# print(dll.length)
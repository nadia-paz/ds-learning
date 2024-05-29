class Node:
    """
    Creates a Node of a LinkedList.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        """  
        Constractor inizializes a LinkedList by creating a new Node with a value
        and pointing head and tail to this Node. 
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        # keep track of the LL length
        self.length = 1

    def print_list(self):
        """
        Prints all values of the LinkedList 
        """
        # start at head
        temp = self.head
        while temp is not None:
            # print value of Nodes until reaches tail
            print(temp.value)
            # move to the next Node
            temp = temp.next
        
    def append(self, value):
        """ 
        Appends a new Node to the end of the LinkedList
        """
        # create a new node with the value
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # point to the new node
            self.tail.next = new_node
            # move tail to the new node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
        Removes the last node from the LinkedList and returns it.
        Set the tail to the new last node.
        """
        if self.length == 0:
            return None
        # create temp (to remove and return)
        # create pre to be a new tail
        # point both variables to the head of LL
        temp = self.head
        pre = self.head
        # while the node is not tail
        while(temp.next):
            # point pre to temp
            pre = temp
            # move temp to the next node
            temp = temp.next
        # when temp hits tail, old tail node is equal temp
        # set pre as a new tail
        self.tail = pre
        self.tail.next = None
        # decrease the length of the LL
        self.length -= 1
        # if new length is 0
        if self.length == 0:
            # remove pointers
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        """
        Inserts a new value to the beginning of the LinkedList
        """
        # create a new node with value
        new_node = Node(value)
        # if the LL is empty, assign head and tail pointers to the new node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # point the new node to the LL's head
            new_node.next = self.head
            # move the LL's head to the new node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        """
        Removes the first node from the LinkedList. Assigns the head pointer to the 2nd node.
        Retures removed node
        """
        if self.length == 0:
            return None
        # create a temp node
        temp = self.head
        # move head to the 2nd node
        self.head = self.head.next
        temp.next = None
        self.length -= 1 
        if self.length == 0:
            self.tail = None
            
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            temp = self.get(index-1)
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
       
        prev = self.get(index-1)
        # node to remove
        temp = prev.next
        prev.next = temp.next
        # break the connection with the LL
        temp.next = None
        return temp

    def reverse(self):
        """
        Reverse the order of the linked list. Doesn't return anything
        """
        # swap 
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # create before and after nodes
        # we move arrows (connections from after to before)
        before = None # temp is still head
        after = temp.next

        # loop through the ll
        for _ in range(self.length):
            # move after one step forward
            after = temp.next
            # change temp pointer direction
            temp.next = before
            # move before to temp
            before = temp
            # move temp to after
            temp = after
            




# check get method
ll = LinkedList(0)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.set_value(4, "Four")
ll.insert(5, "Five")
ll.remove(5)
ll.print_list()

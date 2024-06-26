class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

""" 
Full Tree: every node has 0 or 2 children
Perfect Tree: symmetric
Complete Tree: Fills from Left to Right
"""
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if value == temp.value:
                return False
            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
def printTree(node, level=0):
        # node = self.root
        if node != None:
            printTree(node.right, level + 1)
            if level == 0:
                print("* " + str(node.value))
            else:
                print(' ' * 4 * level + '-> ' + str(node.value))
            printTree(node.left, level + 1)

bst = BinarySearchTree()
bst.insert(43)
bst.insert(27)
bst.insert(56)
bst.insert(49)
bst.insert(19)
bst.insert(17)
bst.insert(29)
bst.insert(63)



printTree(bst.root)

print(bst.contains(20))
print(bst.contains(17))
""" 
Implementation of Binary Search Tree with one class only.
Binary Search Tree: 
    For any Node N, the value of any node in N's left subtree is less that N's value,
    and the value of any node in N's right subtree is greater than N's value.
    Only unique values are acceptable
"""

class TreeNode:
    def __init__(self, value: int, parent = None, left = None, right = None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        

    # def find_value(self, current, target: int):
    def find_value_rec(self, target:int):
        """ 
        Recursive function to find the tree node with the specific value

        Parameters:
            # current: TreeNode, the root of the BST
            target: int, value that has to be found in the BST
        Returns:
            TreeNode if target value is in the BST, otherwise None
        """
        current = self
        if current is None or current.value is None:
            return None
        if current.value == target:
            return current
        if target < current.value and current.left is not None:
            # return self.find_value(current.left, target)
            return current.left.find_value(target)
        if target > current.value and current.right is not None:
            # return self.find_value(current.right, target)
            return current.right.find_value(target)
        return None

    def find_value(self, target:int):
        """
        Iterative approach to find if target value is presented in the BST
        Parameters:
            target: int, value that has to be found in the BST
        Returns:
            TreeNode if target value is in the BST, otherwise None
        """
        current = self 
        while current and current.value != target:
            if target < current.value: current = current.left
            elif target > current.value: current = current.right
        return current

    def insert_node_rec(self, value:int):
        """
        Insert node with the value. Recursive function. 
        If the node with the value exists, prints "Failed to insert"
        Returns None
        """
        # case of nulls
        if self is None:
            self = TreeNode(value)
            return
        
        if self.value is None:
            self.value = value
            return

        current = self
        new_node = TreeNode(value)
        # case if the node with this value already exists 
        if value == current.value:
            print("Failed to insert")
            return
        # case if the value is smaller than current value
        if value < current.value:
            # check if left node is null than assign value else recursive call
            if current.left is None:
                # assign parent to the new node
                new_node.parent = current
                # connect the new node to the current on the left side
                current.left = new_node
                return
            else:
                current.left.insert_node(value)
        else: # value > current.value
            if current.right is None:
                # assign parent to the new node
                new_node.parent = current
                # connect the new node to the current on the left side
                current.right = new_node
                # exit 
                return
            else: # move down to the right and check if ok to insert there
                current.right.insert_node(value)

    def insert_node(self, value):
        """ 
        Iterative approach, inserts node with the while loop
        Returns True if inserted, False otherwise
        """
        new_node = TreeNode(value)
        # case of nulls
        if self is None:
            self = TreeNode(value)
            return True
        if self.value is None:
            self.value = value
            return True
        
        current = self
        new_node = TreeNode(value)
        while True:
            if value == current.value:
                return False
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    return True
                current = current.right
        
    def delete_node(self, value):
        # find the node to delete
        node = self.find_value(value)
        if node is None:
            return False

        # case when the node is a leaf (doesn't have children)
        if node.left is None and node.right is None:
            if node.parent is None: # it's only node in the tree
                del node
                return True
            if value < node.parent.value: # node is located to the left
                # break connections
                node.parent.left, node.parent = None, None
                del node
                return True
            if value > node.parent.value: # node is located to the right of parent
                node.parent.right, node.parent = None, None
                del node 
                return True
        
        # case when the node has on child
        if node.left is None or node.right is None:
            # has only chil on the righ
            if node.left is None:
                # connect child on the right to the new parent
                node.right.parent = node.parent
                node.parent.right = node.right
                # remove mode's connection
                node.parent, node.right = None, None
                del node
                return True
            else: # has a child on its left
                node.left.parent = node.parent
                node.parent.left = node.left
                node.parent, node.left = None, None
                del node
                return True

        # case when the node has two children
        


        




###############################################################

def printTree(node, level=0):
        # node = self.root
        if node != None:
            printTree(node.right, level + 1)
            if level == 0:
                print("* " + str(node.value))
            else:
                print(' ' * 4 * level + '-> ' + str(node.value))
            printTree(node.left, level + 1)

###############################################################
################ Test Functions ###############################

root = TreeNode(47)
left = TreeNode(33, parent=root)
right = TreeNode(56, parent=root)
root.left, root.right = left, right

# root.value = 47
# root.left = left
# root.right = right
# left.value = 33
# right.value = 56
# left.parent = right.parent = root

printTree(root)
for target in [12, 47, 33, 56, 96]:
    result = root.find_value(target)
    print(result.value if result else result)

print("\nCheck insert")
print(root.insert_node(12))
root.insert_node(6)
root.insert_node(44)
root.insert_node(45)
root.insert_node(53)
print(root.insert_node(6)) # should be False, 6 already exists
printTree(root)

root1 = TreeNode(None)
root1.insert_node(2)
printTree(root1)

print("\nCheck delete")
print(root.delete_node(12))
print(root.delete_node(44))
printTree(root)

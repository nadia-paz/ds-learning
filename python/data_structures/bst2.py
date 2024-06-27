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

def printTree(node, level=0):
        # node = self.root
        if node != None:
            printTree(node.right, level + 1)
            if level == 0:
                print("* " + str(node.value))
            else:
                print(' ' * 4 * level + '-> ' + str(node.value))
            printTree(node.left, level + 1)

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
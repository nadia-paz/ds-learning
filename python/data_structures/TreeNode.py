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
        
    def tree_to_array(self):
        # left
        if self.left: yield from self.left.tree_to_array()
        # value
        yield self.value
        # right
        if self.right: yield from self.right.tree_to_array()

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
        if self is None:
            return False
        if self.value is None:
            return False
        # find the node to delete
        node = self.find_value(value)
        if node is None:
            return False

        # case when the node is a leaf (doesn't have children)
        if node.left is None and node.right is None:
            if node.parent is None: # it's only node in the tree
                # del node
                return True
            if value < node.parent.value: # node is located to the left
                # break connections
                node.parent.left, node.parent = None, None
                # del node
                return True
            if value > node.parent.value: # node is located to the right of parent
                node.parent.right, node.parent = None, None
                # del node 
                return True
        
        # case when the node has one child
        if node.left is None or node.right is None:
            # has only child on the righ
            child = node.left if node.left else node.right
            child.parent = node.parent
            if node.parent.left == node:
                node.parent.left = child
            else:
                node.parent.right = child 
            return True

        # case when the node has two children
        # find a successor -> the minimum (or the leftmost) node in the right-hand subtree
        # if there is no leftmost node in the right subtree, the node's right child is a successor
        successor = node.right
        
        # if there is nothing on the left side, the right child is a successor
        is_right_child = False if successor.left else True

        # find leftmost node if exists
        while successor.left:
            successor = successor.left

        self.delete_node(successor.value)
        
        # place a successor on the node's position
        
        # check if it is root do nothing
        if node.parent is None:
            pass
        # otherwise it has a parent
        # point node's parent to successor
        elif node.parent.left == node:
            node.parent.left = successor
        elif node.parent.right == node:
            node.parent.right = successor
        successor.parent = node.parent
        
        # link successor to node's children

        #left side
        successor.left = node.left
        node.left.parent = successor

        # extra careful with the right child. it can be successor and can be removed
        # if not is_right_child:
        successor.right = node.right 
        if node.right != None:
            node.right.parent = successor


        # if the node is a root
        if successor.parent is None:
            self = successor
            self.left = successor.left
            self.right = successor.right

        # prints a tree with new root
        # doesn't do this when method called from outside and fails the test
        # printTree(self)
        # print(list(self.tree_to_array()))
        
        return True
            
            
        

###############################################################
################ Helper Functions #############################

def printTree(node, level=0):
        # node = self.root
        if node != None:
            printTree(node.right, level + 1)
            if level == 0:
                print("* " + str(node.value))
            else:
                print(' ' * 4 * level + '-> ' + str(node.value))
            printTree(node.left, level + 1)


def build_test_tree(extended = False, extended2 = False):
    root = TreeNode(47)
    left = TreeNode(33, parent=root)
    right = TreeNode(56, parent=root)
    root.left, root.right = left, right
    if extended:
        for i in [12, 6, 44, 45, 53]:
            root.insert_node(i)
    if extended2:
        root = TreeNode(50)
        for i in [23, 67, 14, 38, 60, 81, 6, 17, 27, 42, 59, 63, 78, 92, 1, 7, 21, 29, 58, 91, 95]:
            root.insert_node(i)
        
    # printTree(root)
    return root


###############################################################
################ Test Functions ###############################

def check_find_value():
    root = build_test_tree()
    a = [None, 47, 33, 56, None]
    values = []
    for target in [12, 47, 33, 56, 96]:
        result = root.find_value(target)
        values.append(result.value if result else result)
    try:
        assert a == values
        print("Find values works ok")
    except AssertionError:
        print("Find values works incorrect")


def check_insert():
    # check insert to the empty tree
    root1 = TreeNode(None)
    root1.insert_node(2)
    # printTree(root1)

    # check insert to the regular tree
    root = build_test_tree()
    for i in [12, 6, 44, 45, 53]:
        try:
            assert root.insert_node(i) == True
        except AssertionError:
            print("Insertion of %d failed" %i)
    try:
        root.insert_node(6) == False # should be False, 6 already exists
    except AssertionError:
        print("Fail. 6 already exist")
    # printTree(root)


def check_delete():
    # case the root is None
    print('\nCase empty tree')
    root = TreeNode(None)
    values = [None, 3]
    for v in values:
        try:
            root.delete_node(v) == False
            print(f'Value {v} - pass')
        except AssertionError:
            print(f'{v} didn\'t pass deletion test')
    
    # case the node is not found
    print('\nCase value not found')
    root = build_test_tree(extended=True)
    values = [3, 2, 1, 100]
    for v in values:
        try:
            root.delete_node(v) == False
            print(f'Value {v} - pass')
        except AssertionError:
            print(f'{v} didn\'t pass deletion test')


    # check leafs
    print('\nCase - delete leaves')
    root = build_test_tree(extended=True)
    # tree is [6, 12, 33, 44, 45, 47, 53, 56], root 47
    leafs = [6, 45, 53]
    for l in leafs:
        try:
            root.delete_node(l) == True
        except AssertionError:
            print(f"Leaf {l} - fail")
    try:
        list(root.tree_to_array()) == [12, 33, 44, 47, 56]
        print('Leaves deleted correctly')
    except AssertionError:
        print("Leaves deleted incorrect")
    
    # chech node with one child only
    print('\nCase one child only')
    root = build_test_tree(extended=True)
    # printTree(root)
    nodes = [12, 44, 56]
    for n in nodes:
        try:
            root.delete_node(n) == True
            # print(f'Node {n} - pass')
        except AssertionError:
            print(f'Node {n} - fail')
    try:
        list(root.tree_to_array()) == [6, 33, 45, 47, 53]
        print("Nodes with one child deleted correctly")
    except AssertionError:
        print("Nodes deleted incorrect")

    # case when node has 2 children
    root = build_test_tree(extended2=True)
    try:
        arr = [1, 6, 7, 14, 17, 21, 23, 27, 29, 38, 42, 50, 58, 59, 60, 63, 67, 78, 91, 92, 95]
        assert root.delete_node(81) == True
        assert list(root.tree_to_array()) == arr
        print('Node 81 - pass')
    except AssertionError:
        print('Node 81 - fail')
    try:
        arr = [1, 6, 7, 14, 17, 21, 23, 27, 29, 38, 42, 50, 58, 59, 60, 63, 67, 78, 92, 95]
        assert root.delete_node(91) == True
        assert list(root.tree_to_array()) == arr
        print('Node 91 - pass')
    except AssertionError:
        print('Node 91 - fail')
    # check deletion of the root
    try:
        arr = [1, 6, 7, 14, 17, 21, 23, 27, 29, 38, 42, 58, 59, 60, 63, 67, 78, 92, 95]
        assert root.delete_node(50) == True
        assert list(root.tree_to_array()) == arr
        print('Root - pass')
    except AssertionError:
        print('Root - fail') # returns fail, 
        # prints correct tree inside the delete_node method
        # solution 1 -> return a new tree and reasign
        # solution 2 -> create a class BinarySearchTree and in case of root make
        # self.root = successor



    
print("\nCheck find_value")
check_find_value()

print("\nCheck insert")
check_insert()

# printTree(build_test_tree(extended=True))
print("\nCheck delete")
check_delete()
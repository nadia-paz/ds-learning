class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

def is_balanced_parentheses(s):
    if len(s) % 2 == 1:
        return False
    if len(s) != 0 and s[0]==')':
        return False
    stack = Stack()
    is_balanced = False
    for p in s:
        if p == '(':
            stack.push(p)
        elif p == ')' and stack.peek != None:
            stack.pop()
        else:
            break
    if stack.is_empty():
        is_balanced = True
    return is_balanced

def reverse_string(string):
    
    if len(string) <= 1:
        return string
    
    s = Stack()
    # initiate reversed string
    new_string = ""
    
    for letter in string:
        s.push(letter)
   
    while not s.is_empty():
        new_string += s.pop()
    return new_string

def sort_stack(stack):
    # sorted_stack to keep the greatest value on the top
    sorted_stack = Stack()
    # O(n^2)
    while not stack.is_empty():
        # create a temp variable
        temp = stack.pop()
        # if temp variable is smaller that the greatest value of the sorted_stack
        while not sorted_stack.is_empty() and temp < sorted_stack.peek():
            # push the top of the sorted_stack back to stack
            stack.push(sorted_stack.pop())
        # push temp variable to the sorted_stack
        sorted_stack.push(temp)
    
    # move all elements back to the original stack, which makes the smallest element to be 
    # on top
    while not sorted_stack.is_empty():
        stack.push(sorted_stack.pop())



def test_is_balanced_parentheses():
    try:
        assert is_balanced_parentheses('((()))') == True
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert is_balanced_parentheses('()') == True
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        assert is_balanced_parentheses('(()())') == True
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert is_balanced_parentheses('(()') == False
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert is_balanced_parentheses('())') == False
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert is_balanced_parentheses(')(') == False
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert is_balanced_parentheses('') == True
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert is_balanced_parentheses('()()()()') == True
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert is_balanced_parentheses('(())(())') == True
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert is_balanced_parentheses('(()()())') == True
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')

    try:
        assert is_balanced_parentheses('((())') == False
        print('Test case 11 passed')
    except AssertionError:
        print('Test case 11 failed')

test_is_balanced_parentheses()
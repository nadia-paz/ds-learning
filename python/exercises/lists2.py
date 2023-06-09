''' 
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  
lines of commands where each command will be of the  types listed above. 
Iterate through each command in order and perform the corresponding 
operation on your list.
'''

if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        command = input()
        if command == 'print':
            print(l)
        elif command == 'pop':
            _ = l.pop()
        elif command == 'reverse':
            l.reverse()
        elif command == 'sort':
            l.sort()
        elif command.startswith('insert'):
            a = command.split()
            l.insert(int(a[1]), int(a[2]))
        elif command.startswith('remove'):
            a = command.split()
            m = int(a[1])
            if m in l:
                l.remove(m)
        elif command.startswith('append'):
            a = command.split()
            l.append(int(a[1]))

'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each
command will be of the 7 types listed above. Iterate through each command in order and 
perform the corresponding operation on your list
'''


n = int(input())
list_ = []
for i in range (n):
    a=input().split()
    if a[0]=='insert':
        list_.insert(int(a[1]),int(a[2]))
    elif a[0]=='print':
        print(list_)
    elif a[0]=='remove':
        list_.remove(int(a[1]))
    elif a[0]=='append':
        list_.append(int(a[1]))
    elif a[0]=='sort':
        list_.sort()
    elif a[0]=='pop':
        list_.pop()
    else:
        list_.reverse() 
'''Practice Problem: Print the following pattern where each 
row contains a number repeated a specific number of times based 
on its value.'''

n=int(input('entre no here : '))

def pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=' ')
        print()

pattern(n)

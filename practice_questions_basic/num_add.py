'''Practice Problem: Iterate through the first 10 numbers (0–9). 
In each iteration,print the current number, the previous number, and
their sum.'''


def sum(num1,num2):
    sum=num1+num2
    return (f'the current number is {num2} the previous number {num1} \
and there sum is {sum} ')


prev=0
for i in range(10):
    a=sum(i,prev)
    print(a)
    prev=i
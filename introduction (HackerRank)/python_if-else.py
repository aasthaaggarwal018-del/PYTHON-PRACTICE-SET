
'''
 Given an integer, , perform the following conditional actions:
If a is odd, print Weird
If a is even and in the inclusive range of 2 to 5 , print Not Weird
If a is even and in the inclusive range of 6 to 20, print Weird
If a is even and greater than 20, print Not Weird 
'''

a = int(input())
if a % 2 != 0:
    print('Weird')
elif 6<a<20:
    print('Weird')
else:
    print('Not Weird')



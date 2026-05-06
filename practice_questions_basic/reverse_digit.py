''': Write a program to 
extract each digit from an integer in the reverse order.'''



def rev(num):
    while num >0:
        digit = num % 10

        num = num // 10

        print(digit,end='')
        

rev(6789)

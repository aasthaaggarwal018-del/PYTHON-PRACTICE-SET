'''Practice Problem: Write a program that calculates the factorial
 of a given number (e.g., 5!) using a for loop.'''



def factorial(n):
    factorial=1  
    for i in range(1,n+1):
        factorial = i * factorial
    return factorial
    

print(factorial(5))
print(factorial(6))
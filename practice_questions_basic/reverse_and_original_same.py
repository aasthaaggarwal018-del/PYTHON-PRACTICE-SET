'''Write a program to check if a given number is a
 palindrome (reads the same forwards and backwards).'''

a=input('entre your no : ')
b= a[::-1]

def pali():
    if a ==b:
        print(True)
    else:
        print(False) 
    
    
    

pali()
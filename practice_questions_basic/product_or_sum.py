'''Practice Problem: Write a Python function that accepts two integer numbers. 
If the product of the two numbers is less than or equal to 1000, return their product; 
otherwise, return their sum.'''

def pro_or_sum (num1 , num2):
    pro=num1 * num2
    sum= num1 + num2

    if pro <=1000:
        return(pro)
    else:
        return(sum)
    

a = pro_or_sum(20,30)
print(a)

a=pro_or_sum(40,30)
print(a)
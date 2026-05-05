'''Practice Problem: Iterate through a given list of numbers and
 print only those numbers which are divisible by 5.'''


num_list = [10, 20, 33, 46, 55]

def div_5(n):
    for i in n:
        if i % 5 == 0:
            print(i)
       

div_5(num_list)
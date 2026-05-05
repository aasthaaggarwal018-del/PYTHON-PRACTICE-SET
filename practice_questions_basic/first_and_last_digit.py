'''Practice Problem: Write a function to return True if the 
first and last number of a given list is the same. 
If the numbers are different, return False.'''


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def same(number):

    if number[0]==number[-1]:
        print(True)
    else:
        print(False)


same(numbers_x)
same(numbers_y)
 
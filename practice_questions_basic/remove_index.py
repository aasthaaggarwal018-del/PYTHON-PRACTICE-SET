'''Write a function to remove characters from a string starting from index 0 up to n and return 
a new string.'''


def remove(word,n):
    print(f'original string : {word}')
    new_word = word[n:]
    return new_word


print(remove('aastha',3))

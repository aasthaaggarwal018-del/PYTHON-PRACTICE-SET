'''Practice Problem: Write a program to count the
 total number of vowels (a, e, i, o, u) present in a given sentence.'''



def vowel_c(word):
    vowel=0
    constant=0
    vowels=('aeiouAEIOU')
    for i in word:
        if i in vowels:
            vowel += 1
        else:
            constant +=1
    print (f'no of vowels are : {vowel} and constants are : {constant}')


vowel_c('apple')
vowel_c('aastha')

'''Display only those characters which are present at an even index number in given string.'''


word=input('entre word here :')
def even_index():
    for i in range(0,len(word),2):
            
            print(word[i])
        

print(f'word is {word} ')
even_index()



def x():


    vowel='aeiouAEIOU'
    v_count=0
    c_count=0

    i=input('entre your word here:')

    for j in i:
        if(j.isalpha()):
            if (j in vowel ):
                v_count+=1
            else:
                c_count+=1

    return v_count,c_count


a,b=x()
print(f'vowel are:{a} \nconstant are:{b}')
    
    


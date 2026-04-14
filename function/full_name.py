def full_name():
    a=input('entre your first name:')
    b=input('entre your last  name:')
    a=a.capitalize()
    b=b.capitalize()

    return a,b

f,l= full_name()

print(f'{f} {l}')

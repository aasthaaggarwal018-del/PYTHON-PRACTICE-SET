a=open('file_handling/text.txt','r')
data=a.read()
data=data.lower()

if 'aastha' in data:
    print('yes its present ')
else:
    print('not present')

if 'python' in data:
    print('yes its present ')
else:
    print('not present')

 
with open('file_handling/line_text.txt') as a:
    line_1 = a.readline()
    line_2 = a.readline()
    line_3 = a.read()
    print(line_1 , line_2 ,line_3)

'''
Given the names and grades for each student in a class of  students,
 store them in a nested list and print the name(s) of any student(s)
having the second lowest grade.
'''
score_list=[]
name_list=[]
record_list=[]
    
for _ in range(int(input())):
    name = input()
    score = float(input())
    record=[name,score]
    score_list.append(score)
    name_list.append(name)
    record_list.append(record)
    
a=sorted(set(score_list))
lowest_marks=a[1]
b=[i[0]for i in record_list if i[1] == lowest_marks]
b.sort()
for i in b:
    print (i)
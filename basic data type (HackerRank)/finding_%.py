'''The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.'''

if __name__ == '__main__':
    n = int(input('no of students:'))
    student_marks = {}
    for _ in range(n):
        data = input().split()
        name=data[0]
        marks_lst=data[1:]
        scores =[]
        for i in marks_lst:
            scores.append(float(i))
        student_marks[name] = scores
    query_name = input('entre student name :')
    marks=(student_marks[query_name])
    average=(sum(marks)/len(marks))
    b=f"{average:.2f}"
    print (b)
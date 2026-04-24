class student():
    school_name ='dav public school'
    city='amritsar'

    def __init__(self,name , roll ,marks):
        self.name = name
        self.roll = roll
        self.marks=marks

    def avg(self):
        sum=0
        for i in self.marks:
            sum +=i
        return sum/len(self.marks)


    def info(self):
        average = self.avg()
        print(f'{self.school_name} \n{self.city} \n{self.name} \n{self.roll} \n{average}')


student1=student('aastha',2,[45,56,93])
student1.info()
student2=student('vivek',6,[56,34,92])
student2.info()



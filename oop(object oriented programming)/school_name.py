class student ():
    school_name ='dav public school'
    city='amritsar'

    def __init__(self,name,roll_no):
        self.name=name
        self.roll=roll_no
       

    def show_details(self):
        print(f'{self.school_name}\n{self.city}')
        print(f'name : {self.name} \nroll no : {self.roll}')


student1 = student('aastha',2)
student1.show_details()
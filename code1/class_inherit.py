class SchoolMember:
    def __init__(self,age,name):
        self.age=age
        self.name=name
        print("(Initialized SchoolMember:%s)" % self.name)
    def tell(self):
        '''Tell my details.'''
        print("Name:%s Age:%d"%(self.name,self.age))
class Teacher(SchoolMember):
    '''Represents a teacher'''
    def __init__(self,age,name,salary):
        SchoolMember.__init__(self,age,name)
        self.salary=salary
    def tell(self):
        SchoolMember.tell(self)
        print("Salary:%d"%self.salary)
class Student(SchoolMember):
    '''Represents a Student'''
    def __init__(self,age,name,marks):
        SchoolMember.__init__(self,age,name)
        self.marks=marks
    def tell(self):
        SchoolMember.tell(self)
        print("Marks:%d" % self.marks)

t=Teacher(40,'Mr.Smith',2000)
s=Student(18,'John',99)
print # prints a blank line
members=[t,s]
for member in members:
    print(member.__doc__)
    member.tell()




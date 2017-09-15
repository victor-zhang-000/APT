#Q2 (a)
class Student(object):
    def __init__(self,name,GPA,age):
        self.name=name
        self.GPA=GPA
        self.age=age

    def __str__(self):
        return "Name: " + self.name +" GPA: "+ str(self.GPA) +" age: " + str(self.age)

    def __lt__(self, second):
        if(self.GPA< second.GPA):
            return True
        elif(self.GPA==second.GPA):
            if (self.name<second.name):
                return True
            elif((self.name==second.name)):
                if (self.age<second.age):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        return (self.GPA,self.name,self.age)==(other.GPA,other.name,other.age)


    def __hash__(self):
        return hash((self.name,self.age,self.GPA))

#(b)&(c)
s1= Student("Jack",4.0,22)
s2= Student("Tom",4.0,23)
s3= Student("Chloe",3.9,22)
s4= Student("Bob",3.4,24)
s5= Student("Peter",3.4,23)

studentlist=[]
studentlist.append(s1)
studentlist.append(s2)
studentlist.append(s3)
studentlist.append(s4)
studentlist.append(s5)


dict1={s1:"a", s2:"b", s3:"c"}
print(dict1[s1])

print ([str(student) for student in sorted(studentlist, key=lambda student:(student.GPA, student.name, student.age))])




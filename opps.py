
class Student:
    def __init__(self,name,rollNO):
        self.name = name
        self.rollNO =  rollNO

    def getName(self):
        print(self.name)

    def getRoll(self):
        print(self.rollNO)






st1 = Student("Shubham",1001)

st2 = Student("Aman",3002)

st1.getRoll()
st2.getRoll()

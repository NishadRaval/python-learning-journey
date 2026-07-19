class Employee:
    language = "Python"
    salary = 1200000

nishad = Employee()
nishad.language = "C++"
nishad.name = "Nishad"
print(nishad.name, nishad.language, nishad.salary)


class Test:
    subject = "Python"
    marks = 90

    def __init__(self):
        print("Hi Hello This is __init__")

    def getInfo(self): #so we use self to refer to the object that is calling the method
        print(f'scored {self.marks} in {self.subject}')

    @staticmethod
    def greet():
        print("Good Morning")

nishad = Test()
print(nishad.subject, nishad.marks)

rahi = Test()
print(rahi.subject, rahi.marks)

nishad.getInfo() #this is also written as Test.getInfo(nishad)
rahi.getInfo()

nishad.greet()
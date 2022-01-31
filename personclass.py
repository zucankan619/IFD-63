class Person:
   #default constructor
    def __init__(self,argname,argage) -> None:
       print('I am from Person Constructor') 
       self.name=argname
       self.age=argage
    
    def walk(self):
        print(f'{self.name} is now walking')
    
    def run(self):
        print(f'{self.name} {self.age} is now running')
    
    def show(self):
        print(f'I am {self.name} and {self.age} years old ')

# p1=Person('Ankan',19) 
# p1.walk()
# p1.run()
# p1.show()

#inheritance
class Student(Person):
    def __init__(self, argname, argage, argfees) -> None:
        super().__init__(argname, argage)
        self.fees=argfees
        print('I am from constructor of student class')

    #polymarphism
    def show(self):
        print(f'I am {self.name} and {self.age} years old my fees is {self.fees} TK ')


st1=Student('Didar', 12, 2000)
st1.walk()
st1.run()
st1.show()
 

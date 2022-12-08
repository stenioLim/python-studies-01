class Person:
    def __init__(self,name , last_name ):
        self.name = name 
        self.last_name = last_name

    def say_name_class(self):
        print(self.name, self.last_name, self.__class__.__name__)

class Client(Person):
    ...

class Student(Person):
    ...

c1 = Client('Stenio', 'Dllagrecia')
c1.say_name_class()
s1 = Student('Helena','Carla')
s1.say_name_class()
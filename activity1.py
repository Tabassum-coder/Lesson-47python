#Write a program to create a parent class Person (attributes - name, idnumber) with a method display to display the attributes.
#  Create a child class Employee (attributes - name, idnumber, salary, post).
#  Access the attributes of parent class in child class. 
# Then, create an object for child class and call the display method to display the name and idnumber.

#parent class
class Person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print("Name of person is ",self.name)
        print("Idnumber of person is ",self.idnumber)

#child class

class Employee(Person):
    def __init__(self, name, idnumber,salary,post):
        self.salary=salary
        self.post=post
        super().__init__(name, idnumber)

emp=Employee("Ali",1234,15000,"intern")
emp.display()
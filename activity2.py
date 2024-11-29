#Write a program to create a parent class Person (attributes - fname, lname) with a method printname to display the full name. 
# Create a child class Student (attributes - fname, lname, year). Access the attributes of parent class in child class using super() function.
#  Then, create an object for the child class and call the display method to display the full name. 
# Also, print the graduation year.

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print("Name of Person is {} {}".format(self.fname,self.lname))

class Student(Person):
    def __init__(self, fname, lname,year):
        self.graduationyear=year
        super().__init__(fname, lname)

stud=Student("Tabassum","Jahagirdar",2013)
stud.display()
print("Graduation year is ",stud.graduationyear)
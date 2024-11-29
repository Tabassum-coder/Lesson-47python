#Write a program to implement abstraction on animal class (base class).
#  The abstract method will be move that is for displaying what subclasses can do

from abc import ABC

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):
    def move(self):
        print(" I can bark")

class Lion(Animal):
    def move(self):
        print("I can Roar!")


h=Human()
h.move()

s=Snake()
s.move()

d=Dog()
d.move()

l=Lion()
l.move()
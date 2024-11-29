
from abc import ABC
import math

class polygon(ABC):
    def area(self):
        pass

class circle(polygon):
    def area(self,radius):
        print("Area of circle is ",(2*math.pi*radius**2))

c=circle()
c.area(8)
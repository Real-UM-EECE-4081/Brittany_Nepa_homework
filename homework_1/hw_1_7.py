#Write a Python class named Circle constructed by a radius and two methods that will compute the
#area and the perimeter of a circle.
import math

pi = math.pi

class Circle():
    def __init__(self, x):
        self.radius = x

    def area(self):
        return self.radius**2*pi

    def perimeter(self):
        return 2*self.radius*pi

Circle1 = Circle(2)

print("Area of a circle: ")
print(Circle1.area())
print("Area of perimeter")
print(Circle1.perimeter())
import math
class CircleClass :
    def __init__(self,radius) :
        self.radius = radius
    
    def circumference(self) :
        return "{:.2f}".format(2*math.pi*self.radius)

    def area(self) :
        return "{:.2f}".format(math.pi*(self.radius**2))

    def getRadius(self) :
        return self.radius


radius1 = float(input("Enter radius of Circle 1:"))

c1 = CircleClass(radius1)

radius2 = float(input("Enter radius of Circle 2:"))

c2 = CircleClass(radius2)


print("Circumference if circle 1:",c1.circumference())
print("Circumference if circle 2:",c2.circumference())

print("Area of circle 1:",c1.area())
print("Area of circle 2:",c2.area())

if(c1.getRadius()==c2.getRadius()) : print("Both Circle are Equal")
elif(c1.getRadius()>c2.getRadius()) : print("Circle 1 is bigger than Circle 2")
else : print("Circle 2 is bigger than Circle 1")



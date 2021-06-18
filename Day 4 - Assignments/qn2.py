# operator overloading

class Circle :
    def __init__(self,radius) :
        self.radius = radius
    def __eq__(self,other) :
        return self.radius==other.radius
    
radius1 = float(input("Enter the circle-1 radius :"))
c1 = Circle(radius1)
radius2 = float(input("Enter the circle-2 radius :"))
c2 = Circle(radius2)
print("True" if c1==c2 else "False")        #if c1==c2 (return TRUE otherwise return FALSE)
class Rectangle :
    def __init__(self,length,breadth) :
        self.length = length
        self.breadth = breadth

   
    def toFindArea(self) :
        return int(self.length*self.breadth)

length = float(input("Enter th length : "))
breadth = float(input("Enter the breadth : "))
r = Rectangle(length,breadth)
print(r.toFindArea())
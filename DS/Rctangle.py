class Rectangle:
     
    def __init__(self,length,width):
          self.length=length
          self.width=width

    def perimeter(self):
        return 2*(self.length+self.width)
    
    def area(self):
        return self.length*self.width

    def display(self):
        print("the length of rectangle is :",self.length)
        print('the width of rectangle is :',self.width)
        print('the area of the rectangle is:',self.area())
        print('the perimeter of the rectangle is:',self.perimeter())
myrectangle=Rectangle(2,3)
myrectangle.display()
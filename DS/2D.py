class Point:
    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y

    # cordinate
    def __str__(self):
        return '({},{})' .format(self.x_cod,self.y_cod)
    
    # distance b/w two point
    def eucodean_distance(self,other):
        return ((self.x_cod-other.x_cod)**2 + (self.y_cod-other.y_cod)**2)**0.5
    
    # distance from origin
    def distance_from_origin(self):
        # return (self.x_cod**2+self.y_cod**2)**0.5
        return self.eucodean_distance(Point(0,0))
    
    
class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C

    #line equation
    def __str__(self):
          
        
            return '{}x+{}y+{}=0'.format(self.A,self.B,self.C)
    
    # lies a point on given line 
    def point_on_line(line,point):

        if line.A*point.x_cod+line.B*point.y_cod+line.C==0:
            return "lies on line"
        
        else:
            return " not lies on line"

#shortest distance of a line form a given point
    def shortest_distance(line,point):
       return abs(line.A*point.x_cod+line.B*point.y_cod+line.C)/(line.A**2+line.B**2)**0.5
    # to check line are parallel or not
    def intersection(line1,line2):
        if line1.A*line2.B-line2.A*line1.B==0:
            return "lines are parallel"
        else:
            x=(line2.B*line1.C-line1.B*line2.C)/(line1.A*line2.B-line2.A*line1.B)
            y=(line1.A*line2.C-line2.A*line1.C)/(line1.A*line2.B-line2.A*line1.B)
            return  "Intersection point is ({},{})".format(x,y)   
        

        
l1=Line(1,3,-2)
l2=Line(-1,3,0)
print(l1)
print(l2)
print(l1.intersection(l2))
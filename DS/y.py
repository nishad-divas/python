class Point:
    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y

    def __str__(self):
       return '({},{})'.format(self.x_cod,self.y_cod)
    
    def eudance_distance(self,other):
        return ((self.x_cod-other.x_cod)**2+(self.y_cod-other.y_cod)**2)**0.5
    
    def distance_from_origin(self):
        return self.eudance_distance(Point(0,0))
    


class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C

    def line(self):
        if self.C<0:
            self.C=-self.C
            return '{}x+{}y-{}=0'.format(self.A,self.B,self.C)
        if self.C==0:
            return '{}x+{}y=0'.format(self.A,self.B)
        else:
            return '{}x+{}y+{}=0'.format(self.A,self.B,self.C)

    
p1=Point(1,2)
p2=Point(2,3)
print(p1.eudance_distance(p2))
print(p1.distance_from_origin())
l=Line(1,1,0)
print(l.line())


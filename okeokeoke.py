class Vector2D:
    
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y

    def __add__(self,other:Vector2D):
        return Vector2D(self.x+other.x,self.y+other.y)
    
    def __sub__(self,other:Vector2D):
        return Vector2D(self.x-other.x,self.y-other.y)
    
    def __mul__(self,scalar:float):
        return Vector2D(self.x*scalar,self.y*scalar)
    
    def __len__(self):
        return float(self.x**2+self.y**2)
    
    def __str__(self): 
        return f"{self.x};{self.y}"
    

class Money:

    def __init__(self,dollars:int,cents:int):
        self.dollars=dollars
        self.cents=cents
    
    def __add__(self,other: Money):
        d=self.dollars+other.dollars
        c=self.cents+other.cents
        while c!=99:
            if c>=100:
                d+=1
                c-=100
        return Money(d,c)
    
    def __sub__(self,other:Money):
        d=self.dollars-other.dollars
        c=self.cents-other.cents
        while c!=99:
            if c>=100:
                d-=1
                c-=100
        return Money(d,c)
    
    def __repr__(self):
        return f"dollars {self.dollars} and cents {self.cents}"
    
a=Money(6,8)
b=Money(8,8)

print(a+b)
print(a-b)
print(repr(a))


class Time:

    def __init__(self,hours,minutes,seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds

    def __add__(self, other: Time):

        h = self.h+other.h
        m = self.m+other.m
        s = self.s+other.s
        while s!=59:
            if(s>=60):
                m+=1
                s-=60
        while m!=59:    
            if(m>=60):
                h+=1
                m-=60
            
        return Time(h,m,s)
    
    def __len__(self):
        return self.s+self.m*60+self.h*3600
    
    def __repr__(self):
        return f" {self.hours},{self.minutes},{self.seconds}"
    
a=Time(6,8,9)
b=Money(8,8,8)

print(a+b)
print(len(a))
print(repr(a))


class Point:
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y

    def __add__(self,other:Point):
        return Point(other.x+self.x,self.y+other.y)
        
    def __sub__(self,other:Point):
        return Point(other.x-self.x,other.y-self.y)
    
    def __repr__(self):
        return f"{self.x},{self.y}"
    
a=Point(8,8)
b=Point(5,5)

print(a+b)
print(a-b)
print(repr(a))


class ColoredPoint(Point):

    def __init__(self,color:str):
        self.color=color

    def __add__(self,other: ColoredPoint):
        point: Point=super().__add__(other) 
        if self.color==other.color:
            a=self.color  
        else: 
            a='black'          
        return ColoredPoint(point.x, point.y,a)
        
    def __sub__(self,other: ColoredPoint):
        point: Point=super().__sub__(other)
        if self.color==other.color:
            a=self.color  
        else: 
            a='black'        
        return ColoredPoint(point.x, point.y,a)
        
    def __repr__(self):
        return f"{self.x},{self.y},{self.color}"
    
a=ColoredPoint(2,2,"ffff")
b=ColoredPoint(2,2,"ffff")

print(a+b)
print(a-b)
print(repr(a))


class Matrix:

    def __init__(self,a:int,b:int,c:int,d:int):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

    def __add__(self,other: Matrix):
        return Matrix(self.a+other.a,self.b+other.b,self.c+other.c,self.d+other.d)
    
    def __mul__(self,num: int):
        return Matrix(self.a*num,self.b*num,self.c*num,self.d*num)
    
    def __len__(self):
        return 4 
    
    def __repr__(self):
        return f"{self.a},{self.b},{self.c},{self.d}"
    
a=Matrix(1,2,3,4)
b=Matrix(1,2,3,4)

print(a+b)
print(a*b)
print(len(a))
print(repr(a))


class Temperature:

    def __init__(self,degrees):
        self.degrees=degrees

    def __add__(self,other: Temperature):
        return Temperature(other.degrees+self.degrees)
    
    def __sub__(self,other:Temperature):
        return Temperature(other.degrees-self.degrees)
    
    def __mul__(self,other:Temperature,factor:int):
        a=factor*(self.degrees+other.degrees)

    def __repr__(self):
        return f"{self.degrees}"
    
a=Temperature(88)
b=Temperature(88)

print(a+b)
print(a-b)
print(a*b)
print(repr(a))
  
    
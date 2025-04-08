class Vector2D:
    
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y

    #кринж
        


class Money:

    def __init__(self,dollars:int,cents:int):
        self.dollars=dollars
        self.cents=cents

    def add(self,second_money):#тут она еще не поняла ничего
        cents=self.cents//100  #копейки лишнее
        cents_2=self.second_money//100
        sum=self.dollars+cents+second_money.dollars+cents_2
        return sum
    
    def __add__(self,other):
        return self.add(other)
    
    def sub(self,second_money):
        cents=self.cents//100
        cents_2=self.second_money//100
        sub=(self.dollars+cents)-(second_money.dollars+cents_2)
        return sub
    
    def __sub__(self,other):
        return self.sub(other)
    
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

    def add(self,second_time):
        seconds=(self.seconds//60)+(second_time.seconds//60)
        minutes=(self.minutes//60+second_time.minutes)+(seconds//60)
        hours=self.hours+minutes+second_time.hours
        return hours
    
    def __add__(self,other):
        return self.add(other)
    
    def len(self,second_time):
        hours=(self.hours//60)+(second_time.hours//60)
        minutes=(self.minutes//60+second_time.minutes)+(hours//60)
        seconds=self.seconds+minutes+second_time.seconds
        return seconds
    
    def __repr__(self):
        return f" {self.hours} , {self.minutes} , {self.seconds}"
    
a=Time(6,8,9)
b=Money(8,8,8)

print(a+b)
print(a.len(b))
print(repr(a))

class Point:
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y

    def __add__(self,other):#тут она прозрела
        return other+self.x+self.y
        
    def __sub__(self,other):
        return other-self.x-self.y
    
    def __repr__(self):
        return f"{self.x},{self.y}"
    
a=Point(8,8)
b=Point(5,5)

print(a+b)
print(a-b)
print(repr(a))

class ColoredPoint:

    def __init__(self,x:int,y:int,color:str):
        self.x=x
        self.y=y
        self.color=color

    def __add__(self,other):
        if self.color==self.color:
            return other+self.x+self.y
        
        else:
            return f"blac {other+self.x+self.y}"
        
    def __sub__(self,other):
        if self.color==self.color:
            return other-self.x-self.y
        
        else:
            return f"blac {other-self.x-self.y}"
        
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

    def __add__(self,other_matrix):
        return other_matrix+self.a+self.b+self.c+self.d
    
    def __mul__(self,number):
        a=number*(self.a+self.b+self.c+self.d)
        return a
    
    def __repr__(self):
        return f"{self.a},{self.b},{self.c},{self.d}"
    
a=Matrix(1,2,3,4)
b=Matrix(1,2,3,4)

print(a+b)
print(a*b)
print(repr(a))

class Temperature:

    def __init__(self,degrees):
        self.degrees=degrees

    def __add__(self,other):
        return other+self.degrees
    
    def __sub__(self,other):
        return other-self.degrees
    
    def __mul__(self,factor):
        a=factor*self.degrees

    def __repr__(self):
        return f"{self.degrees}"
    
a=Temperature(88)
b=Temperature(88)

print(a+b)
print(a-b)
print(a*b)
print(repr(a))
  
    
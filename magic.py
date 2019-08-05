class MobilePhone():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f'Phone {self.name} {self.price}'
    def __add__(self, other):
        if isinstance(other, MobilePhone):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other
    def __gt__(self, other):
        return self.price > other.price
    def __eq__(self, other):
        return self.price == other.price
iphoneX = MobilePhone('iphoneX', 4000)
lg50 = MobilePhone('Lg50', 3500)
lg45 = MobilePhone('Lg45', 3500)
print(iphoneX + lg50)
print(iphoneX + 200 + 400)
print (iphoneX > lg50)
print (iphoneX == lg50)
print (lg45 == lg50)

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    def __str__(self):
        return f'Point x:{self.x} y:{self.y}'
    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y)

p1 = Point(3.4, 5)
p2 = Point(3.6, 9)
p3 = p1 + p2 # Point(7, 14)
print(p3)

# __eq__  x1==x2 y1 == y2
# _gt__ x1 > x2 y1 > y2
# __ne__ return not __eq__
class MobilePhone():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f'Phone {self.name} {self.price}'
    def __add__(self, other):
        if isinstance(other, MobilePhone):
            return self.price + other.price
        elif isinstance(other, int):
            return self.price + other
    def __gt__(self, other):
        return self.price > other.price
    def __eq__(self, other):
        return self.price == other.price
iphoneX = MobilePhone('iphoneX', 4000)
lg50 = MobilePhone('Lg50', 3500)
lg45 = MobilePhone('Lg45', 3500)
print(iphoneX + lg50)
print(iphoneX + 200 + 400)
print (iphoneX > lg50)
print (iphoneX == lg50)
print (lg45 == lg50)

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    def __str__(self):
        return f'Point x:{self.x} y:{self.y}'
    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y)

p1 = Point(3.4, 5)
p2 = Point(3.6, 9)
p3 = p1 + p2 # Point(7, 14)
print(p3)

# __eq__  x1==x2 y1 == y2
# _gt__ x1 > x2 y1 > y2
# __ne__ return not __eq__

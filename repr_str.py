
class Person():
    def __init__(self,name,age,
                 height):
        self.name = name
        self.age = age
        self.height = height
    def __repr__(self):
        return \
            f'Person("{self.name}",{self.age},{self.height})'
    #def __str__(self):
#        return \
#            f'Person name:{self.name}'\
#            f' age:{self.age}'\
#            f' height:{self.height}'
mickey = Person('Mickey', 3, 1.2)
goofy = Person('goofy', 5, 2)

print(mickey)
print(goofy)

# class Point
#  init (x,y)  default x = 0 y = 0
#  repr - python command for creation
#  str - print point x and y

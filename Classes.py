
class Computer():
    def __init__(self,
                 color = 'black',
                 speed = 0):
        print("new computer...")
        self.color = color
        self.speed = speed

lenovo = Computer('black', 2.2)
imac = Computer()
print(f'lenovo = {lenovo.speed}')
print(f'imac = {imac.speed}')
del lenovo


# create Person clas
# __init__(self, name, age, height)
# create 2 persons
# set default values:
#  name 'incognito', age 0, height 0

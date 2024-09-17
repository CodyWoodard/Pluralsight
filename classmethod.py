class MyClass:
    def __init__(self, x):
        self._x = x
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        if value < 5:
            self._x = value

c = MyClass(3)
c.x = 2
print(c.x)
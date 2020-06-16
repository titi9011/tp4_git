class maclasse():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return str(self.y)

x = maclasse(4, 5)
print(x)
class mere:
    def __init__(self):
        self.x = 0
        self.y = 10
    def sprint(self):
        return 'p'


class fille(mere):
    def __init__(self):
        super().__init__()
        self.y = 9

print(fille().x)
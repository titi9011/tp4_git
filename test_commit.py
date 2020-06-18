import damier
import partie

print(dir(damier))
#damier.piece_peut_se_deplacer(Position(5,2))
# partie.piece_peut_se_deplacer(Position(5, 2))

class maclasse():
    def __init__(self, x):
        self.x = x
    
    def __repr__(self):
        return '6'

x = maclasse(4)
print(x)
from position import Position
from damier import Damier
from piece import Piece
from pickle import dump, load
from engine import print_damier

x = {Position(7, 0): Piece("blanc", "pion"),
Position(7, 2): Piece("blanc", "pion"),
Position(7, 4): Piece("blanc", "pion"),
Position(7, 6): Piece("blanc", "pion"),
Position(6, 1): Piece("blanc", "pion"),
Position(6, 3): Piece("blanc", "pion"),
Position(6, 5): Piece("blanc", "pion"),
Position(6, 7): Piece("blanc", "pion"),
Position(5, 0): Piece("blanc", "pion"),
Position(5, 2): Piece("blanc", "pion"),
Position(4, 3): Piece("blanc", "pion"),
Position(4, 5): Piece("blanc", "pion"),
Position(2, 1): Piece("noir", "pion"),
Position(3, 2): Piece("noir", "pion"),
Position(2, 5): Piece("noir", "pion"),
Position(2, 7): Piece("noir", "pion"),
Position(1, 0): Piece("noir", "pion"),
Position(1, 2): Piece("noir", "pion"),
Position(1, 4): Piece("noir", "pion"),
Position(1, 6): Piece("noir", "pion"),
Position(0, 1): Piece("noir", "pion"),
Position(0, 3): Piece("noir", "pion"),
Position(0, 5): Piece("noir", "pion"),
Position(0, 7): Piece("noir", "pion")}

x2 = {Position(7, 0): Piece("blanc", "pion"),
Position(7, 2): Piece("blanc", "pion"),
Position(7, 4): Piece("blanc", "pion"),
Position(7, 6): Piece("blanc", "pion"),
Position(6, 1): Piece("blanc", "pion"),
Position(6, 3): Piece("blanc", "pion"),
Position(6, 5): Piece("blanc", "pion"),
Position(6, 7): Piece("blanc", "pion"),
Position(5, 0): Piece("blanc", "pion"),
Position(5, 2): Piece("blanc", "pion"),
Position(4, 5): Piece("blanc", "pion"),
Position(2, 1): Piece("noir", "pion"),
Position(5, 4): Piece("noir", "pion"),
Position(2, 5): Piece("noir", "pion"),
Position(2, 7): Piece("noir", "pion"),
Position(1, 0): Piece("noir", "pion"),
Position(1, 2): Piece("noir", "pion"),
Position(1, 4): Piece("noir", "pion"),
Position(1, 6): Piece("noir", "pion"),
Position(0, 1): Piece("noir", "pion"),
Position(0, 3): Piece("noir", "pion"),
Position(0, 5): Piece("noir", "pion"),
Position(0, 7): Piece("noir", "pion")}

print_damier(x)
print_damier(x2)
print(list(x2.keys() - x.keys())[0])

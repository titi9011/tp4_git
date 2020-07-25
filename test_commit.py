from position import Position
from piece import Piece
from pickle import dump, load

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
Position(5, 4): Piece("blanc", "pion"),
Position(5, 6): Piece("blanc", "pion"),
Position(2, 1): Piece("noir", "pion"),
Position(2, 3): Piece("noir", "pion"),
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

fichier = open('partie', 'wb')
dump(['noir', x], fichier)
fichier.close()

fichier = open('partie', 'rb')
dic = load(fichier)
print(dic[0])
print(dic[1])
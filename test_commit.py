from position import Position
from piece import Piece

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

def str_piece(piece):
    if str(piece) == 'x':
        return 'Piece("noir", "pion")'
    if str(piece) == 'X':
        return 'Piece("noir", "dame")'
    if str(piece) == 'o':
        return 'Piece("blanc", "pion")'
    if str(piece) == 'O':
        return 'Piece("blanc", "blanc")'

def str_position(position):
    return 'Position' + str(position)

def str_dic(dic):
    new_dic = {}
    for position, piece in dic.items():
        new_dic[str_position(position)] = str_piece(piece)
    return str(new_dic)

def class_str_dic(dic):
    return dic.replace("'", "")

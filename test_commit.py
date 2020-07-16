from random import randrange
from piece import Piece

x = Piece('noir', 'pion')
dic = {'position': x}

dic['position'].promouvoir()
dic['position'].promouvoir()

print(dic['position'])
from random import randrange
from piece import Piece

x = Piece('noir', 'pion')
print(x)
x.promouvoir()
print(x)
print(type(x))
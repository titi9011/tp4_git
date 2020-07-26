from un_joueur import Un_joueur
from interface_dames import FenetrePartie
from tkinter import *

fenetre = Tk()

button = Button(fenetre, text='Un joueur', command=Un_joueur())
button.pack()
fenetre.mainloop()
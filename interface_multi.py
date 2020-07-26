from un_joueur import Un_joueur
from interface_dames import FenetrePartie
from tkinter import *


fenetre = Tk()
button = Button(fenetre, text='Un joueur', command=lambda:[fenetre.withdraw(), Un_joueur()])
button.pack()
button2 = Button(fenetre, text='Deux joueurs', command=lambda:[fenetre.withdraw(), FenetrePartie()])
button2.pack()

fenetre.mainloop()
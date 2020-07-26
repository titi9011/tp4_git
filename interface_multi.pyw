from un_joueur import Un_joueur
from interface_dames import FenetrePartie
from tkinter import *
import tkinter.font as font

fenetre = Tk()
fenetre.geometry("425x200")
fenetre['background'] = 'mint cream'
fenetre.title("Jouer contre l'ordinateur ou à deux joueurs")
texte_0_A = Label(fenetre)
texte_0_B = Label(fenetre)
texte_0_C = Label(fenetre)
texte_0_A['background'] = 'mint cream'
texte_0_B['background'] = 'mint cream'
texte_0_C['background'] = 'mint cream'
texte_0_A['foreground'] = 'midnight blue'
texte_0_B['foreground'] = 'midnight blue'
texte_0_A['text'] = 'Choisissez "un joueur" si vous désirez jouer contre ' + "l'ordinateur!"
texte_0_B['text'] = " Vous pouvez jouer sans l'aide de l'ordinateur en choisissant " + '"deux joueurs".'
texte_0_C['text'] = " "
texte_0_A['font'] = font.Font(size=9)  #, weight='bold')
texte_0_B['font'] = font.Font(size=9)
texte_0_A.grid(sticky=N)
texte_0_B.grid(sticky=N)
texte_0_C.grid(sticky=N)
button_1 = Button(fenetre, text='Un joueur', command=lambda:[fenetre.withdraw(), Un_joueur()], height = 3, width = 30)
button_1['background'] = '#C9E2FC'
button_1['foreground'] = 'Blue3'
button_1['font'] = font.Font(size=9, weight='bold')
button_1.grid(row=3, pady=5)
texte_0_C.grid(sticky=N)
button_2 = Button(fenetre, text='Deux joueurs', command=lambda:[fenetre.withdraw(), FenetrePartie()], height = 3, width = 30)
button_2['background'] = '#C9E2FC'
button_2['foreground'] = 'Blue3'
button_2['font'] = font.Font(size=9, weight='bold')
button_2.grid()

fenetre.mainloop()
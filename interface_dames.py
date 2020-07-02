# Auteurs: À compléter

from tkinter import Tk, Label, NSEW
from canvas_damier import CanvasDamier
from partie import Partie
from position import Position
from damier import Damier

class FenetrePartie(Tk):
    """Interface graphique de la partie de dames.

    Attributes:
        partie (Partie): Le gestionnaire de la partie de dame
        canvas_damier (CanvasDamier): Le «widget» gérant l'affichage du damier à l'écran
        messages (Label): Un «widget» affichant des messages textes à l'utilisateur du programme

        TODO: AJOUTER VOS PROPRES ATTRIBUTS ICI!
    """

    def __init__(self):
        """Constructeur de la classe FenetrePartie. On initialise une partie en utilisant la classe Partie du TP3 et
        on dispose les «widgets» dans la fenêtre.
        """

        # Appel du constructeur de la classe de base (Tk)
        super().__init__()

        # La partie
        self.partie = Partie()
        self.damier = Damier()

        # Création du canvas damier.
        self.canvas_damier = CanvasDamier(self, self.partie.damier, 60)
        self.canvas_damier.grid(sticky=NSEW)
        self.canvas_damier.bind('<Button-1>', self.selectionner)

        # Ajout d'une étiquette d'information.
        self.messages = Label(self)
        self.messages.grid()

        # Nom de la fenêtre («title» est une méthode de la classe de base «Tk»)
        self.titre_joueur = self.partie.couleur_joueur_courant
        # self.titre_joueur["foreground"] = "red"
        # self.title['foreground'] = 'red'
        self.title("Jeu de dames. Le joueur " + self.titre_joueur + " joue!")


        # Truc pour le redimensionnement automatique des éléments de la fenêtre.
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def selectionner(self, event):
        """Méthode qui gère le clic de souris sur le damier.

        Args:
            event (tkinter.Event): Objet décrivant l'évènement qui a causé l'appel de la méthode.

        """

        # On trouve le numéro de ligne/colonne en divisant les positions en y/x par le nombre de pixels par case.
        ligne = event.y // self.canvas_damier.n_pixels_par_case
        # print("Source : ", ligne)  # temp
        colonne = event.x // self.canvas_damier.n_pixels_par_case
        position = Position(ligne, colonne)
        print("position", position)
# test1 temp
        if self.partie.position_source_valide(position)[0]:
            # print("Houba temp1")
            if self.partie.doit_prendre == True:
                if self.position_source_forcee is None:
                    pass  # verif_source_cible = False
                else:
                    if self.position_source_forcee == position:
                        print("Vous devez prendre. La pièce en position {} a été sélectionnée.".format(
                            self.position_source_forcee))
                        # self.damier.piece_peut_faire_une_prise(self.position_source_forcee)
                        # verif_source_cible = False
                    else:
                        print("Vous devez prendre. La pièce choisie ne peut pas être sélectionnée")

            elif self.damier.piece_peut_se_deplacer(position):
                pass  # verif_source_cible = False
            else:
                print("La pièce que vous avez sélectionnée ne peut pas se déplacer. Veuillez faire un autre choix.")
        else:
            print(self.partie.position_source_valide(position)[1])
# _________ temp
# test2 temp



        ligne = event.y // self.canvas_damier.n_pixels_par_case
        # print("Cible", ligne)  # temp
        colonne = event.x // self.canvas_damier.n_pixels_par_case
        self.position_cible = Position(ligne, colonne)

# ________ temp


        # On récupère l'information sur la pièce à l'endroit choisi.
        piece = self.partie.damier.recuperer_piece_a_position(position)

        if piece is None:
            self.messages['foreground'] = 'red'
            self.messages['text'] = 'Erreur: Aucune pièce à cet endroit.'
        else:
            self.messages['foreground'] = 'black'
            self.messages['text'] = 'Pièce sélectionnée à la position {}.'.format( position)

        # TODO: À continuer....


if __name__ == '__main__':
    # Point d'entrée principal du TP4.
    fenetre = FenetrePartie()
    fenetre.mainloop()

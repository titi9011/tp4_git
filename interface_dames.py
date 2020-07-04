# Auteurs: À compléter

from tkinter import Tk, Label, NSEW, dnd
# import tkinter.dnd
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
        print("init partie")  # temp

        # Création du canvas damier.
        self.canvas_damier = CanvasDamier(self, self.partie.damier, 60)
        self.canvas_damier.grid(sticky=NSEW)
        self.canvas_damier.bind('<Button-1>', self.selectionner)

        # Ajout d'une étiquette d'information.
        self.messages1 = Label(self)
        self.messages1.grid()

        # Nom de la fenêtre («title» est une méthode de la classe de base «Tk»)
        self.titre_joueur = self.partie.couleur_joueur_courant
        # self.titre_joueur["foreground"] = "red"
        # self.title['foreground'] = 'red'
        # self.title("Jeu de dames. Le joueur " + self.titre_joueur + " joue!")
        self.messages = Label(self)
        self.messages.grid_anchor("n")
        self.messages.anchor("n")
        self.messages['text'] = "Jeu de dames. Le joueur " + self.titre_joueur + " joue!"
        # self.titre_joueur

        # Truc pour le redimensionnement automatique des éléments de la fenêtre.
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def selectionner(self, event):
        """Méthode qui gère le clic de souris sur le damier.

        Args:
            event (tkinter.Event): Objet décrivant l'évènement qui a causé l'appel de la méthode.

        """

        # On trouve le numéro de ligne/colonne en divisant les positions en y/x par le nombre de pixels par case.
        # ligne = event.y // self.canvas_damier.n_pixels_par_case
        # colonne = event.x // self.canvas_damier.n_pixels_par_case
        # if flg == 0:
        # position = Position(ligne, colonne)
        #    flg = 1
        # test temp
        #drag = (event.x, event.y)
        self.bind('<Button-1>')
        self.bind('B1-Motion')
        # print("position 76", position)  # temp
        # print(self.selection_get('messages1'))
        # test = drg()
# test1 temp
        try:
            print("flg 81 ", self.flg)  # temp
            if self.flg == 0:
                print("flg 83")  # temp
                ligne = event.y // self.canvas_damier.n_pixels_par_case
                colonne = event.x // self.canvas_damier.n_pixels_par_case
                position_cible = Position(ligne, colonne)
                print("Cible", position_cible)  # temp

                if self.position_cible_valide(position_cible)[0]:
                    print("90")  # temp
                    if self.doit_prendre == True:
                        if self.damier.piece_peut_sauter_vers(position_source_selectionnee, position_cible):
                            verif_source_cible = False
                        else:
                            print(
                                "La pièce choisie doit prendre une pièce adverse. La cible choisie doit être modifiée.")
                    elif self.damier.piece_peut_se_deplacer_vers(position_source_selectionnee, position_cible):
                        verif_source_cible = False
                    else:
                        print("La pièce choisie ne peut pas être déplacée vers cette case.\n")
                else:
                    print(self.position_cible_valide(position_cible)[1])

                del self.flg


        except:
            print("flg 91")  # temp
            ligne = event.y // self.canvas_damier.n_pixels_par_case
            colonne = event.x // self.canvas_damier.n_pixels_par_case
            position = Position(ligne, colonne)
            if self.partie.position_source_valide(position)[0]:
                self.messages1['foreground'] = 'black'
                self.messages1['text'] = 'Pièce sélectionnée à la position {}.'.format( position)
                ligne = event.y // self.canvas_damier.n_pixels_par_case
                colonne = event.x // self.canvas_damier.n_pixels_par_case
                position = Position(ligne, colonne)
                # test_f = dnd.on_release()

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
                            self.messages1['foreground'] = 'red'
                            self.messages1['text'] = "Vous devez prendre. La pièce choisie ne peut pas être sélectionnée."

                elif self.damier.piece_peut_se_deplacer(position):
                    pass  # verif_source_cible = False
                else:
                    self.messages1['foreground'] = 'red'
                    self.messages1['text'] = "La pièce que vous avez sélectionnée ne peut pas se déplacer. Veuillez faire un autre choix."
            else:
                self.messages1['foreground'] = 'red'
                self.messages1['text'] = self.partie.position_source_valide(position)[1]
            # self.canvas_damier.actualiser()
            print("Source 123 : ", position)
            self.flg = 0

# _________ temp
# test2 temp

        # self.canvas_damier.actualiser()
        # self.messages['foreground'] = 'black'
        # self.messages['text'] = "Sélection : " + str(position)



# ________ temp


        # print("Cible : ", self.position_cible)

        # On récupère l'information sur la pièce à l'endroit choisi.
            # piece = self.partie.damier.recuperer_piece_a_position(position)

        #if piece is None:
         #   self.messages['foreground'] = 'red'
          #  self.messages['text'] = 'Erreur: Aucune pièce à cet endroit.'
        #else:
         #   self.messages['foreground'] = 'black'
          #  self.messages['text'] = 'Pièce sélectionnée à la position {}.'.format( position)

        # TODO: À continuer....
    def enregistrer_position_source(self, position):

        return position

    def enregistrer_position_cible(self, position):

        return position

if __name__ == '__main__':
    # Point d'entrée principal du TP4.
    fenetre = FenetrePartie()
    fenetre.mainloop()

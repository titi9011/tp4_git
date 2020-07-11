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
        # self.damier = Damier()

        # Création du canvas damier.
        self.canvas_damier = CanvasDamier(self, self.partie.damier, 60)
        self.canvas_damier.grid(sticky=NSEW)
        self.canvas_damier.bind('<Button-1>', self.selectionner)
        # self.canvas_damier.bind('<B1-Button_release>', self.enregistrer_position_cible)

        # Ajout d'une étiquette d'information.
        self.messages1 = Label(self)
        self.messages1.grid()
        self.messages1['foreground'] = 'blue'
        self.messages1['text'] = 'Quelle pièce désirez-vous déplacer?'
        self.colonne_damier_reel = "abcdefgh"

        # Initialisation des attributs
        self.doit_prendre = False
        self.position_source_selectionnee = None
        self.position_source_forcee = None

        # Nom de la fenêtre («title» est une méthode de la classe de base «Tk»)
        self.titre_joueur = self.partie.couleur_joueur_courant + " joue!"
        self.title("Jeu de dames. Le joueur " + self.titre_joueur)

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



# test1 temp
        try:  # Permet d'affecter le premier clic à la position source et le second à la cible.
            if self.flg == 0:  # Génère l'erreur qui affecte le premier clic.

                ligne = event.y // self.canvas_damier.n_pixels_par_case
                colonne = event.x // self.canvas_damier.n_pixels_par_case
                self.position_cible = Position(ligne, colonne)
                print("Cible-i-85", self.position_cible)  # temp
                try:  # Assure que la position cible soit valide.
                    ligne = event.y // self.canvas_damier.n_pixels_par_case
                    colonne = event.x // self.canvas_damier.n_pixels_par_case
                    self.position_cible = Position(ligne, colonne)
                    print("i-90", self.doit_prendre)  # temp




                    # if self.partie.damier.piece_de_couleur_peut_faire_une_prise(self.partie.couleur_joueur_courant):
                     #   self.doit_prendre = True
                      #  print(97)

                 #       if self.position_source_forcee is None:
                  #          print(" Le joueur doit prendre une pièce.")
                   #     else:
                    #        print(" La pièce en position {} doit faire une autre prise.".format(
                     #           self.position_source_forcee))

                    print("i-105", type(self.position.colonne))
                    print("i-106", str(self.position_cible.ligne))
                    print("i-107",  self.partie.damier.piece_peut_sauter_vers(self.position, self.position_cible))



                    if self.partie.position_cible_valide(self.position_cible)[0]:  # À enlever
                        self.messages1['foreground'] = 'black'
                        position_source_damier_reel =self.colonne_damier_reel[self.position.colonne] +  str(8 - self.position.ligne)
                        position_cible_damier_reel = self.colonne_damier_reel[self.position_cible.colonne] + str(8 - self.position_cible.ligne)
                        self.messages1['text'] = 'Pièce à la position {} déplacée à {}.'.format(position_source_damier_reel, position_cible_damier_reel)

                        if self.doit_prendre == True:
                            if self.partie.damier.piece_peut_sauter_vers(self.position, self.position_cible):
                                print("i-116")  # verif_cible = False
                                pass
                            else:
                                 self.messages1['foreground'] = 'red'
                                 self.messages1['text'] = "La pièce choisie doit prendre une pièce adverse. La cible choisie doit être modifiée."
                                 1 / 0  # Génère une erreur pour modifier la position cible
                        elif self.partie.damier.piece_peut_se_deplacer_vers(self.position, self.position_cible):
                            print("i-123 ", self.partie.damier.piece_peut_se_deplacer_vers(self.position, self.position_cible))  # temp
                            # pass
                        else:
                            self.messages1['foreground'] = 'red'
                            self.messages1['text'] = "La pièce choisie ne peut pas être déplacée vers cette case."
                            1 / 0
                    # else:
                    #    self.messages1['foreground'] = 'red'
                    #    self.messages1['text'] = self.partie.position_cible_valide(self.position_cible)[1]
                    #    1 / 0
                except: # Assure la validité du second clic affecté à la position cible.
                    1 / 0
                else:
                    #ligne = event.y // self.canvas_damier.n_pixels_par_case
                    #colonne = event.x // self.canvas_damier.n_pixels_par_case
                    #self.position_cible = Position(ligne, colonne)
                    pass

                retour_apres_deplacement = self.partie.damier.deplacer(self.position, self.position_cible)  # ok, prise ou erreur

                # del self.flg  # Libère le drapeau pour le tour suivant



                    # print("i-151 ", self.partie.couleur_joueur_courant)  # temp
                if retour_apres_deplacement == "ok":
                     pass
                elif retour_apres_deplacement == "prise":
                    if self.partie.damier.piece_peut_faire_une_prise(self.position_cible):
                        # if self.partie.damier.piece_de_couleur_peut_faire_une_prise(self.couleur_joueur_courant):
                        # Vérifier si peut prendre encore
                        print("i-158 peut prendre encore", self.partie.damier.piece_peut_faire_une_prise(self.position_cible))
                        self.position_source_forcee = self.position_cible
                        self.doit_prendre = True

                    else:
                        self.doit_prendre = False
                        self.position_source_selectionnee = None
                        self.position_source_forcee = None
                else:
                    self.messages1['foreground'] = 'red'
                    self.messages1['text'] = "Il y a erreur dans le code!"
                print("i-166 ", retour_apres_deplacement)  # temp
                if self.doit_prendre == False:
                    if self.partie.couleur_joueur_courant == "blanc":
                        self.partie.couleur_joueur_courant = "noir"
                    else:
                        self.partie.couleur_joueur_courant = "blanc"
                    self.titre_joueur = self.partie.couleur_joueur_courant + " joue!"
                    self.title("Jeu de dames. Le joueur " + self.titre_joueur)
                else:
                    self.titre_joueur = self.partie.couleur_joueur_courant + " joue et doit faire une prise!"
                    self.title("Jeu de dames. Le joueur " + self.titre_joueur)

                del self.flg  # Libère le drapeau pour le tour suivant
                # retour_apres_deplacement = self.damier.deplacer(self.position,self.position_cible)  # ok, prise ou erreur
                # print("i-159 ", self.damier.deplacer(self.position,self.position_cible))  # temp
                # self.damier = Damier()  # temp
                # self.canvas_damier.actualiser()

        except:
            if self.partie.damier.piece_de_couleur_peut_faire_une_prise(self.partie.couleur_joueur_courant):
                self.doit_prendre = True
                print("i-185 == 97")

                if self.position_source_forcee is None:
                    self.titre_joueur = self.partie.couleur_joueur_courant + " joue et doit faire une prise!"
                    self.title("Jeu de dames. Le joueur " + self.titre_joueur)
                    print(" Le joueur doit prendre une pièce.")
                else:
                    print(" La pièce en position {} doit faire une autre prise.".format(
                        self.position_source_forcee))
            print("flg i-192")  # temp
            ligne = event.y // self.canvas_damier.n_pixels_par_case
            colonne = event.x // self.canvas_damier.n_pixels_par_case
            self.position = Position(ligne, colonne)
            print("i-196 ", self.position)
            print("i-197 ", self.partie.position_source_valide(self.position))
            if self.partie.position_source_valide(self.position)[0]:
                self.messages1['foreground'] = 'black'
                position_source_damier_reel = self.colonne_damier_reel[self.position.colonne] + str(8 - self.position.ligne)
                self.messages1['text'] = 'Vous devez prendre. La pièce en position '\
                              + position_source_damier_reel + ' doit être sélectionnée.'
                # ligne = event.y // self.canvas_damier.n_pixels_par_case
                # colonne = event.x // self.canvas_damier.n_pixels_par_case
                # position = Position(ligne, colonne)
                # test_f = dnd.on_release()
                print("i-205", self.doit_prendre)
                if self.doit_prendre == True:
                    if self.position_source_forcee is None:
                       self.flg = 0
                    else:
                        if self.position_source_forcee == self.position:
                            self.messages1['foreground'] = 'red'
                            self.messages1['text'] = "Vous devez prendre. La pièce en position ", position_source_damier_reel, " a été sélectionnée."
                            self.flg = 0
                                # self.damier.piece_peut_faire_une_prise(self.position_source_forcee)
                                # verif_source_cible = False
                        else:
                            self.messages1['foreground'] = 'red'
                            self.messages1['text'] = "Vous devez prendre. La pièce choisie ne peut pas être sélectionnée."

                elif self.partie.damier.piece_peut_se_deplacer(self.position):
                    self.flg = 0
                else:
                    self.messages1['foreground'] = 'red'
                    self.messages1['text'] = "La pièce que vous avez sélectionnée ne peut pas se déplacer. Veuillez " \
                                             "faire un autre choix. "
            else:
                self.messages1['foreground'] = 'red'
                self.messages1['text'] = self.partie.position_source_valide(self.position)[1]
        self.canvas_damier.actualiser()

        # Fin de partie
        if self.partie.damier.piece_de_couleur_peut_se_deplacer(self.partie.couleur_joueur_courant) or \
                self.partie.damier.piece_de_couleur_peut_faire_une_prise(self.partie.couleur_joueur_courant):
            pass
        else:
            self.title("Jeu de dames. La partie est terminée!")
            self.messages1['foreground'] = 'orange'
            if self.partie.couleur_joueur_courant == "blanc":
                self.partie.couleur_joueur_courant = "noir"
            else:
                self.partie.couleur_joueur_courant = "blanc"
            self.messages1['text'] = "Le joueur " + self.partie.couleur_joueur_courant + " a gagné!"

# _________ temp
# test2 temp




#        if self.doit_prendre == False:
 #           if self.couleur_joueur_courant == "blanc":
  #              self.couleur_joueur_courant = "noir"
   #         else:
    #            self.couleur_joueur_courant = "blanc"
            # self.canvas_damier.actualiser()
            # self.messages['foreground'] = 'black'
            # self.messages['text'] = "Sélection : " + str(position)



# ________ temp


        # print("Cible : ", position_cible)

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

    def enregistrer_position_cible(self):
        print("test-release i-241")
        return position

if __name__ == '__main__':
    # Point d'entrée principal du TP4.
    fenetre = FenetrePartie()
    fenetre.mainloop()
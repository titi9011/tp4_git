# Auteurs: À compléter

from tkinter import *  # Tk, Label, NSEW, dnd
from canvas_damier import CanvasDamier
from partie import Partie
from position import Position
# from damier import Damier

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

        # Ajout des boutons : A permettant d'obtenir l'aide et B de quitter et d'enregistrer.
        self.bouton1_A = Button(self, text = 'Aide', command = self.aide)
        self.bouton1_B = Button(self, text = 'Quitter', command = self.quit)
        self.bouton1_A.grid()
        self.bouton1_B.grid()

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
        """Méthode qui gère le clic de souris sur le damier. La méthode appelle les méthodes vérifiant la validité
        des sélections source et cible.
        Tant qu'une cible valide n'est pas sélectionnée, la position source peut être modifiée.

        Args:
            event (tkinter.Event): Objet décrivant l'évènement qui a causé l'appel de la méthode.

        """

        try:  # Permet d'affecter le premier clic à la position source et le second à la cible.
            if self.flg == 0:  # Génère l'erreur qui affecte le premier clic.
                ligne = event.y // self.canvas_damier.n_pixels_par_case
                colonne = event.x // self.canvas_damier.n_pixels_par_case  # On trouve le numéro de ligne/colonne en
                    # divisant les positions en y/x par le nombre de pixels par case.
                self.position_cible = Position(ligne, colonne)

                self.messages1['foreground'] = 'black'
                position_source_damier_reel =self.colonne_damier_reel[self.position.colonne]\
                                                 + str(8 - self.position.ligne)
                position_cible_damier_reel = self.colonne_damier_reel[self.position_cible.colonne]\
                                                 + str(8 - self.position_cible.ligne)
                self.messages1['text'] = 'Pièce à la position {} déplacée à {}.'\
                        .format(position_source_damier_reel, position_cible_damier_reel)

                if not self.valider_et_enregistrer_position_cible()[0]:
 #               if self.partie.position_cible_valide(self.position_cible)[0]:  # Maintenant inutile. À enlever
  #                  if self.doit_prendre == True:
   #                     if self.partie.damier.piece_peut_sauter_vers(self.position, self.position_cible):
    #                        print("i-116")  # verif_cible = False
     #                       pass
      #                  else:
       #                     self.messages1['foreground'] = 'red'
        #                    self.messages1['text'] = "La pièce choisie doit prendre une pièce adverse. La cible " \
         #                                            "choisie doit être modifiée. "
          #                  raise ValueError  # Génère une erreur pour modifier la position cible
           #         elif self.partie.damier.piece_peut_se_deplacer_vers(self.position, self.position_cible):
            #            print("i-123 ", self.partie.damier.piece_peut_se_deplacer_vers(self.position, self.position_cible))  # temp
             #           # pass
              #      else:
                    self.messages1['foreground'] = 'red'
                    self.messages1['text'] = self.valider_et_enregistrer_position_cible()[1]
                    raise ValueError
                    # else:
                    #    self.messages1['foreground'] = 'red'
                    #    self.messages1['text'] = self.partie.position_cible_valide(self.position_cible)[1]
                    #    1 / 0
 #               except: # Assure la validité du second clic affecté à la position cible.
  #                  print("i-134 - except")
   #                 raise ValueError  # 1/ 0
    #            else:
                    #ligne = event.y // self.canvas_damier.n_pixels_par_case
                    #colonne = event.x // self.canvas_damier.n_pixels_par_case
                    #self.position_cible = Position(ligne, colonne)
     #               pass

                retour_apres_deplacement = self.partie.damier.deplacer(self.position, self.position_cible)
                    # ok, prise ou erreur

                if retour_apres_deplacement == "ok":
                     pass
                elif retour_apres_deplacement == "prise":
                    if self.partie.damier.piece_peut_faire_une_prise(self.position_cible):

                        print("i-158 peut prendre encore", self.partie.damier.piece_peut_faire_une_prise(self.position_cible))  # temp
                        self.position_source_forcee = self.position_cible
                        self.doit_prendre = True

                    else:
                        self.doit_prendre = False
                        self.position_source_selectionnee = None
                        self.position_source_forcee = None
                else:
                    self.messages1['foreground'] = 'red'
                    self.messages1['text'] = "Il y a erreur dans le code!"

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

                # self.canvas_damier.actualiser()

        except:
            ligne = event.y // self.canvas_damier.n_pixels_par_case
            colonne = event.x // self.canvas_damier.n_pixels_par_case
            self.position = Position(ligne, colonne)
            position_source_damier_reel = self.colonne_damier_reel[self.position.colonne] + str(8 - self.position.ligne)
            if self.valider_prise_obligee()[0]:
                self.title("Jeu de dames. Le joueur " + self.valider_prise_obligee()[1])
                if self.partie.damier.piece_peut_faire_une_prise(self.position):
                    self.messages1['foreground'] = 'black'
                    self.messages1['text'] = 'La pièce sélectionnée en position ' \
                                                 + position_source_damier_reel + ' peut faire une prise.'

                else:
                    self.messages1['foreground'] = 'red'
                    self.messages1['text'] = 'Sélectionnez une pièce qui peut faire une prise.'

            else:
                self.titre_joueur = self.partie.couleur_joueur_courant + " joue!"
                self.title("Jeu de dames. Le joueur " + self.titre_joueur)

            if self.partie.position_source_valide(self.position)[0]:
                if self.valider_et_enregistrer_position_source()[0]:
                    self.messages1['foreground'] = 'black'
                    self.messages1['text'] = self.valider_et_enregistrer_position_source()[1]
                    self.flg = 0  # Valide la position source et autorise la sélection de la cible
                else:
                    self.messages1['foreground'] = 'red'
                    self.messages1['text'] = self.valider_et_enregistrer_position_source()[1]


#                if self.doit_prendre == True:
 #                   if self.position_source_forcee is None:  # C'est une première prise
  #                      self.flg = 0
   #                 else:
    #                    if self.position_source_forcee == self.position:  # Indique une prise successive
     #                       self.messages1['foreground'] = 'red'
      #                      self.messages1['text'] = "Vous devez prendre. La pièce en position " \
       #                                              + position_source_damier_reel + " a été sélectionnée."
        #                    self.flg = 0
         #                   # self.damier.piece_peut_faire_une_prise(self.position_source_forcee)
          #                  # verif_source_cible = False
           #             else:
            #                self.messages1['foreground'] = 'red'
             #               self.messages1[
              #                  'text'] = "Vous devez prendre. La pièce choisie ne peut pas être sélectionnée."

#                else:
 #                   self.messages1['foreground'] = 'black'
  #                  #position_source_damier_reel = self.colonne_damier_reel[self.position.colonne] + str(8 - self.position.ligne)
   #                 self.messages1['text'] = 'La pièce en position ' + position_source_damier_reel \
    #                                    + ' a été sélectionnée. Cliquez sur la cible désirée. '

#                    print("i-205", self.doit_prendre)  # temp
#
 #                   if self.partie.damier.piece_peut_se_deplacer(self.position):
  #                      self.flg = 0
   #                 else:
    #                    self.messages1['foreground'] = 'red'
     #                   self.messages1['text'] = "La pièce que vous avez sélectionnée ne peut pas se déplacer. Veuillez " \
      #                                       "faire un autre choix. "
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


    def valider_prise_obligee(self):
        """
        Détermine si le joueur actif doit ou non faire une prise. Rend la prise obligatoire dans le choix
        de la position source.
        return:
                [0] : True ou False
                [1] : Message à afficher si le joueur doit faire une prise.
        """
        if self.partie.damier.piece_de_couleur_peut_faire_une_prise(self.partie.couleur_joueur_courant):
            self.doit_prendre = True
            if self.position_source_forcee is None:  # C'est une première prise
                self.titre_joueur = self.partie.couleur_joueur_courant + " joue et doit faire une prise!"

            else:  # Indique une prise successive
                position_source_damier_reel = self.colonne_damier_reel[self.position_source_forcee.colonne] + str(
                    8 - self.position_source_forcee.ligne)
                self.titre_joueur = self.partie.couleur_joueur_courant + " joue. La pièce en position "\
                                    + position_source_damier_reel + " doit faire une prise!"
            return [True, self.titre_joueur]

        else:
            return [False, ""]

    def valider_et_enregistrer_position_source(self):
        """
        S'assure que la position source doit faire une prise, si c'est le cas, sinon que la pièce choisie est de la
        couleur du joueur et qu'elle peut se déplacer.

        return:
                [0] : True ou False
                [1] : Message à afficher si la source n'est pas valide.
        """
        position_source_damier_reel = self.colonne_damier_reel[self.position.colonne] + str(8 - self.position.ligne)
        if self.doit_prendre == True:
            if self.position_source_forcee is None:
                texte_messages1 = "Vous devez prendre. Assurez-vous que la pièce sélectionnée, en position " \
                                  + position_source_damier_reel + " peut prendre."
                return [True, texte_messages1]
            else:
                if self.position_source_forcee == self.position:
                    self.messages1['foreground'] = 'red'
                    texte_messages1 = "Vous devez prendre à nouveau. La pièce en position "\
                                      + position_source_damier_reel + " a été sélectionnée."
                    return [True, texte_messages1]
                else:
                    texte_messages1 = "Vous devez prendre à nouveau. La pièce choisie ne peut pas être sélectionnée."
                    return [False, texte_messages1]
        elif self.partie.damier.piece_peut_se_deplacer(self.position):
            self.messages1['foreground'] = 'black'
            texte_messages1 = 'La pièce en position ' + position_source_damier_reel \
                                       + ' a été sélectionnée. Cliquez sur la cible désirée. '
            return [True, texte_messages1]
        else:
            texte_messages1 = "La pièce que vous avez sélectionnée ne peut pas se déplacer. Veuillez " \
                                         "faire un autre choix. "
            return [False, texte_messages1]

    def valider_et_enregistrer_position_cible(self):
        """
        S'assure que la pièce choisie comme position source peut se déplacer à la position cible, soit en faisant
        une prise ou en se déplaçant.

        return:
                [0] : True ou False
                [1] : Message à afficher si la cible n'est pas valide.
        """
        if self.doit_prendre == True:
            print("i-305 : ", self.partie.couleur_joueur_courant)
            if self.partie.damier.piece_peut_sauter_vers(self.position, self.position_cible,
                                                         self.partie.couleur_joueur_courant):
                return [True, ""]

            else:
                texte_messages1 = "La pièce choisie doit prendre une pièce adverse. La cible choisie doit être modifiée."
                return [False, texte_messages1]

        elif self.partie.damier.piece_peut_se_deplacer_vers(self.position, self.position_cible):
             return [True, ""]
        else:
            texte_messages1 = "La pièce choisie ne peut pas être déplacée vers cette case."
        return [False, texte_messages1]

    def aide(self):
        fenetre_A = Tk()
        # self.texte_aide = Label()

        # self.texte_aide['foreground'] = 'blue'
        # self.texte_aide['text'] = 'Houba!'
        # self.texte_aide.grid(fenetre_A)
        # self.bouton1_C = Button(self, text='Quitter', command=self.quit)
        # self.bouton1_C.grid(fenetre_A)
        fenetre_A.mainloop()

if __name__ == '__main__':
    # Point d'entrée principal du jeu de dame et de l'affichage du damier.
    fenetre = FenetrePartie()
    fenetre.mainloop()

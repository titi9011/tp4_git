# Auteurs: Thierry Blais et Bernard Sévigny

from tkinter import *  # Tk, Label, NSEW, dnd
from canvas_damier import CanvasDamier
from partie import Partie
from position import Position
from datetime import date
import os
from ast import literal_eval

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
        try:
            print(self.activation_partie_sauvegardee)
            if self.activation_partie_sauvegardee == 1:
                damier_actuel = self.damier_ouvert
                print("i-37")
        except:
            damier_actuel = self.partie.damier
            print("i-40")
            # print("41", self.damier_ouvert)
           # print(self.activation_partie_sauvegardee)
        self.canvas_damier = CanvasDamier(self, damier_actuel, 60)
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
        self.bouton1_A = Button(self, text = 'Aide', command = self.aide,)
        self.bouton1_B = Button(self, text = 'Quitter', command = self.quitter_damier)
        self.bouton1_C = Button(self, text='Partie sauvegardée', command=self.partie_sauvegardee)
        self.bouton1_A.grid(row=2, column=0, pady=5)
        self.bouton1_B.grid(row=1, column=1, padx=25, pady=5)  # , sticky=E)
        self.bouton1_C.grid(row=2, column=1, pady=5, sticky=E)

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
                    self.messages1['foreground'] = 'red'
                    self.messages1['text'] = self.valider_et_enregistrer_position_cible()[1]
                    raise ValueError

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
        """
        Fait apparaître une fenêtre contextuelle présentant, sous la forme d'un texte, l'aide à l'utilisation
        du programme damier ainsi que les règlements applicables.
        Le bouton "Quitter" permet de fermer la fenêtre et de retourner au damier.
        """
        self.fenetre_2 = Tk()
        self.fenetre_2.title("Aide et règlements")

        texte_aide0 = Message(self.fenetre_2)
        texte_aide0['foreground'] = 'brown'

        texte_aide1 = Message(self.fenetre_2, width=492)
        texte_aide1['foreground'] = 'blue'

        texte_aide2 = Message(self.fenetre_2)
        texte_aide2['foreground'] = 'brown'

        texte_aide3 = Message(self.fenetre_2)
        texte_aide3['foreground'] = 'blue'

        Extrait_aide = open("Aide_reglements.txt", 'r', encoding="utf-8")
        texte_extrait = Extrait_aide.readlines()
        texte_aide0['text'] = texte_extrait[0]
        texte_aide1['text'] = texte_extrait[1]
        for i in range(2, 5):
            texte_aide1['text'] = texte_aide1['text'] + texte_extrait[i]

        texte_aide2['text'] = texte_extrait[5]
        texte_aide3['text'] = texte_extrait[6]
        for i in range(7, len(texte_extrait)):
              texte_aide3['text'] = texte_aide3['text'] + texte_extrait[i]
        Extrait_aide.close()
        texte_aide0.grid()
        texte_aide1.grid(sticky=W)
        texte_aide2.grid()
        texte_aide3.grid(sticky=W)
        bouton2_A = Button(self.fenetre_2, text='Quitter', command=self.fenetre_aide_quit)
        bouton2_A.grid()
        self.fenetre_2.tkraise()  # mainloop()

    def fenetre_aide_quit(self):
        """
        Méthode appelée par le bouton "Quitter" de la fenêtre "Aide et règlements".
        Permet de fermer la fenêtre en permettant aux joueurs de retourner au jeu déjà commencé.
        """
        self.fenetre_2.withdraw()

    def quitter_damier(self):
        self.fenetre_3 = Tk()
        self.fenetre_3.geometry("460x230")
        self.fenetre_3.title("Pourquoi quitter?")

        # texte_3_A = Message(self.fenetre_3)
        texte_3_A = Label(self.fenetre_3)
        texte_3_B = Label(self.fenetre_3)
        texte_3_C = Label(self.fenetre_3)
        texte_3_D = Label(self.fenetre_3)
        texte_3_A['text'] = "1- Si vous ouvrez une nouvelle partie, la partie non terminée que vous venez de quitter"
        texte_3_B['text'] = "sera encore accessible et il sera possible de jouer deux parties à la fois!\n "
        texte_3_C['text'] = "2- En annulant, vous retournez à la partie déjà ouverte.\n "
        texte_3_D['text'] = "3- Si vous quittez sans sauvegarder, toutes les parties seront fermées."
        texte_3_A.grid(sticky=W)
        texte_3_B.grid(sticky=W)
        texte_3_C.grid(sticky=W)
        texte_3_D.grid(sticky=W)
        bouton3_A = Button(self.fenetre_3, text='Quitter et sauvegarder', command=self.sauvegarde_partie)
        bouton3_B = Button(self.fenetre_3, text='Quitter sans sauvegarder', command=self.quit)
        bouton3_C = Button(self.fenetre_3, text='Nouvelle partie', command=self.nouvelle_partie)
        bouton3_D = Button(self.fenetre_3, text='Annuler', command=self.fenetre_quit_annulee)
        bouton3_A.grid(row=4, column=0, pady=10, sticky=W)
        bouton3_B.grid(row=4, column=0, pady=10, sticky=E)
        bouton3_C.grid(row=5, column=0, sticky=W)
        bouton3_D.grid(row=5, column=0, sticky=E)
        self.fenetre_3.tkraise()
        # Boutons activés :
            # A. Quitter et sauvegarder
            # B. Quitter sans sauvegarder
            # C. Nouvelle partie
            # D. Annuler et revenir à la partie

    def sauvegarde_partie(self):
        """
        Méthode appelée par le bouton "Quitter et sauvegarder" de la fenêtre "Quitter".
        Permet de sauvegarder la partie au point où elle était rendue.
        """
        self.fenetre_4 = Tk()
        self.fenetre_4.geometry("500x130")
        self.fenetre_4.title("Fichier de sauvegarde")
        # Sauvegarde de plusieurs parties à la même date
        # Le nom des fichiers contient la date de la sauvegarde
        n_fich = 1
        while os.path.isfile("Sauvegarde-" + str(date.today()) + "(" + str(n_fich) + ").txt"):
            n_fich += 1
        nom_fichier_sauvegarde = "Sauvegarde-" + str(date.today()) + "(" + str(n_fich) + ").txt"

        fichier_partie = open(nom_fichier_sauvegarde, "w")
        fichier_partie.write(str(self.partie.couleur_joueur_courant))
        fichier_partie.write("\n")
        fichier_partie.write(self.partie.damier.str_dic(self.partie.damier.cases))
        fichier_partie.close()

        texte_4_A = Label(self.fenetre_4)
        texte_4_B = Label(self.fenetre_4)
        texte_4_C = Label(self.fenetre_4)
        texte_4_D = Label(self.fenetre_4)
        texte_4_A['foreground'] = 'blue'
        texte_4_B['foreground'] = 'green'
        texte_4_C['foreground'] = 'blue'
        texte_4_A['text'] = "La partie que vous quittez a été sauvegardée dans le fichier : "
        texte_4_B['text'] = nom_fichier_sauvegarde  # + "!"
        texte_4_C['text'] = "!"
        texte_4_A.grid(row=0, column=0)
        texte_4_B.grid(row=0, column=1)
        texte_4_C.grid(row=0, column=2)
        texte_4_D.grid(row=1, column=0)
        bouton4_A = Button(self.fenetre_4, text='Quitter le jeu', command=self.quit)
        bouton4_B = Button(self.fenetre_4, text='Retour au jeu', command=self.retour_jeu)
        bouton4_A.grid(row=2, column=0, sticky=SW)
        bouton4_B.grid(row=2, column=0, sticky=SE)
        self.fenetre_4.tkraise()

    def nouvelle_partie(self):
        """
        Méthode appelée par le bouton "Nouvelle partie" de la fenêtre "Quitter".
        Ouvre une autre fenêtre de jeu sans fermer le damier déjà commencé,
        permettant aux joueurs de jouer plusieurs parties simultanées.
        """
        self.fenetre_3.withdraw()
        fenetre = FenetrePartie()
        fenetre.mainloop()

    def partie_sauvegardee(self):
        #TODO À compléter
        """
        Méthode appelée par le bouton "Partie sauvegardée" de la fenêtre principale.
        Permet d'ouvrir une partie non complétée au point où elle avait été arrêtée.
        """
        self.fenetre_5 = Tk()
        self.fenetre_5.geometry("400x230")  # Ajuster
        self.fenetre_5.title("Fichiers sauvegardés")

        texte_5_A = Label(self.fenetre_5)
        bouton5_A = Button(self.fenetre_5, text='Annuler', command=self.ouverture_fich_annulee)

        self.liste_fich = Listbox(self.fenetre_5, width=27, height=10, selectmode=SINGLE)
        fich_insere = 0
        for nom_fich in os.listdir():
            if nom_fich[0:10] == "Sauvegarde":
                self.liste_fich.insert(END, nom_fich)
                fich_insere +=1
        if fich_insere != 0:
            texte_5_A['foreground'] = 'purple'
            texte_5_A['text'] = "Liste des fichiers de sauvegarde dans le répertoire du projet :"
            self.liste_fich.grid(row=2, column=0)
            self.liste_fich.bind('<Double-Button-1>', lambda event : self.ouvrir_sauvegarde())

        else:
            texte_5_A['foreground'] = 'red'
            texte_5_A['text'] = "Il n'y a pas de fichiers de sauvegarde dans le répertoire du projet."
        texte_5_A.grid(row=0, column=0)  # Ajuster

        bouton5_A.grid(row=2, column=1, sticky=N)
        self.fenetre_5.tkraise()

    def ouvrir_sauvegarde(self):
        self.index_fich_select = self.liste_fich.curselection()[0]

        nom_fichier = open(self.liste_fich.get(self.index_fich_select), "r")
        self.partie.couleur_joueur_courant = nom_fichier.readline()
        damier_cases = nom_fichier.readline()
        self.damier_ouvert = literal_eval(damier_cases)
        nom_fichier.close()
        self.fenetre_5.withdraw()
        self.activation_partie_sauvegardee = 1
        print("i-443")
        fenetre = FenetrePartie()  # self.canvas_damier.actualiser()
        fenetre.mainloop()

    def fenetre_quit_annulee(self):
        """
        Méthode appelée par le bouton "Annuler" de la fenêtre "Quitter".
        Permet de fermer la fenêtre en permettant aux joueurs de retourner au jeu déjà commencé.
        """
        self.fenetre_3.withdraw()

    def retour_jeu(self):
        """
        Méthode appelée par le bouton "Retour au jeu" de la fenêtre "Quitter et sauvegarder".
        Ferme la fenêtre confirmant le nom du fichier de sauvegarde sans fermer ni le damier déjà commencé
        ni la fenêtre contextuelle, permettant aux joueurs de retourner à la partie en cours.
        """
        self.fenetre_3.withdraw()
        self.fenetre_4.withdraw()

    def ouverture_fich_annulee(self):
        """
        Méthode appelée par le bouton "Annuler" de la fenêtre "Quitter".
        Permet de fermer la fenêtre en permettant aux joueurs de retourner au jeu déjà commencé.
        """
        self.fenetre_5.withdraw()

if __name__ == '__main__':
    # Point d'entrée principal du jeu de dame et de l'affichage du damier.
    fenetre = FenetrePartie()
    fenetre.mainloop()

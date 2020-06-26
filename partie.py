# Auteurs: À compléter

from damier import Damier
from position import Position


class Partie:
    """Gestionnaire de partie de dames.

    Attributes:
        damier (Damier): Le damier de la partie, contenant notamment les pièces.
        couleur_joueur_courant (str): Le joueur à qui c'est le tour de jouer.
        doit_prendre (bool): Un booléen représentant si le joueur actif doit absolument effectuer une prise
            de pièce. Sera utile pour valider les mouvements et pour gérer les prises multiples.
        position_source_selectionnee (Position): La position source qui a été sélectionnée. Utile pour sauvegarder
            cette information avant de poursuivre. Contient None si aucune pièce n'est sélectionnée.
        position_source_forcee (Position): Une position avec laquelle le joueur actif doit absolument jouer. Le
            seul moment où cette position est utilisée est après une prise: si le joueur peut encore prendre
            d'autres pièces adverses, il doit absolument le faire. Ce membre contient None si aucune position n'est
            forcée.

    """
    def __init__(self):
        """Constructeur de la classe Partie. Initialise les attributs à leur valeur par défaut. Le damier est construit
        avec les pièces à leur valeur initiales, le joueur actif est le joueur blanc, et celui-ci n'est pas forcé
        de prendre une pièce adverse. Aucune position source n'est sélectionnée, et aucune position source n'est forcée.

        """
        self.damier = Damier()
        self.couleur_joueur_courant = "blanc"
        self.doit_prendre = False
        self.position_source_selectionnee = None
        self.position_source_forcee = None

    def position_source_valide(self, position_source):
        """Vérifie la validité de la position source, notamment:
            - Est-ce que la position contient une pièce?
            - Est-ce que cette pièce est de la couleur du joueur actif?
            - Si le joueur doit absolument continuer son mouvement avec une prise supplémentaire, a-t-il choisi la
              bonne pièce?

        Cette méthode retourne deux valeurs. La première valeur est Booléenne (True ou False), et la seconde valeur est
        un message d'erreur indiquant la raison pourquoi la position n'est pas valide (ou une chaîne vide s'il n'y a pas
        d'erreur).

        ATTENTION: Utilisez les attributs de la classe pour connaître les informations sur le jeu! (le damier, le joueur
            actif, si une position source est forcée, etc.

        ATTENTION: Vous avez accès ici à un attribut de type Damier. vous avez accès à plusieurs méthodes pratiques
            dans le damier qui vous simplifieront la tâche ici :)

        Args:
            position_source (Position): La position source à valider.

        Returns:
            bool, str: Un couple où le premier élément représente la validité de la position (True ou False), et le
                 deuxième élément est un message d'erreur (ou une chaîne vide s'il n'y a pas d'erreur).

        """
        #TODO: À tester - compléter
        if position_source in self.damier.cases:
            if self.damier.cases[position_source].couleur == self.couleur_joueur_courant:
                return [True, ""]
            else:
                return [False, "Le pion sur la case n'est pas de la couleur qui vous a été attribuée. Veuillez choisir une autre pièce."]
        else:
                return [False, "Il n'y a pas de pièce sur la case que vous avez sélectionnée. Veuillez faire un autre choix."]


    def position_cible_valide(self, position_cible):
        """Vérifie si la position cible est valide (en fonction de la position source sélectionnée). Doit non seulement
        vérifier si le déplacement serait valide (utilisez les méthodes que vous avez programmées dans le Damier!), mais
        également si le joueur a respecté la contrainte de prise obligatoire.

        Returns:
            bool, str: Deux valeurs, la première étant Booléenne et indiquant si la position cible est valide, et la
                seconde valeur est une chaîne de caractères indiquant un message d'erreur (ou une chaîne vide s'il n'y
                a pas d'erreur).

        """
        #TODO: À compléter



        # Damier.piece_peut_se_deplacer_vers(position_piece, position_cible)
        # Damier.piece_peut_faire_une_prise(position_piece)


    def demander_positions_deplacement(self):
        """Demande à l'utilisateur les positions sources et cible, et valide ces positions. Cette méthode doit demander
        les positions à l'utilisateur tant que celles-ci sont invalides.

        Cette méthode ne doit jamais planter, peu importe ce que l'utilisateur entre.

        Returns:
            Position, Position: Un couple de deux positions (source et cible).

        """
        #TODO: À tester - compléter

        verif_source_cible = True
        while verif_source_cible:
            valeur_non_valide = True
            while valeur_non_valide:
                try:
                    position_source = input("Quelle pièce désirez-vous déplacer? ").strip()
                    self.ligne = int(position_source[0])
                except:
                    if ValueError:
                        print("L'entrée devrait être un nombre et est invalide. Veuillez essayer de nouveau!")
                    else:
                        print("L'entrée est invalide. Veuillez essayer de nouveau!")
                else:
                    valeur_non_valide = False

            try:
                self.colonne = int(position_source[2])
            except:
                valeur_non_valide = True
                while valeur_non_valide:
                    try:
                        colonne_test = input(
                            "La valeur entrée comme colonne est invalide. Veuillez entrer de nouveau la colonne!").strip()
                        self.colonne = int(self.colonne)
                    except:
                        print("La pièce que vous désirez déplacer est dans la rangée {}.\n".format(self.ligne))
                        if ValueError:
                            print("L'entrée devrait être un nombre et est invalide. Veuillez essayer de nouveau!")
                        else:
                            print("L'entrée est invalide. Veuillez essayer de nouveau!")
                    else:
                        valeur_non_valide = False

            position_source_selectionnee = "Position(" + str(self.ligne) + "," + str(self.colonne) + ")"
            print("posn sélect :", position_source_selectionnee)  # temp
            position_source_selectionnee = eval(position_source_selectionnee)
            if self.position_source_valide(position_source_selectionnee)[0]:
                print("PSS", position_source_selectionnee)  # temp
                print("PSS", self.damier.piece_peut_faire_une_prise(position_source_selectionnee))  # temp
                if self.doit_prendre == True:
                    if self.position_source_forcee != None:
                        if self.position_source_forcee != position_source_selectionnee:
                            print("Vous devez prendre. La pièce en position {} doit être sélectionnée".format(self.position_source_forcee))
                            # self.damier.piece_peut_faire_une_prise(self.position_source_forcee)
                            verif_source_cible = False
                        else:
                            print("Vous devez prendre. La pièce choisie ne peut pas être sélectionnée")
                    else:
                        print("Compléter : S'assurer d'avoir une pièce qui peut prendre.")
                        verif_source_cible = False
                elif self.damier.piece_peut_faire_une_prise(position_source_selectionnee):  #, position_cible):
                    verif_source_cible = False
                    self.position_source_forcee = position_source_selectionnee
                elif self.damier.piece_peut_se_deplacer(position_source_selectionnee):
                    verif_source_cible = False
                else:
                    print("La pièce que vous avez sélectionnée ne peut pas se déplacer. Veuillez faire un autre choix.")
            else:  # temp
                print(self.position_source_valide(position_source_selectionnee)[1],"\n")  # temp

        verif_source_cible = True
        while verif_source_cible:
            valeur_non_valide = True
            while valeur_non_valide:
                try:
                    position_cible = input("Destination choisie : ").strip()
                    self.ligne = int(position_cible[0])
                except:
                    if ValueError:
                        print("L'entrée devrait être un nombre et est invalide. Veuillez essayer de nouveau!")
                    else:
                        print("L'entrée est invalide. Veuillez essayer de nouveau!")
                else:

                    valeur_non_valide = False

            try:
                self.colonne = int(position_cible[2])
            except:
                valeur_non_valide = True
                while valeur_non_valide:
                    try:
                        colonne_test = input(
                            "La valeur entrée comme colonne est invalide. Veuillez entrer de nouveau la colonne!").strip()
                        self.colonne = int(self.colonne)
                    except:
                        print("La pièce que vous désirez déplacer est dans la rangée {}.\n".format(self.ligne))
                        if ValueError:
                            print("L'entrée devrait être un nombre et est invalide. Veuillez essayer de nouveau!")
                        else:
                            print("L'entrée est invalide. Veuillez essayer de nouveau!")
                    else:
                        valeur_non_valide = False

            position_cible = eval("Position(" + str(self.ligne) + ", " + str(self.colonne) + ")")

            if self.damier.piece_peut_sauter_vers(position_source_selectionnee, position_cible):
                verif_source_cible = False
            elif self.damier.piece_peut_se_deplacer_vers(position_source_selectionnee, position_cible):
                verif_source_cible = False
            else:
                print("La pièce choisie ne peut pas être déplacée vers cette case.\n")

        return [position_source_selectionnee, position_cible]

    def tour(self):
        """Cette méthode effectue le tour d'un joueur, et doit effectuer les actions suivantes:
        - Assigne self.doit_prendre à True si le joueur courant a la possibilité de prendre une pièce adverse.
        - Affiche l'état du jeu
        - Demander les positions source et cible (utilisez self.demander_positions_deplacement!)
        - Effectuer le déplacement (à l'aide de la méthode du damier appropriée)
        - Si une pièce a été prise lors du déplacement, c'est encore au tour du même joueur si celui-ci peut encore
          prendre une pièce adverse en continuant son mouvement. Utilisez les membres self.doit_prendre et
          self.position_source_forcee pour forcer ce prochain tour!
        - Si aucune pièce n'a été prise ou qu'aucun coup supplémentaire peut être fait avec la même pièce, c'est le
          tour du joueur adverse. Mettez à jour les attributs de la classe en conséquence.

        """

        # Détermine si le joueur courant a la possibilité de prendre une pièce adverse.
        #while True:  # True est temporaire
        if self.damier.piece_de_couleur_peut_faire_une_prise(self.couleur_joueur_courant):
            self.doit_prendre = True
            print("Doit prendre activé - forcée? ", self.position_source_forcee)
        # Affiche l'état du jeu
        print(self.damier)
        print("")
        print("Tour du joueur", self.couleur_joueur_courant, end=".")
        if self.doit_prendre:
            if self.position_source_forcee is None:
                print(" Il doit prendre une pièce.")
            else:
                print(" Il doit prendre avec la pièce en position {}.".format(self.position_source_forcee))
        else:
            print("")

        # Demander les positions

        # TODO: À compléter

            print("tour 1")  # temp
        [position_source, position_cible] = self.demander_positions_deplacement()
        print("tour 2\t")  # temp
        print("Source :", position_source)  # temp
        print(self.damier.position_est_dans_damier(position_source))  # temp
        print("Cible : ", position_cible)  # temp
        print(self.damier.position_est_dans_damier(position_cible))  # temp
        # Effectuer le déplacement (à l'aide de la méthode du damier appropriée)

        # TODO: À compléter

        retour_apres_deplacement = self.damier.deplacer(position_source, position_cible)


        # Mettre à jour les attributs de la classe
        # TODO: À compléter

        # Thierry (et Bernard!), il faut mettre à jour les attributs :
        if retour_apres_deplacement == "ok":
            pass
        elif retour_apres_deplacement == "prise":
            # Vérifier si peut prendre encore
            # Sinon :
            self.doit_prendre = False
            self.position_source_selectionnee = None
            self.position_source_forcee = None
        else:
            print("Il y a erreur dans le code!")


        if self.couleur_joueur_courant == "blanc":
            self.couleur_joueur_courant = "noir"
        else:
            self.couleur_joueur_courant = "blanc"

    def jouer(self):
        """Démarre une partie. Tant que le joueur courant a des déplacements possibles (utilisez les méthodes
        appriopriées!), un nouveau tour est joué.

        Returns:
            str: La couleur du joueur gagnant.
        """

        while self.damier.piece_de_couleur_peut_se_deplacer(self.couleur_joueur_courant) or \
                self.damier.piece_de_couleur_peut_faire_une_prise(self.couleur_joueur_courant):
            print("Houba jeu : ", self.couleur_joueur_courant)
            print("Houba jeu 2 :", self.damier.piece_de_couleur_peut_se_deplacer(self.couleur_joueur_courant))
            print("Houba jeu 3 : ", self.damier.piece_de_couleur_peut_faire_une_prise(self.couleur_joueur_courant))

            self.tour()
            print("Houba jeu 4")
            print("Houba jeu 5 : ", self.couleur_joueur_courant)
            print("Houba jeu 6 :", self.damier.piece_de_couleur_peut_se_deplacer(self.couleur_joueur_courant))
        if self.couleur_joueur_courant == "blanc":
            return "noir"
        else:
            return "blanc"


if __name__ == "__main__":
    # Point d'entrée du programme. On initialise une nouvelle partie, et on appelle la méthode jouer().
    partie = Partie()

    gagnant = partie.jouer()

    print("------------------------------------------------------")
    print("Partie terminée! Le joueur gagnant est le joueur", gagnant)
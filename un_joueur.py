from engine import avance
from interface_dames import FenetrePartie

class Un_joueur(FenetrePartie):
    def __init__(self):
        super.__init__()
    
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

        

if __name__ == '__main__':
    fenetre = FenetrePartie()
    fenetre.mainloop()
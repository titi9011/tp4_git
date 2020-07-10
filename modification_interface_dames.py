drapeau_appelant_cible = False
drapeau_appelant_positions = True
while drapeau_appelant_positions == True:
    if drapeau_appelant_cible == False:
        ligne = event.y // self.canvas_damier.n_pixels_par_case
        colonne = event.x // self.canvas_damier.n_pixels_par_case
        self.position = Position(ligne, colonne)
        print("Source-i-80", self.position)  # temp
        print(self.partie.position_source_valide(self.position))
        if self.partie.position_source_valide(self.position)[0]:
            self.messages1['foreground'] = 'black'
            position_source_damier_reel = self.colonne_damier_reel[self.position.colonne] + str(
                8 - self.position.ligne)
            self.messages1['text'] = 'Vous devez prendre. La pièce en position ' \
                                     + position_source_damier_reel + ' doit être sélectionnée.'
            # ligne = event.y // self.canvas_damier.n_pixels_par_case
            # colonne = event.x // self.canvas_damier.n_pixels_par_case
            # position = Position(ligne, colonne)
            # test_f = dnd.on_release()
            print("i-205", self.doit_prendre)
            if self.doit_prendre == True:
                if self.position_source_forcee is None:
                    pass
                else:
                    if self.position_source_forcee == self.position:
                        self.messages1['foreground'] = 'red'
                        self.messages1[
                            'text'] = "Vous devez prendre. La pièce en position ", position_source_damier_reel, " a été sélectionnée."
                        # self.damier.piece_peut_faire_une_prise(self.position_source_forcee)
                        # verif_source_cible = False
                    else:
                        self.messages1['foreground'] = 'red'
                        self.messages1[
                            'text'] = "Vous devez prendre. La pièce choisie ne peut pas être sélectionnée."

            elif self.partie.damier.piece_peut_se_deplacer(self.position):
                pass
            else:
                self.messages1['foreground'] = 'red'
                self.messages1[
                    'text'] = "La pièce que vous avez sélectionnée ne peut pas se déplacer. Veuillez " \
                              "faire un autre choix. "
        else:
            self.messages1['foreground'] = 'red'
            self.messages1['text'] = self.partie.position_source_valide(self.position)[1]
        drapeau_appelant_cible = True
    else:
        ligne = event.y // self.canvas_damier.n_pixels_par_case
        colonne = event.x // self.canvas_damier.n_pixels_par_case
        self.position_cible = Position(ligne, colonne)
        print("Cible-i-86", self.position_cible)  # temp

        if self.partie.position_cible_valide(self.position_cible)[0]:  # À enlever
            self.messages1['foreground'] = 'black'
            position_source_damier_reel = self.colonne_damier_reel[self.position.colonne] + str(
                8 - self.position.ligne)
            position_cible_damier_reel = self.colonne_damier_reel[self.position_cible.colonne] + str(
                8 - self.position_cible.ligne)
            self.messages1['text'] = 'Pièce à la position {} déplacée à {}.'.format(position_source_damier_reel,
                                                                                    position_cible_damier_reel)

            if self.doit_prendre == True:
                if self.partie.damier.piece_peut_sauter_vers(self.position, self.position_cible):
                    print("i-116")  # verif_cible = False
                    pass
                else:
                    self.messages1['foreground'] = 'red'
                    self.messages1[
                        'text'] = "La pièce choisie doit prendre une pièce adverse. La cible choisie doit être modifiée."
                    # 1 / 0  # Génère une erreur pour modifier la position cible
            elif self.partie.damier.piece_peut_se_deplacer_vers(self.position, self.position_cible):
                print("i-123 ", self.partie.damier.piece_peut_se_deplacer_vers(self.position,
                                                                               self.position_cible))  # temp
                # pass
            else:
                self.messages1['foreground'] = 'red'
                self.messages1['text'] = "La pièce choisie ne peut pas être déplacée vers cette case."

        drapeau_appelant_cible = False
        drapeau_appelant_positions = False
p = input("Houb")
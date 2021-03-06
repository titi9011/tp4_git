# Auteurs: Thierry Blais et Bernard Sévigny

from piece import Piece
from position import Position


class Damier:
    """Plateau de jeu d'un jeu de dames. Contient un ensemble de pièces positionnées à une certaine position
    sur le plateau.
    Attributes:
        cases (dict): Dictionnaire dont une clé représente une Position, et une valeur correspond à la Piece
            positionnée à cet endroit sur le plateau. Notez bien qu'une case vide (sans pièce blanche ou noire)
            correspond à l'absence de clé la position de cette case dans le dictionnaire.
        n_lignes (int): Le nombre de lignes du plateau. La valeur est 8 (constante).
        n_colonnes (int): Le nombre de colonnes du plateau. La valeur est 8 (constante).
    """

    def __init__(self):
        """Constructeur du Damier. Initialise un damier initial de 8 lignes par 8 colonnes.
        """
        self.n_lignes = 8
        self.n_colonnes = 8
        #if self.partie.activation_partie_sauvegardee != None:

        self.cases = {
            Position(7, 0): Piece("blanc", "pion"),
            Position(7, 2): Piece("blanc", "pion"),
            Position(7, 4): Piece("blanc", "pion"),
            Position(7, 6): Piece("blanc", "pion"),
            Position(6, 1): Piece("blanc", "pion"),
            Position(6, 3): Piece("blanc", "pion"),
            Position(6, 5): Piece("blanc", "pion"),
            Position(6, 7): Piece("blanc", "pion"),
            Position(5, 0): Piece("blanc", "pion"),
            Position(5, 2): Piece("blanc", "pion"),
            Position(5, 4): Piece("blanc", "pion"),
            Position(5, 6): Piece("blanc", "pion"),
            Position(2, 1): Piece("noir", "pion"),
            Position(2, 3): Piece("noir", "pion"),
            Position(2, 5): Piece("noir", "pion"),
            Position(2, 7): Piece("noir", "pion"),
            Position(1, 0): Piece("noir", "pion"),
            Position(1, 2): Piece("noir", "pion"),
            Position(1, 4): Piece("noir", "pion"),
            Position(1, 6): Piece("noir", "pion"),
            Position(0, 1): Piece("noir", "pion"),
            Position(0, 3): Piece("noir", "pion"),
            Position(0, 5): Piece("noir", "pion"),
            Position(0, 7): Piece("noir", "pion"),
        }

    def str_piece(self, piece):
        if str(piece) == 'x':
            return 'Piece("noir", "pion")'
        if str(piece) == 'X':
            return 'Piece("noir", "dame")'
        if str(piece) == 'o':
            return 'Piece("blanc", "pion")'
        if str(piece) == 'O':
            return 'Piece("blanc", "blanc")'

    def str_position(self, position):
        return 'Position' + str(position)

    def str_dic(self, dic):
        new_dic = {}
        for position, piece in dic.items():
            new_dic[self.str_position(position)] = self.str_piece(piece)
        return str(new_dic)

    def recuperer_piece_a_position(self, position):
        """Récupère une pièce dans le damier à partir d'une position.
        Args:
            position (Position): La position où récupérer la pièce.
        Returns:
            La pièce (de type Piece) à la position reçue en argument, ou None si aucune pièce n'était à cette position.
        """
        if position not in self.cases:
            return None

        return self.cases[position]

    def position_est_dans_damier(self, position):
        """Vérifie si les coordonnées d'une position sont dans les bornes du damier (entre 0 inclusivement et le nombre
        de lignes/colonnes, exclusement.
        Args:
            position (Position): La position à valider.
        Returns:
            bool: True si la position est dans les bornes, False autrement.
        """
        if position.ligne in range(8) and position.colonne in range(8):
            return True
        else:
            return False

    def piece_peut_se_deplacer_vers(self, position_piece, position_cible):
        """Cette méthode détermine si une pièce (à la position reçue) peut se déplacer à une certaine position cible.
        On parle ici d'un déplacement standard (et non une prise).
        Une pièce doit être positionnée à la position_piece reçue en argument (retourner False autrement).
        Une pièce de type pion ne peut qu'avancer en diagonale (vers le haut pour une pièce blanche, vers le bas pour
        une pièce noire). Une pièce de type dame peut avancer sur n'importe quelle diagonale, peu importe sa couleur.
        Une pièce ne peut pas se déplacer sur une case déjà occupée par une autre pièce. Une pièce ne peut pas se
        déplacer à l'extérieur du damier.
        Args:
            position_piece (Position): La position de la pièce source du déplacement.
            position_cible (Position): La position cible du déplacement.
        Returns:
            bool: True si la pièce peut se déplacer à la position cible, False autrement.
        """
        #si la position est dans le damier et s'il y a une piece sur la case et si la position_cible n'est pas occupée
        if self.position_est_dans_damier(position_cible) and position_piece in self.cases and not position_cible in self.cases:

            if self.recuperer_piece_a_position(position_piece).est_dame():
                if position_cible in position_piece.quatre_positions_diagonales():
                    return True
                else:

                    return False

            elif self.recuperer_piece_a_position(position_piece).est_noire():
                if position_cible in position_piece.positions_diagonales_bas():
                    return True
                else:
                    return False
            elif self.recuperer_piece_a_position(position_piece).est_blanche():
                if position_cible in position_piece.positions_diagonales_haut():
                    return True
                else:
                    return False
        else:
            return False

    def piece_peut_sauter_vers(self, position_piece, position_cible, couleur_joueur):
        """Cette méthode détermine si une pièce (à la position reçue) peut sauter vers une certaine position cible.
        On parle ici d'un déplacement qui "mange" une pièce adverse.
        Une pièce doit être positionnée à la position_piece reçue en argument (retourner False autrement).
        Une pièce ne peut que sauter de deux cases en diagonale. N'importe quel type de pièce (pion ou dame) peut sauter
        vers l'avant ou vers l'arrière. Une pièce ne peut pas sauter vers une case qui est déjà occupée par une autre
        pièce. Une pièce ne peut faire un saut que si elle saute par dessus une pièce de couleur adverse.
        Args:
            position_piece (Position): La position de la pièce source du saut.
            position_cible (Position): La position cible du saut.
            couleur: Couleur du joueur courant.
        Returns:
            bool: True si la pièce peut sauter vers la position cible, False autrement.
        """
        position_piece_mange = position_piece.position_mange(position_cible)
        piece_mange = self.recuperer_piece_a_position(position_piece_mange)

        # S'il y a une pièce sur la case et si la position_cible est libre"
        if position_piece_mange != position_piece and position_piece_mange in self.cases \
                and position_cible != position_piece_mange:
            if self.cases[position_piece_mange].couleur == couleur_joueur:
                return False
            else:
                return True
        if self.position_est_dans_damier(position_cible) and position_piece in self.cases and not position_cible in self.cases:
            # Si une pièce adverse peut être prise"
            if position_piece_mange in self.cases and self.recuperer_piece_a_position(position_piece) != piece_mange:
                return True
            else:
                return False
        else:
            return False

    def piece_peut_se_deplacer(self, position_piece):
        """Vérifie si une pièce à une certaine position a la possibilité de se déplacer (sans faire de saut).
        ATTENTION: N'oubliez pas qu'étant donné une position, il existe une méthode dans la classe Position retournant
        les positions des quatre déplacements possibles.
        Args:
            position_piece (Position): La position source.
        Returns:
            bool: True si une pièce est à la position reçue et celle-ci peut se déplacer, False autrement.
        """
        verif_depl_possible = False
        if position_piece in self.cases:
            if (self.cases[position_piece].type_de_piece) == "dame":
                for i in range(4):
                    if self.position_est_dans_damier(position_piece.quatre_positions_diagonales()[i]):
                        if position_piece.quatre_positions_diagonales()[i] not in self.cases:
                            verif_depl_possible = True
            elif (self.cases[position_piece].type_de_piece) == "pion":
                if (self.cases[position_piece].couleur) == "blanc":
                    for i in range(2):
                        if self.position_est_dans_damier(position_piece.positions_diagonales_haut()[i]):
                            if position_piece.positions_diagonales_haut()[i] not in self.cases:
                                verif_depl_possible = True
                else:
                    for i in range(2):
                        if self.position_est_dans_damier(position_piece.positions_diagonales_bas()[i]):
                            if position_piece.positions_diagonales_bas()[i] not in self.cases:
                                verif_depl_possible = True

            else:
                print("La pièce choisie ne peut pas être déplacée.\n")

        else:
            print("Il n'y a pas de pièce de votre couleur dans la case sélectionnée.\n")

        return verif_depl_possible

    def piece_peut_faire_une_prise(self, position_piece):
        """Vérifie si une pièce à une certaine position a la possibilité de faire une prise.
        Warning:
            N'oubliez pas qu'étant donné une position, il existe une méthode dans la classe Position retournant
            les positions des quatre sauts possibles.
        Args:
            position_piece (Position): La position source.
        Returns:
            bool: True si une pièce est à la position reçue et celle-ci peut faire une prise. False autrement.
        """
        if position_piece in self.cases:
            for i in range(4):
                if self.position_est_dans_damier(position_piece.quatre_positions_sauts()[i]):
                    if position_piece.quatre_positions_diagonales()[i] in self.cases:
                        if self.cases[position_piece.quatre_positions_diagonales()[i]].couleur != self.cases[position_piece].couleur:
                            if position_piece.quatre_positions_sauts()[i] not in self.cases:
                                return True

        return False

    def piece_de_couleur_peut_se_deplacer(self, couleur):
        """Vérifie si n'importe quelle pièce d'une certaine couleur reçue en argument a la possibilité de se déplacer
        vers une case adjacente (sans saut).
        ATTENTION: Réutilisez les méthodes déjà programmées!
        Args:
            couleur (str): La couleur à vérifier.
        Returns:
            bool: True si une pièce de la couleur reçue peut faire un déplacement standard, False autrement.
        """
        for i in range(8):
            for j in range(8):
                if Position(i,j) in self.cases:
                    if self.cases[Position(i, j)].couleur == couleur:
                        if self.piece_peut_se_deplacer(Position(i, j)):
                            return True

        return False

    def piece_de_couleur_peut_faire_une_prise(self, couleur):
        """Vérifie si n'importe quelle pièce d'une certaine couleur reçue en argument a la possibilité de faire un
        saut, c'est à dire vérifie s'il existe une pièce d'une certaine couleur qui a la possibilité de prendre une
        pièce adverse.
        ATTENTION: Réutilisez les méthodes déjà programmées!
        Args:
            couleur (str): La couleur à vérifier.
        Returns:
            bool: True si une pièce de la couleur reçue peut faire un saut (une prise), False autrement.
        """
        for i in range(8):
            for j in range(8):
                if Position(i, j) in self.cases:
                    if self.cases[Position(i, j)].couleur == couleur:
                        for k in range(4):
                            if self.position_est_dans_damier(Position(i, j).quatre_positions_sauts()[k]):

                                if Position.quatre_positions_diagonales(Position(i, j))[k] in self.cases:

                                    if self.cases[Position.quatre_positions_diagonales(Position(i, j))[k]].couleur != couleur:
                                        if Position.quatre_positions_sauts(Position(i, j))[k] not in self.cases:
                                            return True

        return False

    def deplacer(self, position_source, position_cible):
        """Effectue le déplacement sur le damier. Si le déplacement est valide, on doit mettre à jour le dictionnaire
        self.cases, en déplaçant la pièce à sa nouvelle position (et possiblement en supprimant une pièce adverse qui a
        été prise).
        Cette méthode doit également:
        - Promouvoir un pion en dame si celui-ci atteint l'autre extrémité du plateau.
        - Retourner un message indiquant "ok", "prise" ou "erreur".
        ATTENTION: Si le déplacement est effectué, cette méthode doit retourner "ok" si aucune prise n'a été faite,
            et "prise" si une pièce a été prise.
        ATTENTION: Ne dupliquez pas de code! Vous avez déjà programmé (ou allez programmer) des méthodes permettant
            de valider si une pièce peut se déplacer vers un certain endroit ou non.
        Args:
            position_source (Position): La position source du déplacement.
            position_cible (Position): La position cible du déplacement.
        Returns:
            str: "ok" si le déplacement a été effectué sans prise, "prise" si une pièce adverse a été prise, et
                "erreur" autrement.
        """

        if not (not (position_cible.ligne == 0 and self.cases[
            Position(position_source.ligne, position_source.colonne)].couleur == "blanc") and not (
                position_cible.ligne == 7 and self.cases[
            Position(position_source.ligne, position_source.colonne)].couleur == "noir")):
            self.cases[Position(position_source.ligne, position_source.colonne)].type_de_piece = "dame"

        if abs(position_cible.ligne - position_source.ligne) == 1:
            self.cases[position_cible] = self.cases[position_source]
            del self.cases[position_source]
            return "ok"
        elif abs(position_cible.ligne - position_source.ligne) == 2:

            self.cases[position_cible] = self.cases[position_source]
            del self.cases[position_source]
            del self.cases[Position.position_mange(position_source, position_cible)]
            return "prise"
        else:
            return "erreur"

    def print_damier(self, dic):

        s = " +-0-+-1-+-2-+-3-+-4-+-5-+-6-+-7-+\n"
        for i in range(0, 8):
            s += str(i)+"| "
            for j in range(0, 8):
                if Position(i, j) in dic:
                    s += str(dic[Position(i, j)])+" | "
                else:
                    s += "  | "
            s += "\n +---+---+---+---+---+---+---+---+\n"

        return print(s)

    def __repr__(self):
        """Cette méthode spéciale permet de modifier le comportement d'une instance de la classe Damier pour
        l'affichage. Faire un print(un_damier) affichera le damier à l'écran.
        """
        s = " +-0-+-1-+-2-+-3-+-4-+-5-+-6-+-7-+\n"
        for i in range(0, 8):
            s += str(i)+"| "
            for j in range(0, 8):
                if Position(i, j) in self.cases:
                    s += str(self.cases[Position(i, j)])+" | "
                else:
                    s += "  | "
            s += "\n +---+---+---+---+---+---+---+---+\n"

        return s


if __name__ == "__main__":
    print('Test unitaires de la classe "Damier"...')

    un_damier = Damier()

    # Test 1
    assert un_damier.recuperer_piece_a_position(Position(4, 0)) is None
    assert un_damier.recuperer_piece_a_position(Position(0, 5)).est_pion()
    assert un_damier.recuperer_piece_a_position(Position(0, 5)).est_noire()

    # Test 2
    assert un_damier.position_est_dans_damier(Position(2, 2))
    assert not un_damier.position_est_dans_damier(Position(-1, 2))

    # Test 3
    assert not un_damier.piece_peut_se_deplacer_vers(Position(0, 0), Position(1, 1))
    assert un_damier.piece_peut_se_deplacer_vers(Position(2, 1), Position(3, 0))
    assert un_damier.piece_peut_se_deplacer_vers(Position(5, 0), Position(4, 1))
    assert not un_damier.piece_peut_se_deplacer_vers(Position(6, 1), Position(5, 2))
    assert not un_damier.piece_peut_se_deplacer_vers(Position(0, 7), Position(1, 6))

    # Test 4
    assert not un_damier.piece_peut_sauter_vers(Position(5, 4), Position(3, 6), "blanc")

    # Test 5
    assert un_damier.piece_peut_se_deplacer(Position(5, 2))
    assert un_damier.piece_peut_se_deplacer(Position(2, 1))
    assert not un_damier.piece_peut_se_deplacer(Position(6, 1))

    # Test 6
    assert not un_damier.piece_peut_faire_une_prise(Position(6, 1))
    assert not un_damier.piece_peut_faire_une_prise(Position(2, 5))

    # Test 7
    assert un_damier.piece_de_couleur_peut_se_deplacer("blanc")
    assert un_damier.piece_de_couleur_peut_se_deplacer("noir")

    # Test 8
    assert not un_damier.piece_de_couleur_peut_faire_une_prise("blanc")
    assert not un_damier.piece_de_couleur_peut_faire_une_prise("noir")

    # Test 9
    print(un_damier.deplacer(Position(6, 1), Position(5, 0)))
    assert un_damier.deplacer(Position(2, 1), Position(3, 0)) == 'ok'

    print('Tests unitaires passés avec succès!')
    # NOTEZ BIEN: Pour vous aider lors du développement, affichez le damier!
    print(un_damier)
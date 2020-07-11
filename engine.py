from partie import Partie
from position import Position
from piece import Piece
from interface_dames import FenetrePartie
from damier import Damier

class Engine(FenetrePartie):

    #initialisation de l'arbre des possibilités
    def __init__(self):
        super().__init__()


    def dic_blanc(self, dic):
        dic_blanc = {}
        for position, piece in dic.items():
            if piece.couleur == 'blanc':
                dic_blanc[position] = piece
        return dic_blanc

    def dic_noir(self, dic):
        dic_noir = {}
        for position, piece in dic.items():
            if piece.couleur == 'noir':
                dic_noir[position] = piece
        return dic_noir

    #détermine les cases qu'une pièce peut jouer
    #retourne la nouvelle position et la piece à supprimer
    def cases_jouable(self, position_source):
        #list des déplacement possible (dict)
        list_dic = []
        #si la piece peut faire un déplacement classique
        for position_cible in position_source.quatre_positions_diagonales():
            if Damier().piece_peut_se_deplacer_vers(position_source, position_cible):
                nouveau_dic = self.partie.damier.cases
                nouveau_dic[position_cible] = self.partie.damier.cases[position_source]
                del nouveau_dic[position_source]
                list_dic += nouveau_dic
        return list_dic
        
    def dic(self):
        return self.partie.damier.cases

Engine().cases_jouable(Position(5,4))
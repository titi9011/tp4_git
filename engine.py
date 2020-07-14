from partie import Partie
from position import Position
from piece import Piece
from interface_dames import FenetrePartie
from damier import Damier

class Engine():

    #initialisation de l'arbre des possibilités
    def __init__(self):
        pass

    def print_damier(self, dic):
        return Damier().print_damier(dic)

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
    def cases_jouable(self, position_source, dic):
        """Détermine les déplacements classiques possible.

        Attribut:
            position_source (dict): Clef et valeur d'une pièce.

        return: 
            list_dic (list): Une liste de dictionnaire représentant 
            les positions obtenablent en déplacant la pièce en queston.
        """
        #list des déplacement possible (dict)
        list_dic = []
        #si la piece peut faire un déplacement classique
        for position_cible in position_source.quatre_positions_diagonales():
            if Damier().piece_peut_se_deplacer_vers(position_source, position_cible):
                nouveau_dic = dict(dic)
                nouveau_dic[position_cible] = nouveau_dic[position_source]
                del nouveau_dic[position_source]
                list_dic.append(nouveau_dic)
        return list_dic

    def cases_jouable_saut(self, position_source, dic):
        """Détermine les sauts possiblent.

        Attribut:
            position_source (dict): Clef et valeur d'une pièce.

        return: 
            list_dic (list): Une liste de dictionnaire représentant 
            les positions obtenablent en déplaçant la pièce en queston.
        """
        #list des déplacement possible (dict)
        list_dic = []
        #si la piece peut faire un saut
        for position_cible in position_source.quatre_positions_sauts():
            if Damier().piece_peut_sauter_vers(position_source, position_cible):
                nouveau_dic = dict(dic)
                nouveau_dic[position_cible] = nouveau_dic[position_source]
                del nouveau_dic[position_source]
                #on supprime la pièce mangé
                piece_mange = position_source.position_mange(position_cible)
                del nouveau_dic[piece_mange]
                list_dic.append(nouveau_dic)
        return list_dic

    def dic_une_piece(self, position_source, dic):
        list_dic = []
        #ajout des sauts
        dic_saut = self.cases_jouable_saut(position_source, dic)
        if dic_saut != []:
            list_dic += dic_saut
        else:
            #ajout des positions classique
            dic_classique = self.cases_jouable(position_source, dic)
            list_dic += dic_classique
        return list_dic
    
    def iteration_dic(self, dic):
        dic_noir = self.dic_noir(dic)
        list_dic = []
        for position in list(dic_noir.keys()):
            dic_position = self.dic_une_piece(position, dic)
            self.print_damier(dic_position[0])



dic = FenetrePartie().partie.damier.cases
Engine().iteration_dic(dic)

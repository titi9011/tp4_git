from partie import Partie
from position import Position
from piece import Piece
from interface_dames import FenetrePartie
from damier import Damier
from random import randrange
from time import sleep

class Engine():

    #initialisation de l'arbre des possibilités
    def __init__(self):
        pass

    def print_damier(self, dic):
        return Damier().print_damier(dic)
    
    def print_dic_list(self, dic):
        for dictionnaire in dic:
            self.print_damier(dictionnaire)


    def piece_peut_se_deplacer_vers_modif(self, position_piece, position_cible, dic):
        #si la position est dans le damier et s'il y a une piece sur la case et si la position_cible n'est pas occupée
        if Damier().position_est_dans_damier(position_cible) and position_piece in dic and not position_cible in dic:

            if dic[position_piece].est_dame():
                if position_cible in position_piece.quatre_positions_diagonales():
                    return True
                else:

                    return False

            elif dic[position_piece].est_noire():
                if position_cible in position_piece.positions_diagonales_bas():
                    return True
                else:
                    return False
            elif dic[position_piece].est_blanche():
                if position_cible in position_piece.positions_diagonales_haut():
                    return True
                else:
                    return False
        else:
            return False

    def piece_peut_sauter_vers_modif(self, position_piece, position_cible, dic):
        #TODO: À tester - compléter
        position_piece_mange = position_piece.position_mange(position_cible)
        #s'il y a une piece à manger
        if position_piece_mange in dic:
            piece_mange = dic[position_piece_mange]
            # Si la position est dans le damier, s'il y a une pièce sur la case et si la position_cible est libre"            
            if Damier().position_est_dans_damier(position_cible) and position_piece in dic and not position_cible in dic:
                # Si la piece est adverse
                if position_piece_mange in dic and str(dic[position_piece]) != str(piece_mange):
                    return True
                else:
                    return False
            else:
                return False

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
            if self.piece_peut_se_deplacer_vers_modif(position_source, position_cible, dic):
                #si la pièce doit être promue
                if position_cible.cases_promotion():
                    nouveau_dic = dict(dic)
                    nouveau_dic[position_cible] = nouveau_dic[position_source].promouvoir()
                    del nouveau_dic[position_source]
                    list_dic.append(nouveau_dic)
                #sinon
                else:
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
            if self.piece_peut_sauter_vers_modif(position_source, position_cible, dic):
                #si pièce doit être promue
                if position_cible.cases_promotion():
                    nouveau_dic = dict(dic)
                    nouveau_dic[position_cible] = nouveau_dic[position_source].promouvoir()
                    del nouveau_dic[position_source]
                    #on supprime la pièce mangé
                    piece_mange = position_source.position_mange(position_cible)
                    del nouveau_dic[piece_mange]
                    list_dic.append(nouveau_dic)
                else:
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
            return list_dic, True
        else:
            #ajout des positions classique
            dic_classique = self.cases_jouable(position_source, dic)
            list_dic += dic_classique
            return list_dic, False
    
    def iteration_dic_noir(self, dic):
        dic_noir = self.dic_noir(dic)
        list_dic_saut = []
        list_dic = []
        for position in range(len(dic_noir)):
            #position_simple: toutes les positions des pièces noirs
            position_simple = list(dic_noir.keys())[position]
            #dic_position: toutes les dictionnaires associers aux déplacements d'une pièce (dans une liste)
            #saut: True si c'est un saut et False si déplacement simple
            dic_position, saut = self.dic_une_piece(position_simple, dic)
            if saut:
                for position_profonde in dic_position:
                    list_dic_saut.append(position_profonde)
            else:
                for position_profonde in dic_position:
                    list_dic.append(position_profonde)
        if list_dic_saut != []:
            return list_dic_saut
        else:
            return list_dic

    def iteration_dic_blanc(self, dic):
        dic_blanc = self.dic_blanc(dic)
        list_dic_saut = []
        list_dic = []
        for position in range(len(dic_blanc)):
            #position_simple: toutes les positions des pièces noirs
            position_simple = list(dic_blanc.keys())[position]
            #dic_position: toutes les dictionnaires associers aux déplacements d'une pièce (dans une liste)
            #saut: True si c'est un saut et False si déplacement simple
            dic_position, saut = self.dic_une_piece(position_simple, dic)
            if saut:
                for position_profonde in dic_position:
                    list_dic_saut.append(position_profonde)
            else:
                for position_profonde in dic_position:
                    list_dic.append(position_profonde)
        if list_dic_saut != []:
            return list_dic_saut
        else:
            return list_dic
    
    def debutant_noir(self, dic):
        list_dic = self.iteration_dic_noir(dic)
        numero_dic_choisit = randrange(len(list_dic))
        dic_choisit = list_dic[numero_dic_choisit]
        return dic_choisit

    def debutant_blanc(self, dic):
        list_dic = self.iteration_dic_blanc(dic)
        numero_dic_choisit = randrange(len(list_dic))
        dic_choisit = list_dic[numero_dic_choisit]
        return dic_choisit




dic = FenetrePartie().partie.damier.cases
Engine().print_damier(dic)

for i in range(40):
    dic = Engine().debutant_noir(dic)
    Engine().print_damier(dic)
    dic = Engine().debutant_blanc(dic)
    Engine().print_damier(dic)


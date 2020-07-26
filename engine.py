# Auteurs: Thierry Blais et Bernard Sévigny

from partie import Partie
from position import Position
from piece import Piece
from interface_dames import FenetrePartie
from damier import Damier
from canvas_damier import CanvasDamier
from random import randrange
from time import sleep
from copy import deepcopy


def print_damier(dic):
    """Affiche un damier.

    Args:
        dic (dict): Dictionnaire d'une position.

    Returns:
            (str): Représentation des pieces du damier.
    """
    return Damier().print_damier(dic)
    
def print_dic_list(list_dic):
    """Afficher une liste de damiers.
     Args:
        list_dic (list): Liste de plusieurs dictionnaires.
     Returns:
        (str): Représentation des damiers.
    """
    for dictionnaire in list_dic:
        print_damier(dictionnaire)


def piece_peut_se_deplacer_vers_modif(position_piece, position_cible, dic):
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
        dic (dict): Dictionnaire des positions.
    Returns:
        bool: True si la pièce peut se déplacer à la position cible, False autrement.
    """
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

def piece_peut_sauter_vers_modif(position_piece, position_cible, dic):
    """Cette méthode détermine si une pièce (à la position reçue) peut sauter vers une certaine position cible.
    On parle ici d'un déplacement qui "mange" une pièce adverse.
    Une pièce doit être positionnée à la position_piece reçue en argument (retourner False autrement).
    Une pièce ne peut que sauter de deux cases en diagonale. N'importe quel type de pièce (pion ou dame) peut sauter
    vers l'avant ou vers l'arrière. Une pièce ne peut pas sauter vers une case qui est déjà occupée par une autre
    pièce. Une pièce ne peut faire un saut que si elle saute par dessus une pièce de couleur adverse.
     Args:
        position_piece (Position): La position de la pièce source du saut.
        position_cible (Position): La position cible du saut.
        dic (dict): Dictionnaire des positions.
     Returns:
        bool: True si la pièce peut sauter vers la position cible, False autrement.
    """
    position_piece_mange = position_piece.position_mange(position_cible)
    #s'il y a une piece à manger
    if position_piece_mange in dic:
        piece_mange = dic[position_piece_mange]
        # Si la position est dans le damier, s'il y a une pièce sur la case et si la position_cible est libre"            
        if Damier().position_est_dans_damier(position_cible) and position_piece in dic and not position_cible in dic:
            # Si la piece est adverse
            if dic[position_piece].est_noire() and piece_mange.est_blanche():
                return True
            elif dic[position_piece].est_blanche() and piece_mange.est_noire():
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def dic_blanc(dic):
    """Permet de filtrer seulement les pièces blanches d'un dictionnaire.
    Args:
        dic (dict): Dictionnaire des positions.
    Returns:
        (dict): Dictionnaire des positions sans les pièces noires.
    """
    dic_blanc = {}
    for position, piece in dic.items():
        if piece.couleur == 'blanc':
            dic_blanc[position] = piece
    return dic_blanc

def dic_noir(dic):
    """Permet de filtrer seulement les pièces noires d'un dictionnaire.
    Args:
        dic (dict): Dictionnaire des positions.
    Returns:
        (dict): Dictionnaire des positions sans les pièces blanches.
    """
    dic_noir = {}
    for position, piece in dic.items():
        if piece.couleur == 'noir':
            dic_noir[position] = piece
    return dic_noir

#détermine les cases qu'une pièce peut jouer
#retourne la nouvelle position et la piece à supprimer
def cases_jouable(position_source, dic):
    """Détermine les déplacements classiques possibles.
     Args:
        position_source (dict): Clef et valeur d'une pièce.
        dic (dict): Dictionnaire des positions.
     Returns: 
        (list): Une liste de dictionnaire représentant les 
        positions possibles en déplacant la pièce en question.
    """
    #list des déplacement possible (dict)
    list_dic = []
    #si la piece peut faire un déplacement classique
    for position_cible in position_source.quatre_positions_diagonales():
        if piece_peut_se_deplacer_vers_modif(position_source, position_cible, dic):
            #si la pièce doit être promue
            if position_cible.cases_promotion():
                nouveau_dic = dict(dic)
                nouveau_dic[position_cible] = nouveau_dic[position_source]
                nouveau_dic[position_cible].promouvoir()
                del nouveau_dic[position_source]
                list_dic.append(nouveau_dic)
            #sinon
            else:
                nouveau_dic = dict(dic)
                nouveau_dic[position_cible] = nouveau_dic[position_source]
                del nouveau_dic[position_source]
                list_dic.append(nouveau_dic)
    return list_dic
def cases_jouable_saut(position_source, dic):
    """Détermine les sauts possibles.
    Args:
        position_source (dict): Clef et valeur d'une pièce.
        dic (dict): Dictionnaire des positions.
    Returns: 
        (list): Une liste de dictionnaires représentant
        les positions possibles en déplaçant la pièce en question.
    """
    #list des déplacement possible (dict)
    list_dic = []
    #si la piece peut faire un saut
    for position_cible in position_source.quatre_positions_sauts():
        if piece_peut_sauter_vers_modif(position_source, position_cible, dic):
            #si pièce doit être promue
            if position_cible.cases_promotion():
                nouveau_dic = dict(dic)
                nouveau_dic[position_cible] = nouveau_dic[position_source]
                nouveau_dic[position_cible].promouvoir()
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

def dic_une_piece(position_source, dic):
    """Détermine les déplacements et les sauts possibles.
    Args:
        position_source (dict): Clef et valeur d'une pièce.
        dic (dict): Dictionnaire des positions.
    Returns:
        (list), (bool): La liste des coups possibles, True si les coups
            sont des sauts et False s'ils sont des déplacements classiques.
    """
    list_dic = []
    # Ajout des sauts
    dic_saut = cases_jouable_saut(position_source, dic)
    if dic_saut != []:
        list_dic += dic_saut
        return list_dic, True
    else:
        # Ajout des positions classique
        dic_classique = cases_jouable(position_source, dic)
        list_dic += dic_classique
        return list_dic, False

def iteration_dic_noir(dic):
    """Détermine l'ensemble des coups possibles pour les noirs.
    Args:
        dic (dict): Dictionnaire des positions.
    Returns:
        (list), (int): Liste des coups possibles pour le joueur noir,
                       Point attribué à un saut.
    """
    dictionnaire_noir = dic_noir(dic)
    list_dic_saut = []
    list_dic = []
    for position in range(len(dictionnaire_noir)):
        #position_simple: toutes les positions des pièces noirs
        position_simple = list(dictionnaire_noir.keys())[position]
        #dic_position: toutes les dictionnaires associers aux déplacements d'une pièce (dans une liste)
        #saut: True si c'est un saut et False si déplacement simple
        dic_position, saut = dic_une_piece(position_simple, dic)
        if saut:
            for position_profonde in dic_position:
                list_dic_saut.append(position_profonde)
        else:
            for position_profonde in dic_position:
                list_dic.append(position_profonde)
    if list_dic_saut != []:
        return list_dic_saut, 1
    else:
        return list_dic, 0
def iteration_dic_blanc(dic):
    """Détermine l'assemble des coups possibles pour les blancs.
    Args:
        dic (dict): Distionnaire des positions.
    Returns:
        (list), (int): Liste des coups possiblent pour le joueur blanc,
            Point attribué à un saut.
    """
    dictionnaire_blanc = dic_blanc(dic)
    list_dic_saut = []
    list_dic = []
    for position in range(len(dictionnaire_blanc)):
        #position_simple: toutes les positions des pièces noirs
        position_simple = list(dictionnaire_blanc.keys())[position]
        #dic_position: toutes les dictionnaires associers aux déplacements d'une pièce (dans une liste)
        #saut: True si c'est un saut et False si déplacement simple
        dic_position, saut = dic_une_piece(position_simple, dic)
        if saut:
            for position_profonde in dic_position:
                list_dic_saut.append(position_profonde)
        else:
            for position_profonde in dic_position:
                list_dic.append(position_profonde)
    if list_dic_saut != []:
        return list_dic_saut, 1
    else:
        return list_dic, 0

def debutant_noir(dic):
    """Détermine un coup aléatoire pour le joueur noir.
    Args:
        dic (dict): Dictionnaire de la position.
    Returns:
        (dict): Un coup aléatoire et légale.
    """
    list_dic, saut = iteration_dic_noir(dic)
    numero_dic_choisit = randrange(len(list_dic))
    dic_choisit = list_dic[numero_dic_choisit]
    return dic_choisit

def debutant_blanc(dic):
    """Détermine un coup aléatoire pour le joueur blanc.
    Args:
        dic (dict): Dictionnaire de la position.
    Returns:
        (dict): Un coup aléatoire et légale.
    """
    list_dic, saut = iteration_dic_blanc(dic)
    numero_dic_choisit = randrange(len(list_dic))
    dic_choisit = list_dic[numero_dic_choisit]
    return dic_choisit
  
def avance_une_prise(dic):
    """Détermine quatre coups à l'avance le nombre de points des noirs.
        La méthode choisit le coup qui maximise les points des noirs.
    Args:
        dic (dict): Dictionnaire des positions.
    Returns:
        (dict): Le coup choisi par le programme.
    """
    score_max = 0
    position_choisit = None
    list_dic, point = iteration_dic_noir(dic)
    list_dic1 = deepcopy(list_dic)
    for dictionnaire in range(len(list_dic1)):
        deuxieme_list_dic, deuxieme_point = iteration_dic_blanc(list_dic1[dictionnaire])
        deuxieme_list_dic2 = deepcopy(deuxieme_list_dic)
        for deuxieme_dictionnaire in deuxieme_list_dic2:
            troisieme_list_dic, troisieme_point = iteration_dic_noir(deuxieme_dictionnaire)
            troisieme_list_dic2 = deepcopy(troisieme_list_dic)
            for troisieme_dictionnaire in troisieme_list_dic2:
                quatrieme_list_dic, quatrieme_point = iteration_dic_blanc(troisieme_dictionnaire)
                quatrieme_list_dic2 = deepcopy(quatrieme_list_dic)
                for quatrieme_dicionnaire in quatrieme_list_dic2:
                    cinquieme_list_dic, cinquieme_point = iteration_dic_noir(quatrieme_dicionnaire)
                    score = point - deuxieme_point + troisieme_point - quatrieme_point + cinquieme_point
                    if score > score_max:
                        score_max = score
                        position_choisit = list_dic[dictionnaire]
    if position_choisit == None:
        numero_dic_choisit = randrange(len(list_dic))
        position_choisit = list_dic[numero_dic_choisit]
    return position_choisit
  
def avance_blanc(dic):
    """Détermine quatre coups à l'avance le nombre de points des blancs.
        La méthode choisit le coup qui maximise les points des blancs.
    Args:
        dic (dict): Dictionnaire des positions.
          
    Returns:
        (dict): Le coup choisi par le programme.
    """
    score_max = 0
    position_choisit = None
    list_dic, point = iteration_dic_blanc(dic)
    list_dic1 = deepcopy(list_dic)
    for dictionnaire in range(len(list_dic1)):
        deuxieme_list_dic, deuxieme_point = iteration_dic_noir(list_dic1[dictionnaire])
        deuxieme_list_dic2 = deepcopy(deuxieme_list_dic)
        for deuxieme_dictionnaire in deuxieme_list_dic2:
            troisieme_list_dic, troisieme_point = iteration_dic_blanc(deuxieme_dictionnaire)
            troisieme_list_dic2 = deepcopy(troisieme_list_dic)
            for troisieme_dictionnaire in troisieme_list_dic2:
                quatrieme_list_dic, quatrieme_point = iteration_dic_noir(troisieme_dictionnaire)
                quatrieme_list_dic2 = deepcopy(quatrieme_list_dic)
                for quatrieme_dicionnaire2 in quatrieme_list_dic2:
                    cinquieme_list_dic, cinquieme_point = iteration_dic_blanc(quatrieme_dicionnaire2)
                    score = point - deuxieme_point + troisieme_point - quatrieme_point + cinquieme_point
                    if score > score_max:
                        score_max = score
                        position_choisit = list_dic[dictionnaire]
    if position_choisit == None:
        numero_dic_choisit = randrange(len(list_dic))
        position_choisit = list_dic[numero_dic_choisit]
    return position_choisit


def avance(dic):
    """La méthode permet plusieurs prise par l'engine noir.
    Args:
        dic (dict): Dictionnaire des positions.
    Returns:
        (dict): Solution de l'engine qui prend en compte les prises multiples.
    """
    print("a-366")
    prise = True
    while prise:
        dic_base = deepcopy(dic)
        dic = avance_une_prise(dic)
        # S'il y a une pièce de moins
        if len(dic) < len(dic_base):
            piece_bouge = list(dic.keys() - dic_base.keys())[0]
            #Est-ce que la piece qui bouge peut manger
            dictionnaire_une_piece, saut = dic_une_piece(piece_bouge, dic)
            # si oui, la boucle recommence
            prise = saut
        else:
            prise = False
    return dic



if __name__ == "__main__":
    dic = FenetrePartie().partie.damier.cases
    print_damier(dic)

    for i in range(1000):
        dic = avance(dic)
        print('coup noir')
        print_damier(dic)
        dic = avance_blanc(dic)
        print('coup blanc')
        print_damier(dic)
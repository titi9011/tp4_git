from damier import Damier
import damier

class Test:

    def __init__(self):
        """Constructeur de la classe Partie. Initialise les attributs à leur valeur par défaut. Le damier est construit
        avec les pièces à leur valeur initiale. Aucune position source n'est sélectionnée, et aucune position source n'est forcée.

        """
        self.damier = Damier()
    print("damier :", damier)
    print("Damier :", Damier())
    posS = "Position(5, 0)"
    posC = "Position(4, 1)"

    s = 1  # damier.Damier.deplacer(posS, posC)
    print(s)
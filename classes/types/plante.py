from classes.pokemon import *

class Plante(Pokemon):
    def __init__(self, nom, niveau, type2 = "Nul", evol = []):
        super().__init__(nom, niveau, type2, evol)
        self.type[0] = "Plante"
        self.setDefense(1)
        self.setAttaque(12)
        self.setPvMax(115)
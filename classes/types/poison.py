from classes.pokemon import *


class Poison(Pokemon):
    def __init__(self, nom, niveau, type2 = "Nul", evol = []):
        super().__init__(nom, niveau, type2, evol)
        self.type[0] = "Feu"
        self.setDefense(1)
        self.setAttaque(15)
        self.setPvMax(80)
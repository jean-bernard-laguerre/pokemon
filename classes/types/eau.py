from classes.pokemon import *


class Eau(Pokemon):
    def __init__(self, nom, niveau, type2 = "Nul", evol = []):
        super().__init__(nom, niveau, type2, evol)
        self.type[0] = "Eau"
        self.setPvMax(125)
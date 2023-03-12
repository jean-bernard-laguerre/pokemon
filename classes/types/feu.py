from classes.pokemon import *

class Feu(Pokemon):
    def __init__(self, nom, niveau, type2 = "Nul", evol = []):
        super().__init__(nom, niveau, type2, evol)
        self.type[0] = "Feu"
        self.setAttaque(15)

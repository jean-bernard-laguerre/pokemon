from classes.pokemon import *

class Normal(Pokemon):
    def __init__(self, nom, niveau, type2 = "Nul", evol = []):
        super().__init__(nom, niveau, type2, evol)
        self.type[0] = "Normal"
        self.setAttaque(12)
        self.setDefense(2)
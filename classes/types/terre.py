from classes.pokemon import *

class Terre(Pokemon):
    def __init__(self, nom, niveau, type2 = "Nul", evol = []):
        super().__init__(nom, niveau, type2, evol)
        self.type[0] = "Terre"
        self.setDefense(8)


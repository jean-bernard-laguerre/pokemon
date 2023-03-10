class Pokemon:
    def __init__(self, nom, niveau, type2 = "Nul", evol = []):
        
        self.__pv = 100
        self.__pvMax = self.__pv
        self.__nom = nom
        self.niveau = niveau
        self.type = ["Nul", type2]
        self.__attaque = 10
        self.__defense = 5
        self.evolution = [nom] + evol
        self.forme = 0

    def getPv(self):
        return self.__pv
    def setPv(self, pv):
        if pv < 0:
            self.__pv = 0
        else:
            self.__pv = pv

    def getPvMax(self):
        return self.__pvMax
    def setPvMax(self, pv):
        self.__pvMax = pv
        self.__pv = pv

    def getNom(self):
        return self.__nom
    def getNiveau(self):
        return self.niveau
    
    def getAttaque(self):
        return self.__attaque
    def setAttaque(self, atk):
        self.__attaque = atk

    def getDefense(self):
        return self.__defense
    def setDefense(self, dfs):
        self.__defense = dfs

    def afficherInfos(self):
        print(f"Nom: {self.__nom}")
        print(f"Type: {self.type}")
        print(f"Niveau: {self.niveau}")
        print(f"PV: {self.__pv}")
        print(f"Attaque: {self.__attaque}")
        print(f"Defense: {self.__defense}")

    def evoluer(self):
        if len(self.evolution) > 1 and self.forme < len(self.evolution)-1:

            self.__nom = self.evolution[self.forme + 1]
            self.forme += 1 
            self.__attaque += 4
            self.__defense += 4

class Feu(Pokemon):
    def __init__(self, nom, niveau, type2 = "Nul", evol = []):
        super().__init__(nom, niveau, type2, evol)
        self.type[0] = "Feu"
        self.setAttaque(15)


class Eau(Pokemon):
    def __init__(self, nom, niveau, type2 = "Nul", evol = []):
        super().__init__(nom, niveau, type2, evol)
        self.type[0] = "Eau"
        self.setPvMax(125)


class Terre(Pokemon):
    def __init__(self, nom, niveau, type2 = "Nul", evol = []):
        super().__init__(nom, niveau, type2, evol)
        self.type[0] = "Terre"
        self.setDefense(8)


class Plante(Pokemon):
    def __init__(self, nom, niveau, type2 = "Nul", evol = []):
        super().__init__(nom, niveau, type2, evol)
        self.type[0] = "Plante"
        self.setDefense(1)
        self.setAttaque(12)
        self.setPvMax(115)


class Normal(Pokemon):
    def __init__(self, nom, niveau, type2 = "Nul", evol = []):
        super().__init__(nom, niveau, type2, evol)
        self.type[0] = "Normal"
        self.setAttaque(12)
        self.setDefense(2)
    

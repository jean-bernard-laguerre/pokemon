import random
import json
from classes.pokemon import *
from outils.variable import *
from outils.outils import *

class Combat:
    def __init__(self, joueur):
        self.joueur = joueur
        self.adversaire = recup_pokemon()


    def statut(self, pokemon):
        if pokemon.getPv() == 0:
            return False
        return True
    
    def attaquer(self, auteur, cible):
        coup = random.choice([0,1])
        if coup == 1:
            degats = (10 + (auteur.getAttaque() - cible.getDefense())) * (TABLE[id_types[cible.type[0]]][id_types[auteur.type[0]]] * TABLE[id_types[cible.type[1]]][id_types[auteur.type[1]]])
            cible.setPv(cible.getPv() - (int(degats)))
            return True
        return False
    
    def perdant(self):
        pass

    #Ajoute le pokemon dans pokedex.json
    def enregistrer(self, pokemon):

        f = open("outils\pokedex.json", "r+")
        pokedex = json.load(f)

        if pokemon.getNom() not in pokedex:

            pokedex[pokemon.getNom()] = {"Nom": pokemon.getNom(),
                                         "Type": pokemon.type,
                                         "Niveau": pokemon.getNiveau(),
                                         "Evolutions":pokemon.evolution,
                                         "Attaque": pokemon.getAttaque(),
                                         "Defense": pokemon.getDefense()}

        f.seek(0)
        json.dump(pokedex, f, indent=4)

        f.close()

    def tour(self):

        for i in range(2):
            
            if i == 0:
                self.attaquer(self.joueur, self.adversaire)
            else:
                self.attaquer(self.adversaire, self.joueur)

            if (not self.statut(self.joueur)) or (not self.statut(self.adversaire)):
                self.enregistrer(self.adversaire)
                self.enregistrer(self.joueur)
                return True



        
            

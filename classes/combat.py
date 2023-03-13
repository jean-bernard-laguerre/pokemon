import random
import json
from classes.pokemon import *
from outils.variable import *
from outils.outils import *

class Combat:
    def __init__(self, joueur):
        self.joueur = joueur
        self.adversaire = recup_pokemon()

    #Retourne False si un pokemon est KO
    def statut(self, pokemon):
        if pokemon.getPv() == 0:
            return False
        return True
    
    #Attaque un pokemon 
    def attaquer(self, auteur, cible):
        #Si coup est egal a 1 le coup reussi
        coup = random.choice([0,1])
        if coup == 1:
            #Les degats sont multiplié par les resistances de la cible au type de l'auteur de l'attaque
            degats = (10 + (auteur.getAttaque() - cible.getDefense())) * (TABLE[id_types[cible.type[0]]][id_types[auteur.type[0]]] * TABLE[id_types[cible.type[1]]][id_types[auteur.type[1]]])
            cible.setPv(cible.getPv() - (int(degats)))
            return True
        print("Raté...")
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

    #Tour du combat
    def tour(self):

        #Les pokemons s'attaquent chacun leur tours
        for i in range(2):
            
            if i == 0:
                self.attaquer(self.joueur, self.adversaire)
            else:
                self.attaquer(self.adversaire, self.joueur)

            if (not self.statut(self.joueur)) or (not self.statut(self.adversaire)):
                self.enregistrer(self.adversaire)
                self.enregistrer(self.joueur)
                return True
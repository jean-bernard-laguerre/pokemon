import json 
import random
from classes.pokemon import *

def recup_pokemon(nom = ""):

    f = open("outils\pokemon.json")
    pokemons = json.load(f)


    if nom == "":    
        pokemon = pokemons[random.choice(list(pokemons))]
    else:
        pokemon = pokemons[nom]

    match pokemon["Type"][0]:
        case "Feu":
            return Feu(pokemon["Nom"], pokemon["Niveau"], pokemon["Type"][1], pokemon["Evolutions"][1:])
        case "Eau":
            return Eau(pokemon["Nom"], pokemon["Niveau"], pokemon["Type"][1], pokemon["Evolutions"][1:])
        case "Terre":
            return Terre(pokemon["Nom"], pokemon["Niveau"], pokemon["Type"][1], pokemon["Evolutions"][1:])
        case "Plante":
            return Plante(pokemon["Nom"], pokemon["Niveau"], pokemon["Type"][1], pokemon["Evolutions"][1:])
        case "Normal":
            return Normal(pokemon["Nom"], pokemon["Niveau"], pokemon["Type"][1], pokemon["Evolutions"][1:])
        
def recup_pokedex():
    f = open("outils\pokedex.json")
    pokedex = json.load(f)
    f.close()
    return pokedex

def reset_pokedex():
    pass
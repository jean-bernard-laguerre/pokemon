import json 
import random
from classes.types.eau import *
from classes.types.feu import *
from classes.types.terre import *
from classes.types.normal import *
from classes.types.plante import *

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
    f = open("outils\pokedex.json", "r+")
    f.truncate(0)
    json.dump({}, f, indent=4)

    f.close()
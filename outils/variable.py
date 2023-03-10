from classes.pokemon import *

#Types

id_types = {"Nul" : 0,
            "Eau": 1,
            "Feu": 2,
            "Terre": 3,
            "Normal": 4,
            "Plante": 5,
            "Poison": 6}

TABLE = [   [1, 1, 1, 1, 1, 1, 1],
            [1, 1, .5, .5, 1, 2, 1],
            [1, 2, 1, 2, 1, .5, 1],
            [1, 2, .5, 1, 1, 2, 1],
            [1, .75, .75, .75, 1, .75, .75], 
            [1, .5, 2, .5, .1, .5, 2],
            [1, 1, 2, 1, 1, .5, .5]]

#Pokemon
evoli = Normal("Evoli", 10, evol=["Pyroli"])
carapuce = Eau("Carapuce", 10, evol=["Carabaffe", "Tortank"])
bulbizarre = Plante("Bulbizarre", 10, "Poison", ["Herbizarre", "Florizarre"])
salameche = Feu("Salameche", 10, evol=["Reptincel", "Dracaufeu"])
racaillou = Terre("Racaillou", 10, evol=["Gravalanche", "Grolem"])
volcanion = Feu("Volcanion", 10, "Eau")

liste_Pokemon = [evoli, carapuce, salameche, racaillou, bulbizarre, volcanion]
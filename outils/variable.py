from classes.pokemon import *

#Types

id_types = {"Nul" : 0,
            "Eau": 1,
            "Feu": 2,
            "Terre": 3,
            "Normal": 4,
            "Plante": 5,
            "Poison": 6}

#Tableau de resistance
TABLE = [   [1, 1, 1, 1, 1, 1, 1],
            [1, 1, .5, .5, 1, 2, 1],
            [1, 2, 1, 2, 1, .5, 1],
            [1, 2, .5, 1, 1, 2, 1],
            [1, .75, .75, .75, 1, .75, .75], 
            [1, .5, 2, .5, .1, .5, 2],
            [1, 1, 2, 1, 1, .5, .5]]

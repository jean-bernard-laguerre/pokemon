from classes.combat import *
from classes.pokemon import *
from classes.bouton import *
from outils.variable import *
import pygame

options = ["Salameche", "Carapuce", "Bulbizarre"]
pygame.init()

page = 0
index = 0
clique = False

fenetre = pygame.display.set_mode((800, 600))
tdr = pygame.time.Clock()

police_pokemon = pygame.font.Font("polices\PKMN RBYGSC.ttf", 16)

def menu():
    global combat
    for i,option in enumerate(options):
        
        if Bouton(option, 200+(i*200), 300, police_pokemon, "black").affichage(fenetre):
            poke = recup_pokemon(option)
            combat = Combat(poke)
            nav(1)

    if Bouton("Pokedex", 400, 500, police_pokemon, "black").affichage(fenetre):
            nav(2)
        

def afficher_combat():
    global clique

    nom_joueur = police_pokemon.render(f"{combat.joueur.getNom()}", 1, "black")
    nom_adversaire = police_pokemon.render(f"{combat.adversaire.getNom()}", 1, "black")

    nv_joueur = police_pokemon.render(f"Nv:{(combat.joueur.getNiveau())}", 1, "black")
    nv_adversaire = police_pokemon.render(f"Nv:{combat.adversaire.getNiveau()}", 1, "black")

    fenetre.blit(nom_joueur, (170, 450))
    fenetre.blit(nom_adversaire, (620, 100))

    fenetre.blit(nv_joueur, (100, 450))
    fenetre.blit(nv_adversaire, (550, 100))
    
    barre(combat.joueur.getPv(), combat.joueur.getPvMax(), 100, 480)
    barre(combat.adversaire.getPv(), combat.adversaire.getPvMax(), 550, 130)

    if Bouton("Attaque", 150, 510, police_pokemon, "black").affichage(fenetre) and not clique:
        clique = True
        if combat.tour():
            nav(3)

    if Bouton("Evoluer", 150, 550, police_pokemon, "black").affichage(fenetre) and not clique:
        clique = True
        combat.joueur.evoluer()


def affiche_pokedex():
    global index, clique

    pokedex = recup_pokedex()

    if len(list(pokedex)) > 0:

        pokemon = pokedex[list(pokedex)[index]]
        nom_pokedex = police_pokemon.render(f"Nom: {pokemon['Nom']}", 1, "black")
        type_pokedex = police_pokemon.render(f"Type: {pokemon['Type'][0]}", 1, "black")
        if pokemon["Type"][1] != "Nul":
            type_pokedex = police_pokemon.render(f"Type: {pokemon['Type'][0]} / {pokemon['Type'][1]}", 1, "black")
        att_pokedex = police_pokemon.render(f"Attaque: {pokemon['Attaque']}", 1, "black")
        def_pokedex = police_pokemon.render(f"Defense: {pokemon['Defense']}", 1, "black")

        fenetre.blit(nom_pokedex, (325, 180))
        fenetre.blit(type_pokedex, (325, 220))
        fenetre.blit(att_pokedex, (325, 260))
        fenetre.blit(def_pokedex, (325, 300))

        if index < len(list(pokedex))-1:
            if Bouton("Suivant", 700, 300, police_pokemon, "black").affichage(fenetre) and not clique:
                clique = True
                index += 1

        if index >= 1:
            if Bouton("Precedent", 100, 300, police_pokemon, "black").affichage(fenetre) and not clique:
                clique = True
                index -= 1

    else :
        fenetre.blit(police_pokemon.render("Pokedex vide", 1, "black"), (325, 300))

    if Bouton("Menu", 650, 500, police_pokemon, "black").affichage(fenetre):
        nav(0)


def ecran_fin():

    if combat.adversaire.getPv() == 0:
        vainqueur = combat.joueur.getNom()
    else:
        vainqueur = combat.adversaire.getNom()

    lbl_vainqueur = police_pokemon.render(f"{vainqueur} a remporté le combat", 1, "black")

    fenetre.blit(lbl_vainqueur, (400-(lbl_vainqueur.get_rect().w/2), 300))

    if Bouton("Menu", 650, 500, police_pokemon, "black").affichage(fenetre):
        nav(0)


#Barre de vie
def barre(pv, pvMax, x, y):

    frame = pygame.Rect(x, y, 150, 10)
    progres = pygame.Rect(x, y, int(pv*(150/pvMax)), 10)
        
    pygame.draw.rect(fenetre, 'aquamarine3', progres)
    pygame.draw.rect(fenetre, 'black', frame, 2)


def nav(id):
    global page
    page = id


#Boucle principale
en_cours = True
while en_cours:

    tdr.tick(30) / 10000
    fenetre.fill((255,255,255))
    match page:
        case 0:
            menu()
        case 1:
            afficher_combat()
        case 2:
            affiche_pokedex()
        case 3:
            ecran_fin()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        if event.type == pygame.MOUSEBUTTONUP:
            clique = False

    pygame.display.update()

pygame.quit()
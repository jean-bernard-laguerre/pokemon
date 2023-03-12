from classes.combat import *
from classes.types.eau import *
from classes.types.feu import *
from classes.types.terre import *
from classes.types.normal import *
from classes.types.plante import *
from classes.bouton import *
from outils.variable import *
import pygame

options = ["Salameche", "Carapuce", "Bulbizarre"]
pygame.init()

page = 0
index = 0
clique = False

fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pokemon")
tdr = pygame.time.Clock()

police_pokemon = pygame.font.Font("polices\PKMN RBYGSC.ttf", 16)

menu_bg = pygame.image.load("images\menu_bg.jpg")

combat_bg = pygame.image.load("images\d9spuwer2c491.png")
combat_bg_rect = combat_bg.get_rect()


def menu():
    global combat

    fenetre.blit(menu_bg, menu_bg.get_rect())

    for i,option in enumerate(options):

        pk_image = pygame.image.load(f"images\{option}_face.png")
        fenetre.blit(pk_image, (160+(i*200), 230), pk_image.get_rect())
        
        if Bouton(option, 200+(i*200), 300, police_pokemon, "white").affichage(fenetre):
            poke = recup_pokemon(option)
            combat = Combat(poke)
            nav(1)

    if Bouton("Pokedex", 400, 500, police_pokemon, "white").affichage(fenetre):
            nav(2)

    if Bouton("Reset", 200, 500, police_pokemon, "white").affichage(fenetre):
            reset_pokedex()
        

def afficher_combat():
    global clique

    nom_joueur = police_pokemon.render(f"{combat.joueur.getNom()}", 1, "white")
    nom_adversaire = police_pokemon.render(f"{combat.adversaire.getNom()}", 1, "white")

    nv_joueur = police_pokemon.render(f"Nv:{(combat.joueur.getNiveau())}", 1, "white")
    nv_adversaire = police_pokemon.render(f"Nv:{combat.adversaire.getNiveau()}", 1, "white")

    try:
        image_pk_face = pygame.image.load(f"images\{combat.adversaire.getNom()}_face.png")
        image_pk_dos = pygame.image.load(f"images\{combat.joueur.getNom()}_dos.png")
    except:
        image_pk_face = pygame.image.load(f"images\Salameche_face.png")
        image_pk_dos = pygame.image.load(f"images\Salameche_dos.png")

    fenetre.blit(combat_bg, combat_bg_rect)

    fenetre.blit(image_pk_dos, (200, 380), image_pk_dos.get_rect())
    fenetre.blit(image_pk_face, (500, 250), image_pk_face.get_rect())

    fenetre.blit(nom_joueur, (170, 450))
    fenetre.blit(nom_adversaire, (620, 100))

    fenetre.blit(nv_joueur, (100, 450))
    fenetre.blit(nv_adversaire, (550, 100))
    
    barre(combat.joueur.getPv(), combat.joueur.getPvMax(), 100, 480)
    barre(combat.adversaire.getPv(), combat.adversaire.getPvMax(), 550, 130)

    if Bouton("Attaque", 150, 510, police_pokemon, "white").affichage(fenetre) and not clique:
        clique = True
        if combat.tour():
            nav(3)

    if Bouton("Evoluer", 150, 550, police_pokemon, "white").affichage(fenetre) and not clique:
        clique = True
        combat.joueur.evoluer()


def affiche_pokedex():
    global index, clique

    fenetre.blit(menu_bg, menu_bg.get_rect())
    pokedex = recup_pokedex()

    if len(list(pokedex)) > 0:

        pokemon = pokedex[list(pokedex)[index]]
        pk_image = pygame.image.load(f"images\{pokemon['Nom']}_face.png")
        nom_pokedex = police_pokemon.render(f"Nom: {pokemon['Nom']}", 1, "white")
        type_pokedex = police_pokemon.render(f"Type: {pokemon['Type'][0]}", 1, "white")
        if pokemon["Type"][1] != "Nul":
            type_pokedex = police_pokemon.render(f"Type: {pokemon['Type'][0]} / {pokemon['Type'][1]}", 1, "white")
        att_pokedex = police_pokemon.render(f"Attaque: {pokemon['Attaque']}", 1, "white")
        def_pokedex = police_pokemon.render(f"Defense: {pokemon['Defense']}", 1, "white")
        
        fenetre.blit(pk_image, (350, 150), pk_image.get_rect())
        fenetre.blit(nom_pokedex, (325, 230))
        fenetre.blit(type_pokedex, (325, 270))
        fenetre.blit(att_pokedex, (325, 310))
        fenetre.blit(def_pokedex, (325, 350))

        if index < len(list(pokedex))-1:
            if Bouton("Suivant", 700, 300, police_pokemon, "white").affichage(fenetre) and not clique:
                clique = True
                index += 1

        if index >= 1:
            if Bouton("Precedent", 100, 300, police_pokemon, "white").affichage(fenetre) and not clique:
                clique = True
                index -= 1

    else :
        fenetre.blit(police_pokemon.render("Pokedex vide", 1, "white"), (325, 300))

    if Bouton("Menu", 650, 500, police_pokemon, "white").affichage(fenetre):
        nav(0)


def ecran_fin():

    fenetre.blit(menu_bg, menu_bg.get_rect())

    if combat.adversaire.getPv() == 0:
        vainqueur = combat.joueur.getNom()
    else:
        vainqueur = combat.adversaire.getNom()

    lbl_vainqueur = police_pokemon.render(f"{vainqueur} a remporté le combat", 1, "white")

    fenetre.blit(lbl_vainqueur, (400-(lbl_vainqueur.get_rect().w/2), 300))

    if Bouton("Menu", 650, 500, police_pokemon, "white").affichage(fenetre):
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
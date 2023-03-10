import pygame

class Bouton():
    def __init__(self, message, x, y, police, couleur):
        self.texte = police.render(message, 1, couleur)
        self.rect = self.texte.get_rect()
        self.rect.topleft = (x-self.rect.w/2, y)
        self.rect.w = self.texte.get_width()+20
        self.rect.h = self.texte.get_height()+20

    #Affiche le bouton retourne True lorsque l'on clique a l'interieur
    def affichage(self, surface):
        
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):

            if (pygame.mouse.get_pressed()[0] == 1):
                action = True

        surface.blit(self.texte, ( self.rect.x, self.rect.y))

        return action
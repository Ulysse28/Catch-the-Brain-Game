import pygame
import random
import math
from game import Game


#initialisation du module pygame
pygame.init()


#générer le fentre de jeu
pygame.display.set_caption("Catch the Circle")
screen = pygame.display.set_mode((1080, 600))

#importer le fond
background = pygame.image.load('Images/fond.jpg')
background = pygame.transform.scale(background, (1080, 600))




#importer l'image pour cacher le cercle
cache = pygame.image.load('square.png')

#importer l'image pour cacher le cerveau
cache2 = pygame.image.load('square.png')


#importer le cerveau
clue = pygame.image.load('anxiety.png')


#importer le bouton level 1

level_1_button = pygame.image.load('Images/one.png')
level_1_button_rect = level_1_button.get_rect()
level_1_button_rect.x = math.ceil(screen.get_width() / 2.2)
level_1_button_rect.y = math.ceil(screen.get_height() / 2.2)

#importer le boutton level 2

level_2_button = pygame.image.load('Images/two.png')
level_2_button_rect = level_2_button.get_rect()
level_2_button_rect.x = math.ceil(screen.get_width() / 2.2)
level_2_button_rect.y = math.ceil(screen.get_height() / 1.7)


game = Game()

#boucle du jeu
running = True

while running:

    screen.blit(background, (0, 0))

    #ecran d'accueil ou de jeu

    if game.first_level:
        game.update(screen)
    elif game.second_level:
        game.update2(screen)
    else:

        screen.blit(level_1_button, (level_1_button_rect))
        screen.blit(level_2_button, (level_2_button_rect))


    pygame.display.flip()

    #evenements de pygame
    for event in pygame.event.get():
        #si le joueur ferme la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")


        #si le joueur appuie sur la souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score = 0
            if game.white.rect.collidepoint(event.pos):


                game.white.more_points()

                #cache le cerveau
                screen.blit(cache, (game.white.rect.x, game.white.rect.y))

                #nouvelles coordonnées du cercles
                game.white.rect.x = game.circle.rect.x
                game.white.rect.y = game.circle.rect.y

                #cache le cerveau
                screen.blit(cache2, (game.white.rect) )

                #nouvelles coordonnées du cerveaux
                game.circle.rect.x = random.randint(0, 1000)
                game.circle.rect.y = random.randint(0, 500)



            if level_1_button_rect.collidepoint(event.pos):
                    game.level1()
                    screen.blit(cache,(level_1_button_rect))
                    screen.blit(cache,(level_2_button_rect ))

            elif level_2_button_rect.collidepoint(event.pos):
                    game.level2()
                    screen.blit(cache, (level_1_button_rect))
                    screen.blit(cache, (level_2_button_rect))

    if game.white.score > 50:
        #game.welcome = True
        game.first_level = False
        game.second_level = False















import math
import time

import pygame
from sys import exit

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('Runner')
    clock = pygame.time.Clock()
    test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
    sky_surface = pygame.image.load('graphics/Sky.png')
    ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
    score_surf = test_font.render('My game', False, (64,64,64)).convert_alpha()
    score_rect = score_surf.get_rect(center = (400, 50))

    player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()

    player_rect = player_surf.get_rect(midbottom = (80, 300))
    snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
    snail_rect = snail_surface.get_rect(midbottom = (160, 300))
    player_y_pos = 300
    player_gravity = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               exit()
            screen.blit(sky_surface, (0,0))
            screen.blit(ground_surface, (0,300))
            pygame.draw.rect(screen, "#c0e8ec", score_rect)
            pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
            screen.blit(score_surf, score_rect)
            if snail_rect.right < 0: snail_rect.left = 800
            screen.blit(snail_surface, snail_rect)
            snail_rect.left -= 3

            mouse_pos = pygame.mouse.get_pos()
            if player_rect.collidepoint(mouse_pos):
                print(pygame.mouse.get_pressed())
            if event.type == pygame.MOUSEMOTION:
                if player_rect.collidepoint(event.pos):
                    print("col")
            keys = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_y_pos = 100
                    print("jump")

            #if event.type == pygame.KEYUP:
            #    print("key up")
        while player_y_pos < 300:
            if player_y_pos < 250:
                player_y_pos += 10
                time.sleep(0.2)
                #time.sleep(1)
            elif player_y_pos < 200:
                player_y_pos += 20
                time.sleep(0.1)

            else:
                player_y_pos = 300
            pygame.display.update()
            screen.blit(player_surf, player_surf.get_rect(midbottom=(80, player_y_pos)))



        pygame.display.update()
        screen.blit(player_surf, player_surf.get_rect(midbottom = (80, player_y_pos)))

        clock.tick(60)

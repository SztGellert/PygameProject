import math
import time

import pygame
from sys import exit

def display_score(score: int):
    score_surf = test_font.render(f'Score: {score}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)


if __name__ == '__main__':
    game_active = True
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('Runner')
    clock = pygame.time.Clock()
    test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
    sky_surface = pygame.image.load('graphics/Sky.png')
    ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
    player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
    start_time = 0
    player_rect = player_surf.get_rect(midbottom = (80, 300))
    snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
    snail_rect = snail_surface.get_rect(midbottom = (160, 300))

    player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
    player_stand = pygame.transform.rotozoom(player_stand, 0 ,2 )
    player_stand_rect = player_stand.get_rect(center = (400, 200))

    game_name= test_font.render('Pixel Runner', False, (111,196,169))
    game_name_rect = game_name.get_rect(center = (400, 80))



    player_gravity = 0
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               exit()
            if game_active:
                mouse_pos = pygame.mouse.get_pos()
                if player_rect.collidepoint(mouse_pos):
                    print(pygame.mouse.get_pressed())
                if event.type == pygame.MOUSEMOTION:
                    if player_rect.collidepoint(event.pos):
                        print("col")
                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                        player_gravity = -20
                        score+=1

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        score = 0

                        game_active = True
                        snail_rect.right=800
                        start_time =  int(pygame.time.get_ticks() / 1000)
        if game_active:

            screen.blit(sky_surface, (0,0))
            screen.blit(ground_surface, (0,300))
            display_score(score)
            if snail_rect.right < 0: snail_rect.left = 800
            screen.blit(snail_surface, snail_rect)
            snail_rect.left -= 3
            player_gravity += 1
            player_rect.y += player_gravity
            if player_rect.bottom >= 300:
                player_rect.bottom = 300
            screen.blit(player_surf, player_rect)

            if snail_rect.colliderect(player_rect):
                game_active = False

        else:
            screen.fill((94,129,162))
            if score != 0:
                score_surf = test_font.render(f'Score: {score}', False, (64, 64, 64))
                score_rect = score_surf.get_rect(center=(400, 50))
                screen.blit(score_surf, score_rect)
            screen.blit(game_name, game_name_rect)
            screen.blit(player_stand, player_stand_rect)

        pygame.display.update()

        clock.tick(60)

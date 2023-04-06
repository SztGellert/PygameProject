import math
import random
import time

import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def collision(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []


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
    player_rect = player_surf.get_rect(midbottom=(80, 300))
    snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
    fly_surf = pygame.image.load('graphics/fly/fly1.png').convert_alpha()

    player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
    player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
    player_stand_rect = player_stand.get_rect(center=(400, 200))

    game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
    game_name_rect = game_name.get_rect(center=(400, 80))

    game_msg = test_font.render('Press space to run', False, (111, 196, 169))
    game_msg_rect = game_name.get_rect(center=(350, 340))

    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, 1400)

    obstacle_rect_list = []

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

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_active = True
                        start_time = int(pygame.time.get_ticks() / 1000)
            if event.type == obstacle_timer and game_active:
                if random.randint(0, 2):
                    obstacle_rect_list.append(snail_surface.get_rect(bottomright=(random.randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright=(random.randint(900, 1100), 210)))

        if game_active:

            screen.blit(sky_surface, (0, 0))
            screen.blit(ground_surface, (0, 300))
            score = display_score()

            player_gravity += 1
            player_rect.y += player_gravity
            if player_rect.bottom >= 300:
                player_rect.bottom = 300
            screen.blit(player_surf, player_rect)

            obstacle_rect_list = obstacle_movement(obstacle_rect_list)

            game_active = collision(player_rect, obstacle_rect_list)

        else:
            screen.fill((94, 129, 162))
            screen.blit(player_stand, player_stand_rect)
            player_rect.midbottom = (80, 300)
            player_gravity = 0
            obstacle_rect_list.clear()
            score_msg = test_font.render(f'Your score: {score}', False, (111, 196, 169))
            score_msg_rect = score_msg.get_rect(center=(400, 350))
            screen.blit(game_name, game_name_rect)

            if score == 0:
                screen.blit(game_msg, game_msg_rect)
            else:
                screen.blit(score_msg, score_msg_rect)

        pygame.display.update()

        clock.tick(60)

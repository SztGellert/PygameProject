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
    text_surface = test_font.render('My game', False, 'Black').convert_alpha()
    player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
    player_rect = player_surf.get_rect(midbottom = (80, 300))
    snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
    snail_rect = snail_surface.get_rect(midbottom = (160, 300))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               exit()
            screen.blit(sky_surface, (0,0))
            screen.blit(ground_surface, (0,300))
            screen.blit(text_surface, (300,50))
            if snail_rect.left < -100: snail_rect.left = 800
            screen.blit(player_surf, player_rect)
            screen.blit(snail_surface, snail_rect)
            snail_rect.left -= 3

        pygame.display.update()
        clock.tick(60)

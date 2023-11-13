#!/usr/bin/env python

def screen_creater():
    import pygame
    import colors

    pygame.init()


    # Set up the screen
    screen = pygame.display.set_mode((800, 600))
    screen.fill(colors.BLACK)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    

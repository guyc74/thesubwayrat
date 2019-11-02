import pygame, random, sys, time
# from pygame.locals import *

pygame.init()
windowSurface = pygame.display.set_mode((500, 700))
manny_image = pygame.image.load('manny.png')
manny_rect = manny_image.get_rect()
manny_rect.topleft = (250, 350)
windowSurface.blit(manny_image, manny_rect)
pygame.display.update()
time.sleep(2)

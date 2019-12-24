import pygame
pygame.init()
window = pygame.display.set_mode((700, 500))

manny_image = pygame.image.load('manny.png')
manny_rect = manny_image.get_rect()
manny_rect.topleft = (250, 250)
window.blit(manny_image, manny_rect)

pygame.display.update()
input()

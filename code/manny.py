import pygame, random, sys, time
from pygame.locals import *

# initialize the game
pygame.init()
game_width = 700
game_height = 400
windowSurface = pygame.display.set_mode((game_width, game_height))

# initialize many
manny_image = pygame.image.load('manny.png')
manny_rect = manny_image.get_rect()
manny_y = game_height / 2
manny_x = 200
manny_speed = 0.1
manny_is_alive = True

# initialize obstacles
obstacle_image = pygame.image.load('obstacle.png')
obstacles = []
obstacle_speed = 0.1

move_up = False
move_down = False
obstacle_add_counter = 0

while manny_is_alive:
  # check keys:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if event.type == KEYDOWN and event.key == K_UP:
      move_up = True

    if event.type == KEYDOWN and event.key == K_DOWN:
      move_down = True

    if event.type == KEYUP and event.key == K_UP:
      move_up = False

    if event.type == KEYUP and event.key == K_DOWN:
      move_down = False

  # move_manny:
  if move_up and manny_y > 0:
    manny_y = manny_y - manny_speed

  if move_down and (manny_y + manny_rect.height) < 500:
    manny_y = manny_y + manny_speed

  manny_rect.topleft = (manny_x, manny_y)

  # do we need to add an obstacle?
  obstacle_add_counter += 1
  if obstacle_add_counter == 500:
    obstacle = {'rect': obstacle_image.get_rect(),
                'image': obstacle_image,
                'x': 700,
                'y': random.randint(0, game_height)}
    obstacles.append(obstacle)
    obstacle_add_counter = 0
  
  # move each obstacle
  for obstacle in obstacles:
    obstacle['x'] -= obstacle_speed
    obstacle['rect'].topleft = (obstacle['x'], obstacle['y'])

  # when an obstacle reaches left of screen - remove it
  for obstacle in obstacles:
    if obstacle['x'] == 0:
      obstacles.remove(obstacle)

  # if manny touches any obstacle then manny is dead
  for obstacle in obstacles:
    if manny_rect.colliderect(obstacle['rect']):
      manny_is_alive = False

  # draw the elements of the game
  windowSurface.fill((0, 0, 0))
  windowSurface.blit(manny_image, manny_rect)
  for obstacle in obstacles:
    windowSurface.blit(obstacle['image'], obstacle['rect'])

  pygame.display.update()


manny_is_dead_image = pygame.image.load('manny_is_dead.png')
manny_is_dead_rect = manny_is_dead_image.get_rect()
manny_is_dead_rect.topleft = (100, 100)
windowSurface.blit(manny_is_dead_image, manny_is_dead_rect)
pygame.display.update()
input("many is dead ...")


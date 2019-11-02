Drawing Manny
=============

The first thing we'll do is draw Manny the rat.
A computer screen is a composed of many small points on a grid.
Each point is called a **pixel**.
The position of each pixel is indicated by two numbers:
the distance from the left side of the screen
and distance from the top of the screen.
This position is called a **coordinate**.
If the distance from the left side of the screen is x,
and the distance from the top of the screne is y,
then the coordinate of that pixel is (x,y).
In the figre below we see a pixel at position (7,4).

.. figure:: _static/pixel.png
    :figwidth: 85 %
    :width: 85 %
    :align: center

    A pixel at position (7,4)

To draw a rat we need to turn on several pixels.
In the figure below the picture of a simple rat was created by writing to pixels:
(2,3), (3,3), (4,3), (5,3),
(6,1), (6,2), (6,3), (6,4), (6,5),
(7,2), (7,3), (7,4),
(8,2), (8,3), (8,4),
(9,1), (9,2), (9,3), (9,4), (9,5)
and (10, 3).
That's a lot of pixels.

.. figure:: _static/simple_rat.png
    :figwidth: 85 %
    :width: 85 %
    :align: center

    A simple rat

It is hard to write so many pixels.
Instead of writing each pixel individually we can use a ready made image.
We can create one using the paint program.
You can also use thi ready image `Manny <manny.png>`_.
Right click on the link and save the image.

Manny on the screen
-------------------

Below is a piece of code that draws Manny on the screen.
Open a new file in your editor and call it draw_manny.py.
Then copy-paste the piece of code from the browser to the editor.
And now run the piece of code.

.. code-block:: python

  import pygame, random, sys, time
  pygame.init()
  windowSurface = pygame.display.set_mode((500, 700))
  manny_image = pygame.image.load('manny.png')
  manny_rect = manny_image.get_rect()
  manny_rect.topleft = (250, 350)
  windowSurface.blit(manny_image, manny_rect)
  pygame.display.update()
  time.sleep(2)

Lets go over each line and undertand what it does.


With the pygame package we don't have to create the image pixel by pixel.
Instead we can load an image to a variable::

  manny_image = pygame.image.load('manny.png')

You can create any image you like.
Or you can use this ready mande image of manny:

Right click on the image, download it and copy it to our directory.

To draw the image we define the rectable where it is on the screen.
First we create the rectangle::

  manny_rect = manny_image.get_rect()

Now we need to decide where on the screen we want to place Manny:

  manny_rect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)

And now we need to actually draw Manny::

  windowSurface.blit(manny_image, manny_rect)



Our program should look like this. Make sure you understand each part!::

  windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
  manny_image = pygame.image.load('manny.png')
  manny_rect = manny_image.get_rect()
  manny_rect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
  windowSurface.blit(manny_image, manny_rect)

Manny moves
===========

Subway obstacles
================

We drew Manny.
We moved Manny.

Drawing obstacles and moving obstacles should very similar and therefor easy.
The differences are:
* The obstacle image is different.
* Obstacles move from right to left and not up down.
* The obstacles need to move without our control - even if we don't touch the keyboard.

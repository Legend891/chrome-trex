##chrome diansour game##
import pygame
import random
from pygame.locals import *


pygame.init()

clock = pygame.time.Clock()
fps = 100

screenwidth = 1000
screenhieght = 936
track_scroll = 0
move_speed = 4
screen = pygame.display.set_mode((screenwidth, screenhieght))
pygame.display.set_caption('chrome dino')

run =True
while run :
	
	clock.tick(fps)
	
	
	bg = pygame.image.load('Bg.png')
	screen.blit (bg,(0,0))
	tk = pygame.image.load('Track.png')
	screen.blit (tk,(track_scroll,1227))
	track_scroll -= move_speed
	if abs(track_scroll) > 500 :
			track_scroll = 0
	
	
	
	pygame.display.update()
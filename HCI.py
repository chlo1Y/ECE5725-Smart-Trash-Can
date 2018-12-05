import pygame # Import pygame graphics library
import os # for OS calls
import time
from constants import *



def draw( status, screen, my_font ):
	trash_can = pygame.image.load("trash_can.PNG")
	trash_can_rect = trash_can.get_rect( center = ( 160, 170 ) )
	
	if( len(status) > 0 ):
		volume_surface = my_font.render( status, True, BLACK )
		print status
	screen.fill( WHITE )

	if status == "I am hungry":
		emotion = pygame.image.load("hungry.jpg")
		volume_surface_rect = volume_surface.get_rect( center=( 245, 230 ) )
		pygame.draw.rect( screen, RED, [240, 240 , 20, 0] )
	elif status == "feed me more":
		emotion = pygame.image.load("more.png")
		volume_surface_rect = volume_surface.get_rect( center=( 245, 180 ) )
		pygame.draw.rect( screen, RED, [240, 190 , 20, 50] )
	elif status == "almost full":
		emotion = pygame.image.load("sad.jpg")
		volume_surface_rect = volume_surface.get_rect( center=( 245, 130 ) )
		pygame.draw.rect( screen, RED, [240, 140 , 20, 100] )
	else:
		emotion = pygame.image.load("cry.png")
		volume_surface_rect = volume_surface.get_rect( center=( 245, 80 ) )
		pygame.draw.rect( screen, RED, [240, 90, 20, 150] )

	emotion_rect = emotion.get_rect( center = (160,40) )

	screen.blit( trash_can, trash_can_rect )
	screen.blit( volume_surface, volume_surface_rect )
	screen.blit( emotion, emotion_rect )
	pygame.display.flip()

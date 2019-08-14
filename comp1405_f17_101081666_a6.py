# ============================================================
#                                                             
# Student Name (as it appears on cuLearn): Long Nguyen     
# Student ID (9 digits in angle brackets): <101081666>        
# Course Code (for this current semester): COMP1405B          
#                                                             
# ============================================================
import sys
import pygame
pygame.init()

#Ask user if they need instructions
instructions = input("Do you require instructions? Enter YES or NO ").upper()
#If they need instructions, print instructions
if instructions == "YES":
	print("Choose from one of the following images for your background and enter the filename in its exact format into the command line when prompted:")
	print("abandoned_circus.bmp")
	print("abandoned_homestead.bmp")
	print("abandoned_plant.bmp")
	print("Then choose one of the following images for your ghost and enter the filename in its exact format into the command line when prompted:")
	print("ghost_with_broom.bmp")
	print("ghost_with_crutches.bmp")
	print("ghost_with_frame.bmp")	
else:
	print()

#Getting filenames for background and ghost images
background = input("Enter the filename of your background ")
ghost = input("Enter the filename of your image ")


#loading the image
background_load = pygame.image.load(background)
#getting the size of the background image
(w,h) = background_load.get_rect().size
#setting the display screen
screen = pygame.display.set_mode((w,h))
#set the background picture as the screen
screen.blit(background_load, (0,0))
#display background
pygame.display.update()

#load ghost image
ghost_load = pygame.image.load(ghost)
#get size of ghost image
(gw,gh) = ghost_load.get_rect().size

#asking user for x and y coordinates
while True:
	ghost_x = int(input("Enter the x coordinate for your image position "))
	ghost_y = int(input("Enter the y coordinate for your image position "))
	if ((ghost_x < 0 or ghost_x > w) or (ghost_y < 0 or ghost_y > h)):
		print("Choose x and y coordinates within the borders")
	else:
		break;

#checking each pixel for colors
for i in range (gw):
	for j in range (gh):
		(gr,gg,gb,_) = ghost_load.get_at((i,j))
		(br,bg,bb,_) = background_load.get_at((i+ghost_x,j+ghost_y))
		if (gr,gg,gb) == (0,255,0):
			ghost_load.set_at((i,j),(br,bg,bb))
		if not (gr,gg,gb) == (0,255,0): 
			ghost_load.set_at((i,j),((gr+br)/2,(gg+bg)/2,(gb+bb)/2)) 


screen.blit(ghost_load,(ghost_x,ghost_y))
		
while True:
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	



	



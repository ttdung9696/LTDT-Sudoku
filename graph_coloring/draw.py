import pygame
from random import randint	

def main():

	board = [
		[7, 8, 0, 4, 0, 0, 1, 2, 0],
		[6, 0, 0, 0, 7, 5, 0, 0, 9],
		[0, 0, 0, 6, 0, 1, 0, 7, 8],
		[0, 0, 7, 0, 4, 0, 2, 6, 0],
		[0, 0, 1, 0, 5, 0, 9, 3, 0],
		[9, 0, 4, 0, 6, 0, 0, 0, 5],
		[0, 7, 0, 3, 0, 0, 0, 1, 2],
		[1, 2, 0, 0, 0, 7, 4, 0, 0],
		[0, 4, 9, 2, 0, 6, 0, 0, 7]
	]
	win = pygame.display.set_mode((800, 800))
	win.fill((255,255,255))
	pygame.draw.circle(win, (220,220,220), (50, 50), 30)
	pygame.draw.circle(win, (220,220,220), (200, 200), 30)
	pygame.draw.line(win, (255,0,255), (50,50), (200,200), 2)
	pygame.display.update()
	run = True
	while run:
		True

main()
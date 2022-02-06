from random import randint

import pygame, sys
from pygame.locals import *


# Funciones
# salir De Luego
def salir(): 
	pygame.quit()
	sys.exit()

pygame.init()

# Puntos
Puntos = 0

# Cursor
pygame.mouse.set_visible(False)

# Teclas
pygame.key.set_repeat(1, 25)

# Musica
pygame.mixer.music.load("Mat/Back_to_the_volcano_castle.mp3")
pygame.mixer.music.play(1)
pygame.mixer.music.set_volume(0.10)

# reloj
fps = 60
reloj = pygame.time.Clock()

# ventana
ventana = pygame.display.set_mode([1920, 1080])
pygame.display.set_caption("Shoot The Aliens")
fondo = pygame.image.load('Mat/Fondo_Espacial.png')
color = (0, 0, 0)
menu = (100, 230, 90)

# Mirilla_Jugador
mirilla = pygame.image.load('Mat/Mirilla.png')
rect_mirilla = mirilla.get_rect()

# Pause / Play
play = pygame.image.load('Mat/Play.png')
rect_play = play.get_rect()

pause = pygame.image.load('Mat/Pause.png')
rect_pause = pause.get_rect()

rect_pause.center = (1900, 1050)
rect_play.center = (1850, 1050)

num_marcianos = 0

# num_marcianos = 7 #input("Introduce Un Numero De Aliens Para Matar:")

# Texto En Pantalla
text = "Introduce un Número de Aliens a Combatir"
fuente = pygame.font.Font(None, 30)
mensaje = fuente.render(text, 1, (255, 255, 255))

# Loop Del menu Del Juego
seguir = False
while seguir == False:

	ventana.fill(color)
	
	if num_marcianos == 0:
		ventana.blit(mensaje, (700, 540))
	else:
		text2 = str(num_marcianos) + " Aliens Desplegados En La Galaxia Pulsa Arriba Para Salvar La Tierra"
		mensaje2 = fuente.render(text2, 1, (255, 255, 255))
		ventana.blit(mensaje2, (700, 540))
		
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			salir()
	
		elif event.type == KEYDOWN:
			if (num_marcianos == 0 and (event.key == K_1
				or event.key == K_2 or event.key == K_3
				or event.key == K_4 or event.key == K_5
				or event.key == K_6 or event.key == K_7
				or event.key == K_8 or event.key == K_9)):
				num_marcianos = event.key - 48
				
			if event.key == K_UP:
				seguir = True
			elif event.key == K_ESCAPE:
				salir()
                    
	pygame.display.update()
	reloj.tick(fps)

# Enemigos
contador_aliens = 0

# Arrays Enemigos
Alien = { }
Rect_Alien = { }
Alien_Visible = { }

for i in range(0, num_marcianos):
	Alien[i] = pygame.image.load('Mat/Alien_Invader.png')
	Rect_Alien[i] = Alien[i].get_rect()
	Alien_Visible[i] = True
	Rect_Alien[i].left = randint(50, 1900)
	Rect_Alien[i].top = randint(50, 1000)

# Loop Principal Del Juego
pygame.mouse.set_visible(False)

while True:

	if Puntos > num_marcianos - 1:
		print("Has Ganado ;)")
		salir()

	rect_mirilla.center = pygame.mouse.get_pos()

	ventana.fill(color)
	ventana.blit(fondo, (0, 0))

	ventana.blit(play, rect_play)
	ventana.blit(pause, rect_pause)

	for i in range(0, num_marcianos):
		if Alien_Visible[i] == True:
			Rect_Alien[i].left = Rect_Alien[i].left + 2
			if Rect_Alien[i].left > 1900:
				Rect_Alien[i].left = 20
			
			ventana.blit(Alien[i], Rect_Alien[i])
		
	ventana.blit(mirilla, rect_mirilla)

	for event in pygame.event.get():
			if event.type == pygame.QUIT:
	        		salir()
	        	
			if event.type == pygame.MOUSEBUTTONDOWN:
					if rect_pause.collidepoint(pygame.mouse.get_pos()) == True:
						pygame.mixer.music.pause()
					
					if rect_play.collidepoint(pygame.mouse.get_pos()) == True:
						pygame.mixer.music.unpause()
				
					for i in range(0, num_marcianos):
							if Rect_Alien[i].collidepoint(pygame.mouse.get_pos()) == True and Alien_Visible[i] == True:
								contador_aliens = contador_aliens + 1
								Alien_Visible[i] = False
								Puntos = Puntos + 1
								print("Has Eliminado:" , contador_aliens , "Aliens !!")
								
			elif event.type == KEYDOWN:
				if event.key == K_p:
					pygame.mixer.music.pause()
				elif event.key == K_ESCAPE:
					salir()
					
	pygame.display.update()
	reloj.tick(fps)


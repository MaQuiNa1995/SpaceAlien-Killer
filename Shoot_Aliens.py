from random import randint
from tkinter import CENTER

import pygame, sys
from pygame.locals import *


# Funciones
# salir De Luego
def salir():
	print("Saliendo Del Juego...")
	pygame.quit()
	sys.exit()


pygame.init()

# Puntos
Puntos = 0

# Cursor
pygame.mouse.set_visible(False)

# Teclas
pygame.key.set_repeat(1, 25)

# Jugador
nave = pygame.image.load('Mat/Space_ship.png')
rect_nave = nave.get_rect()
rect_nave.left = 540
rect_nave.top = 1016
velocidad = 14

# Musica
pygame.mixer.music.load("Mat/Back_to_the_volcano_castle.mp3")
pygame.mixer.music.play(1)
pygame.mixer.music.set_volume(0.10)

# Reloj
fps = 60
reloj = pygame.time.Clock()

# ventana
ventana = pygame.display.set_mode([1920, 1080])
pygame.display.set_caption("Shoot The Aliens")
fondo = pygame.image.load('Mat/Fondo_Espacial.png')
color = (0, 0, 0)
disparoColor = (255,255,0)
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

# Texto En Pantalla
text = "Introduce un Número de Aliens a Combatir"
fuente = pygame.font.Font(None, 30)
mensaje = fuente.render(text, 1, (255, 255, 255))

# --------------- Loop Del menu Del Juego ---------------
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
alien = { }
rect_alien = { }
alien_visible = { }

for i in range(0, num_marcianos):
	alien[i] = pygame.image.load('Mat/Alien_Invader.png')
	rect_alien[i] = alien[i].get_rect()
	alien_visible[i] = True
	rect_alien[i].left = randint(50, 1900)
	rect_alien[i].top = randint(50, 1000)

disparo = pygame.image.load('Mat/Disparo.png')
disparo = pygame.transform.scale(disparo, (disparo.get_width()+10,disparo.get_height() +10))
rect_disparo = disparo.get_rect()

# --------------- Loop Principal Del Juego ---------------
pygame.mouse.set_visible(False)
disparoActivo = False

while True:

	if Puntos > num_marcianos - 1:
		print("Has Ganado ;)")
		salir()

	rect_mirilla.center = pygame.mouse.get_pos()

	ventana.fill(color)
	ventana.blit(fondo, (0, 0))

	ventana.blit(nave, rect_nave)

	ventana.blit(play, rect_play)
	ventana.blit(pause, rect_pause)

	if disparoActivo == True:
		rect_disparo.y = rect_disparo.y - 4
		ventana.blit(disparo, rect_disparo)

		if rect_disparo.y < 0:
			disparoActivo = False
			print("No has dado a nadie")

	for i in range(0, num_marcianos):
		if alien_visible[i] == True:
			rect_alien[i].left = rect_alien[i].left + 2
			if rect_alien[i].left > 1900:
				rect_alien[i].left = 20
			
			ventana.blit(alien[i], rect_alien[i])
		
	ventana.blit(mirilla, rect_mirilla)

	for i in range(0, num_marcianos):
		if pygame.Rect.colliderect(rect_alien[i], rect_disparo) == True and alien_visible[i] == True:
			contador_aliens = contador_aliens + 1
			alien_visible[i] = False
			Puntos = Puntos + 1
			print("Has Eliminado:" , contador_aliens , "Aliens !!")
			disparoActivo = False

	for event in pygame.event.get():
			if event.type == pygame.QUIT:
	        		salir()
	
			if event.type == pygame.MOUSEBUTTONDOWN:
					if rect_pause.collidepoint(pygame.mouse.get_pos()) == True:
						pygame.mixer.music.pause()
					
					if rect_play.collidepoint(pygame.mouse.get_pos()) == True:
						pygame.mixer.music.unpause()
								
			elif event.type == KEYDOWN:
				if event.key == K_p:
					pygame.mixer.music.pause()
				elif event.key == K_ESCAPE:
					salir()
				elif event.key == K_LEFT:
					rect_nave.x = rect_nave.x - velocidad
				elif event.key == K_RIGHT:
					rect_nave.x = rect_nave.x + velocidad
				elif event.key == K_SPACE:
					if disparoActivo == False:
						print("disparo")
						rect_disparo.center = rect_nave.center
					disparoActivo = True
					
	pygame.display.update()
	reloj.tick(fps)


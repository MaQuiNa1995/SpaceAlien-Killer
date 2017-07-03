import pygame,sys
from pygame.locals import *
from random import randint

#Funciones

# Salir De Luego
def Salir(): 
	pygame.quit()
	sys.exit()

pygame.init()

# Puntos
Puntos = 0

# Cursor
pygame.mouse.set_visible(False)
# Pillar Posicion Actual Del Raton pygame.mouse.get_pos()

# Teclas
pygame.key.set_repeat(1,25)

#Musica
pygame.mixer.music.load("Musica/Cruzifi.mp3")
pygame.mixer.music.play(1)
pygame.mixer.music.set_volume(0.10)

# Reloj
Fps = 20
Reloj = pygame.time.Clock()

# Ventana
Ventana = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Shoot The Aliens")
Fondo = pygame.image.load('Mat/Fondo_Espacial.png')
Color_Ventana = (0,0,0)
Menu = (100,230,90)

# Mirilla_Jugador
Mirilla = pygame.image.load('Mat/Mirilla2.png')
Rect_Mirilla = Mirilla.get_rect()

# Pause / Play
Repro = pygame.image.load('Mat/Play.png')
Rect_Repro = Repro.get_rect()

Pausa = pygame.image.load('Mat/Pause.png')
Rect_Pausa = Pausa.get_rect()

Rect_Pausa.center = (485,485)
Rect_Repro.center = (485,485)

Reproducir = False
Musica_Ocupada = False
Click = False

#Num_Marcianos=raw_input("Introduce Un Numero De Aliens Para Matar:")

# Texto En Pantalla
Text = "5 Aliens Desplegados En La Galaxia, Pulsa Arriba Para Salvar La Tierra" 
fuente = pygame.font.Font(None, 20)
mensaje = fuente.render(Text, 1, (255, 255, 255))


# Loop Del Menu Del Juego
Seguir = False
while Seguir == False:

	Ventana.fill(Color_Ventana)
	Ventana.blit(mensaje, (50, 250))

	for event in pygame.event.get():	
		
        	if event.type == pygame.QUIT:
                	Salir()

		elif event.type==KEYDOWN:
			if event.key==K_UP:
				Seguir = True

                        elif event.key==K_ESCAPE:
                                Salir()
	pygame.display.update()
	Reloj.tick(Fps)

# Enemigos
Contador_Aliens = 0
Num_Marcianos = 5

# Arrays Enemigos
Alien = { }
Rect_Alien = { }
Alien_Visible = { }

for i in range(0,Num_Marcianos):
	Alien[i] = pygame.image.load('Mat/Alien_Invader2.png')
	Rect_Alien[i] = Alien[i].get_rect()
	Alien_Visible[i] = True
	Rect_Alien[i].left = randint(50,450)
	Rect_Alien[i].top = randint(50,450)

# Loop Principal Del Juego
pygame.mouse.set_visible(False)

while True:

	if Puntos > Num_Marcianos-1:
		print("Has Ganado ;)")
		Salir()

	Rect_Mirilla.center = pygame.mouse.get_pos()

	Ventana.fill(Color_Ventana)
	Ventana.blit(Fondo,(0,0))

	if Reproducir == True:
		Ventana.blit(Repro, Rect_Repro)
	else:
		Ventana.blit(Pausa, Rect_Pausa)

	for i in range(0,Num_Marcianos):
		if Alien_Visible[i] == True:
			Ventana.blit(Alien[i], Rect_Alien[i])
		
	Ventana.blit(Mirilla, Rect_Mirilla)
	
#	if Rect_Pausa.collidepoint(Rect_Mirilla.center) or Rect_Repro.collidepoint(Rect_Mirilla.center) and Click == False:
#		Click = True

	for event in pygame.event.get():

        	if event.type == pygame.QUIT:
                	Salir()


		elif event.type==pygame.MOUSEBUTTONDOWN:

			#if Reproducir == False and Musica_Ocupada == False:
			if Reproducir == False and Rect_Pausa.collidepoint(pygame.mouse.get_pos()) == True:
				pygame.mixer.music.play(1)
				pygame.mixer.music.set_volume(0.10)
				Reproducir = True

			if Reproducir == True and Rect_Repro.collidepoint(pygame.mouse.get_pos()) == True:
				Reproducir = False
				pygame.mixer.music.stop()

			for i in range(0,Num_Marcianos):
				if Rect_Alien[i].collidepoint(pygame.mouse.get_pos()) == True and Alien_Visible[i] == True:
					Contador_Aliens = Contador_Aliens + 1
            				print "Has Eliminado:",Contador_Aliens ,"Aliens !!"
					Alien_Visible[i] = False
					Puntos = Puntos + 1

                elif event.type==KEYDOWN:
			if event.key==K_p:
				pygame.mixer.music.stop()

                        elif event.key==K_ESCAPE:
                                Salir()

	
	pygame.display.update()
	Reloj.tick(Fps)



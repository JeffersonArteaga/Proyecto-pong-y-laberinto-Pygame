# Proyecto videojuegos Computacion Grafica Jefferson Arteaga - Juan Miguel Aguirre

import pygame
import time
import os
import sys
pygame.init()

#Colores
Negro = (0, 0, 0)
Blanco = (255, 255, 255)
rojo = (255, 0, 0)
azul = (0, 0, 255)
Tamano = (1280, 720)
PlayerAncho = 15
PlayerAlto = 90

Ventana = pygame.display.set_mode(Tamano)

clock = pygame.time.Clock()
fondo = pygame.image.load("fondos/fondoPong6.jpg").convert()
fondoPereira = pygame.image.load("fondos/fondoPereira.jpg").convert()
fondoBoca = pygame.image.load("fondos/fondoBoca.jpg").convert()
fondoEmpate = pygame.image.load("fondos/fondoEmpate.jpg").convert()

# Cargar imagen del balón
balon = pygame.image.load("imagenes/balon.png")  # cargar imagen
nuevo_tamaño = (balon.get_width() // 45, balon.get_height() // 45)  # nuevo tamaño de la imagen
balon_reducido = pygame.transform.scale(balon, nuevo_tamaño)  # escalar imagen

# Definir la fuente y el tamaño del texto
font = pygame.font.SysFont('Bahnschrift', 40)
font_time = pygame.font.SysFont('Bahnschrift', 35)
font_time_final = pygame.font.SysFont('Bahnschrift', 30)


# Definir la variable que deseas mostrar
score_p = 0
score_b = 0

#Coordenadas y velocidad del jugador 1
CoorPlayer1_X = 50
CoorPlayer1_Y = 360 - 45
player1Vel_Y = 0

#Coordenadas y velocidad del jugador 2
CoorPlayer2_X = 1230 - PlayerAncho
CoorPlayer2_Y = 360 - 45
Player2Vel_Y = 0

# Coordenadas de la pelota
Pelota_X = 650
Pelota_Y = 410
PelotaVel_X = 13
PelotaVel_Y = 13

game_over = False
resultado = False
pelota_en_posicion_inicial = False

pygame.mixer.music.load("sonidos/songPong.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)  # Reproducir la música en bucle
sonidoGol = pygame.mixer.Sound("sonidos/gritoGol.mp3")
sonidoGolClos = pygame.mixer.Sound("sonidos/gritoGolClos.mp3")
select = pygame.mixer.Sound("sonidos/select.mp3")
pitidoFinal = pygame.mixer.Sound("sonidos/pitidoFinal.mp3")

# Definir el tiempo límite en segundos
time_limit = 90
start_time = time.time()

# Función para convertir segundos a minutos y segundos separados
def get_time(seconds):
    minutes = seconds // 60
    seconds %= 60
    return f"{minutes:02d}:{seconds:02d}"

s1 = False
s2 = False

while not game_over:
	 # Obtener el tiempo transcurrido
	elapsed_time = int(time.time() - start_time)
    
    # Obtener el tiempo restante
	time_left = time_limit - elapsed_time
	x, y = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			
			if 760 <= x <= 1150 and 614 <= y <= 663:
				pygame.quit()
				quit()

			if 109 <= x <= 522 and 614 <= y <= 663:
				pygame.quit()
				os.system("py -m menu.py")
				sys.exit()


		if event.type == pygame.KEYDOWN:
			# Jugador 1
			if event.key == pygame.K_w:
				player1Vel_Y = -4
			if event.key == pygame.K_s:
				player1Vel_Y = 4

				# Jugador 2
			if event.key == pygame.K_UP:
					Player2Vel_Y = -4
			if event.key == pygame.K_DOWN:
					Player2Vel_Y = 4
		
		if event.type == pygame.KEYUP:
			# Jugador 1
			if event.key == pygame.K_w:
				player1Vel_Y = 0
			if event.key == pygame.K_s:
				player1Vel_Y = 0
			# Jugador 2
			if event.key == pygame.K_UP:
				Player2Vel_Y = 0
			if event.key == pygame.K_DOWN:
				Player2Vel_Y = 0
		
	

	#Ventana.blit(fondo, (0, 0))

	#Zona de dibujo

	

	

	# Si el tiempo restante es menor o igual a cero, salir del bucle
	if time_left > 0:
		Ventana.blit(fondo, (0, 0))
		if pelota_en_posicion_inicial:
			pygame.time.delay(2000)
			pelota_en_posicion_inicial = False
			pygame.mixer.music.set_volume(0.3)

	
		if Pelota_Y > 690 or Pelota_Y < 140:
			PelotaVel_Y *= -1

		# Revisa si la pelota sale del lado derecho
		if Pelota_X > 1280:
			score_p += 1
			pygame.mixer.music.set_volume(0.1)
			sonidoGol.play()
			sonidoGolClos.play()
			Pelota_X = 650
			Pelota_Y = 410
			# Si sale de la pantalla, invierte direccion
			PelotaVel_X *= -1
			PelotaVel_Y *= -1
			pelota_en_posicion_inicial = True
			#Coordenadas y velocidad del jugador 1
			CoorPlayer1_X = 50
			CoorPlayer1_Y = 360 - 45
			player1Vel_Y = 0

			#Coordenadas y velocidad del jugador 2
			CoorPlayer2_X = 1230 - PlayerAncho
			CoorPlayer2_Y = 360 - 45
			Player2Vel_Y = 0

		# Revisa si la pelota sale del lado izquierdo
		if Pelota_X < 0:
			score_b += 1
			pygame.mixer.music.set_volume(0.1)
			sonidoGol.play()
			sonidoGolClos.play()
			Pelota_X = 650
			Pelota_Y = 410
			# Si sale de la pantalla, invierte direccion
			PelotaVel_X *= -1
			PelotaVel_Y *= -1
			pelota_en_posicion_inicial = True
			CoorPlayer1_X = 50
			CoorPlayer1_Y = 360 - 45
			player1Vel_Y = 0

			#Coordenadas y velocidad del jugador 2
			CoorPlayer2_X = 1230 - PlayerAncho
			CoorPlayer2_Y = 360 - 45
			Player2Vel_Y = 0

		


		# Modifica las coordenadas para dar mov. a los jugadores/ pelota
		#CoorPlayer1_Y += player1Vel_Y
		CoorPlayer1_Y += player1Vel_Y
		CoorPlayer1_Y = pygame.math.clamp(CoorPlayer1_Y, 0, 630) # 630 es el tamaño de la pantalla (720) menos el tamaño del jugador (90)

		CoorPlayer2_Y += Player2Vel_Y
		CoorPlayer2_Y = pygame.math.clamp(CoorPlayer2_Y, 0, 630) # 630 es el tamaño de la pantalla (720) menos el tamaño del jugador (90)

		# Movimiento pelota
		Pelota_X += PelotaVel_X
		Pelota_Y += PelotaVel_Y


		jugador1 = pygame.draw.rect(Ventana,rojo, (CoorPlayer1_X, CoorPlayer1_Y, PlayerAncho, PlayerAlto))
		jugador2 = pygame.draw.rect(Ventana, azul, (CoorPlayer2_X, CoorPlayer2_Y, PlayerAncho, PlayerAlto))	
		balon_reducido_rect = balon_reducido.get_rect(center=(Pelota_X, Pelota_Y))
		Ventana.blit(balon_reducido, balon_reducido_rect)

			# Obtener el tiempo restante en minutos y segundos separados
		time_text = get_time(time_left)

		# Renderizar el texto que muestra el tiempo restante
		text_surface = font_time.render(time_text, True, Blanco)
		Ventana.blit(text_surface, (420, 35))
		
		# Colisiones
		if balon_reducido_rect.colliderect(jugador1) or balon_reducido_rect.colliderect(jugador2):
			PelotaVel_X *= -1

	else:
		pygame.mixer.music.stop()
		if not s2:
			pitidoFinal.play()
			s2 = True
		if score_p == score_b:
			Ventana.blit(fondoEmpate, (0, 0))
		elif score_p > score_b:
			Ventana.blit(fondoPereira, (0, 0))
		elif score_b > score_p:
			Ventana.blit(fondoBoca, (0, 0))
		# Renderizar el texto que muestra el tiempo restante
		text_surface = font_time_final.render("FINAL", True, Blanco)
		Ventana.blit(text_surface, (420, 35))

		if 109 <= x <= 522 and 614 <= y <= 663:
			if not s1:
				select.play()
				s1 = True
			pygame.draw.line(Ventana, Negro, (109, 670), (522, 670), 2)
			pygame.draw.line(Ventana, Negro, (109, 671), (522, 671), 2)
			pygame.draw.line(Ventana, Negro, (109, 672), (522, 672), 2)
       
        # Dibujar la línea amarilla si el mouse está en el área de pong
		elif 760 <= x <= 1150 and 614 <= y <= 663:
			if not s1:
				select.play()
				s1 = True
			pygame.draw.line(Ventana, Negro, (760, 670), (1156, 670), 2)
			pygame.draw.line(Ventana, Negro, (760, 671), (1156, 671), 2)
			pygame.draw.line(Ventana, Negro, (760, 672), (1156, 672), 2)
			pygame.draw.line(Ventana, Negro, (760, 673), (1156, 673), 2)
		else:
			s1 = False

	# Crear el objeto Surface con el texto
	score_text = font.render(f'{score_p}      {score_b}', True, Blanco)

	# Copiar el objeto Surface en la pantalla
	Ventana.blit(score_text, (160, 35))
	
	
	pygame.display.flip()
	clock.tick(60)




pygame.quit()
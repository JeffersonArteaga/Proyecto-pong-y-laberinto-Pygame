# Proyecto videojuegos Computacion Grafica Jefferson Arteaga - Juan Miguel Aguirre

import pygame
import os
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Cargar imágenes de fondo y escalarlas a tamaño HD
background_frames = []
background_folder = "fondos/fondoMenu"
for file_name in sorted(os.listdir(background_folder)):
    if file_name.endswith(".jpg"):
        file_path = os.path.join(background_folder, file_name)
        image = pygame.image.load(file_path)
        image = pygame.transform.scale(image, (screen_width, screen_height))
        background_frames.append(image)
background_frames += background_frames[::-1]  # Invertir la lista


opening_frames = []
opening_folder = "fondos/fondoOpening"
for file_name in sorted(os.listdir(opening_folder)):
    if file_name.endswith(".jpg"):
        file_path = os.path.join(opening_folder, file_name)
        image = pygame.image.load(file_path)
        image = pygame.transform.scale(image, (screen_width, screen_height))
        opening_frames.append(image)

# Configurar el reloj
clock = pygame.time.Clock()
FPS = 25

# Cargar sonido de fondo
pygame.mixer.music.stop()
pygame.mixer.music.load("sonidos/songMenu.mp3")
select = pygame.mixer.Sound("sonidos/select.mp3")

s1 = False
music_playing = False
# Cargar sonido de clic


# Bucle principal del juego
current_frame = 0
opening = True
while True:

    # Lógica del juego
    # ...

    if opening:
        screen.blit(opening_frames[current_frame], (0, 0))
        current_frame += 1
        if current_frame == (len(opening_frames) -1):
            opening = False
            current_frame = 0
    else:
        screen.blit(background_frames[current_frame], (0, 0))
        current_frame = (current_frame + 1) % len(background_frames)

        x, y = pygame.mouse.get_pos()
        # Dibujar la línea rosada si el mouse está en el área de salir
        if 35 <= x <= 203 and 18 <= y <= 107:
            if not s1:
                select.play()
                s1 = True
            pygame.draw.line(screen, (238, 37, 201), (37, 109), (202, 109), 2)
            pygame.draw.line(screen, (238, 37, 201), (37, 110), (202, 110), 2)
            pygame.draw.line(screen, (238, 37, 201), (37, 111), (202, 111), 2)
       
        # Dibujar la línea amarilla si el mouse está en el área de pong
        elif 514 <= x <= 726 and 342 <= y <= 403:
            if not s1:
                select.play()
                s1 = True
            pygame.draw.line(screen, (237, 243, 37), (514, 412), (726, 412), 2)
            pygame.draw.line(screen, (237, 243, 37), (514, 413), (726, 413), 2)
            pygame.draw.line(screen, (237, 243, 37), (514, 414), (726, 414), 2)
            
        # Dibujar la línea amarilla si el mouse está en el área de laberinto
        elif 404 <= x <= 875 and 450 <= y <= 509:
            if not s1:
                select.play()
                s1 = True
            pygame.draw.line(screen, (237, 243, 37), (404, 518), (875, 518), 2)
            pygame.draw.line(screen, (237, 243, 37), (404, 519), (875, 519), 2)
            pygame.draw.line(screen, (237, 243, 37), (404, 520), (875, 520), 2)
        else:
            s1 = False
    
          # Reproducir la música en bucle
    if not opening and not music_playing:
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)  # Reproducir la música en bucle
        music_playing = True
    
    # Actualizar pantalla
    pygame.display.flip()

    # Cambiar al siguiente fotograma
    
    # Limitar FPS
    clock.tick(FPS)

    # Comprobar eventos de salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 58 <= x <= 300 and 40 <= y <= 158:
                pygame.quit()
                quit()

            if 514 <= x <= 726 and 342 <= y <= 403:
                pygame.quit()
                if sys.platform == "win32":
                    os.system("py -m pong.py")
                else:  # Asumimos cualquier otro caso como Linux/Unix
                    os.system("python3 -m pong.py")
                sys.exit()

            if 404 <= x <= 875 and 450 <= y <= 509:
                pygame.quit()
                if sys.platform == "win32":
                    os.system("py -m laberinto.py")
                else:  # Asumimos cualquier otro caso como Linux/Unix
                    os.system("python3 -m laberinto.py")
                sys.exit()
                
                



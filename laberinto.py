# Proyecto videojuegos Computacion Grafica Jefferson Arteaga - Juan Miguel Aguirre

import pygame
import os
import sys
def walls(window):
    size = (700,700)
    wall_width = 7
    wall_lenght = size[1] - 200 
    grid_size = wall_lenght/11
    start_x = 100
    start_y = 100
    #colors
    BLACK = (0,0,0)
    walls = [pygame.draw.rect(window,BLACK,(0,start_y,start_x,wall_width)),
            pygame.draw.rect(window,BLACK,(0,start_y + grid_size,start_x,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x,start_y,wall_lenght,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x,start_y + grid_size,wall_lenght - 10*grid_size,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 2*grid_size,start_y + grid_size,wall_lenght - 10*grid_size+1,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 4*grid_size,start_y + grid_size,wall_lenght - 9*grid_size,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 8*grid_size,start_y + grid_size,wall_lenght - 9*grid_size+1,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + grid_size,start_y + 2*grid_size,wall_lenght - 10*grid_size,wall_width)), 
            pygame.draw.rect(window,BLACK,(start_x + 3*grid_size,start_y + 2*grid_size,grid_size,wall_width)), 
            pygame.draw.rect(window,BLACK,(start_x + 6*grid_size,start_y + 2*grid_size,5*grid_size+1,wall_width)), 
            pygame.draw.rect(window,BLACK,(start_x,start_y + 3*grid_size,grid_size,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 5*grid_size,start_y + 3*grid_size,5*grid_size,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + grid_size,start_y + 4*grid_size,grid_size,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 4*grid_size,start_y + 4*grid_size,grid_size+1,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 7*grid_size,start_y + 4*grid_size,grid_size,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 9*grid_size,start_y + 4*grid_size,grid_size,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + grid_size,start_y + 5*grid_size,2*grid_size+1,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 8*grid_size,start_y + 5*grid_size,grid_size+1,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + grid_size,start_y + 6*grid_size,grid_size,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 3*grid_size,start_y + 6*grid_size,grid_size,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 7*grid_size,start_y + 6*grid_size,grid_size,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x,start_y + 7*grid_size,3*grid_size,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 4*grid_size,start_y + 7*grid_size,grid_size+1,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 8*grid_size,start_y + 7*grid_size,grid_size+1,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 3*grid_size,start_y + 8*grid_size,grid_size,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 5*grid_size,start_y + 8*grid_size,grid_size,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 9*grid_size,start_y + 8*grid_size,2*grid_size+1,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 2*grid_size,start_y + 9*grid_size,2*grid_size+1,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 5*grid_size,start_y + 9*grid_size,2*grid_size+1,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 8*grid_size,start_y + 9*grid_size,grid_size+1,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x,start_y + 10*grid_size,grid_size,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 4*grid_size,start_y + 10*grid_size,grid_size+1,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 7*grid_size,start_y + 10*grid_size,grid_size,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x,start_y + 11*grid_size,wall_lenght,wall_width)),
            pygame.draw.rect(window,BLACK,(start_x,start_y + grid_size,wall_width,8*grid_size)),
            pygame.draw.rect(window,BLACK,(start_x,start_y + 10*grid_size,wall_width,grid_size+1)),
            pygame.draw.rect(window,BLACK,(start_x + grid_size,start_y + 5*grid_size,wall_width,grid_size)),
            pygame.draw.rect(window,BLACK,(start_x + grid_size,start_y + 8*grid_size,wall_width,2*grid_size+wall_width+1)),
            pygame.draw.rect(window,BLACK,(start_x + 2*grid_size,start_y + grid_size,wall_width,3*grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 2*grid_size,start_y + 7*grid_size,wall_width,3*grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 3*grid_size,start_y,wall_width,grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 3*grid_size,start_y + 2*grid_size,wall_width,3*grid_size+wall_width+1)),
            pygame.draw.rect(window,BLACK,(start_x + 3*grid_size,start_y + 6*grid_size,wall_width,grid_size+wall_width+1)),
            pygame.draw.rect(window,BLACK,(start_x + 3*grid_size,start_y + 10*grid_size,wall_width,grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 4*grid_size,start_y + grid_size,wall_width,grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 4*grid_size,start_y + 3*grid_size,wall_width,3*grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 4*grid_size,start_y + 7*grid_size,wall_width,grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 4*grid_size,start_y + 9*grid_size,wall_width,grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 5*grid_size,start_y + grid_size,wall_width,2*grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 5*grid_size,start_y + 4*grid_size,wall_width,3*grid_size+wall_width+1)),
            pygame.draw.rect(window,BLACK,(start_x + 5*grid_size,start_y + 9*grid_size,wall_width,grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 6*grid_size,start_y + 3*grid_size,wall_width,5*grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 6*grid_size,start_y + 10*grid_size,wall_width,grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 7*grid_size,start_y + grid_size,wall_width,grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 7*grid_size,start_y + 4*grid_size,wall_width,6*grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 8*grid_size,start_y,wall_width,grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 8*grid_size,start_y + 5*grid_size,wall_width,grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 8*grid_size,start_y + 7*grid_size,wall_width,2*grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 9*grid_size,start_y + 4*grid_size,wall_width,grid_size+wall_width+1)),
            pygame.draw.rect(window,BLACK,(start_x + 9*grid_size,start_y + 6*grid_size,wall_width,2*grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 9*grid_size,start_y + 9*grid_size,wall_width,2*grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 10*grid_size,start_y + 3*grid_size,wall_width,grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 10*grid_size,start_y + 5*grid_size,wall_width,2*grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 10*grid_size,start_y + 8*grid_size,wall_width,2*grid_size+wall_width)),
            pygame.draw.rect(window,BLACK,(start_x + 11*grid_size,start_y,wall_width,wall_lenght+wall_width))]
    return walls

class mochi(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sheet = pygame.image.load("imagenes/mochi.png")
        self.sheet.set_clip(pygame.Rect(37,15,21,19))
        self.image = pygame.transform.scale(self.sheet.subsurface(self.sheet.get_clip()),(31,28))
        self.rect = self.image.get_rect()
        self.sheet_hurt = pygame.image.load("imagenes/mochi_hurt.png")
        self.sheet_hurt.set_clip(pygame.Rect(7, 15, 21, 19))
        self.direction = "right"
        self.rect.x = x
        self.rect.y = y
        self.frame = 0
        self.vel_x = 0
        self.vel_y = 0
        self.states = {0: (7,15,21,19),1: (37,15,21,19),2: (67,15,21,19),3: (101,15,21,19)}
    
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

class background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sheet = pygame.image.load("imagenes/space.png")
        self.sheet.set_clip(pygame.Rect(0, 0, 64, 64))
        self.image = pygame.transform.scale(self.sheet.subsurface(self.sheet.get_clip()),(700,700))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.frame = 0
        self.states = {0: (0,0,64,64),1: (64,0,64,64),2: (128,0,64,64),3:(192,0,64,64)}

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
    
class portal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sheet = pygame.image.load("imagenes/portal.png")
        self.sheet.set_clip(pygame.Rect(0, 0, 64, 64))
        self.image = pygame.transform.scale(self.sheet.subsurface(self.sheet.get_clip()),(86,86))
        self.rect = self.image.get_rect()
        self.rect.x = 35
        self.rect.y = 480
        self.rect_collision = pygame.Rect(self.rect.left + 32, self.rect.top + 40, 10, 10)
        print(self.rect_collision)
        self.frame = 0
        self.closing_frame = 0
        self.closed_frame = False
        self.standing_states = {0: (0,0,64,64), 1: (64,0,64,64), 2: (128,0,64,64), 3:(192,0,64,64), 4:(256,0,64,64), 5:(320,0,64,64), 6:(384,0,64,64), 7:(448,0,64,64)}
        self.closed_states = {0: (0,128,64,64), 1: (64,128,64,64), 2: (128,128,64,64), 3:(192,128,64,64), 4:(256,128,64,64), 5:(320,128,64,64), 6:(384,128,64,64)}

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
    
    def get_closing_frame(self, frame_set):
        self.closing_frame += 1
        if self.closing_frame > (len(frame_set) - 1):
            self.closing_frame = 6
            self.closed_frame = True
        return frame_set[self.closing_frame]

def laberinto_game():
    pygame.init()
    size = (700,700)
    font = pygame.font.SysFont(None,50)
    #player
    velocity_player = 1 #----
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Laberinto")
    clock = pygame.time.Clock()
    game_over = False
    is_moving = False #------
    first_move = False #-----
    hurt_animation = False
    in_portal = False#-----
    input_enabled = True
    game_time = 0
    time_elapsed_player = 0 # variable para contar el tiempo transcurrido
    time_elapsed_background = 0 # variable para contar el tiempo transcurrido
    time_elapsed_portal = 0
    time_elapsed_hurt = 0
    anim_delay = 100 # tiempo en milisegundos antes de actualizar la animación
    anim_background_delay = 1000
    anim_portal_delay = 100
    anim_hurt_delay = 800
    mochi1 = mochi(50,110)
    background1 = background()
    portal1 = portal()
    scale_percent = 1 #------
    pygame.mixer.init()
    walk_sound = pygame.mixer.Sound('sonidos/walk.mp3')
    walk_sound.set_volume(0.5)
    walk_sound_flag = False #---------
    hurt_sound = pygame.mixer.Sound('sonidos/auch2.wav')
    hurt_sound.set_volume(0.5)
    hurt_sound_flag = False #---------
    enter_portal_sound = pygame.mixer.Sound('sonidos/portal.mp3')
    enter_portal_sound_flag = False #---------
    pygame.mixer.music.load("sonidos/fondo_lab.mp3")
    pygame.mixer.music.play(-1)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if input_enabled == True and event.type == pygame.KEYDOWN:
                first_move = True
                if event.key == pygame.K_UP:
                    mochi1.vel_x = 0
                    mochi1.vel_y = -velocity_player
                    is_moving = True
                if event.key == pygame.K_DOWN:
                    mochi1.vel_x = 0
                    mochi1.vel_y = velocity_player
                    is_moving = True
                if event.key == pygame.K_LEFT:
                    mochi1.vel_y = 0
                    mochi1.vel_x = -velocity_player
                    mochi1.direction = 'left'
                    is_moving = True
                if event.key == pygame.K_RIGHT:
                    mochi1.vel_y = 0
                    mochi1.vel_x = velocity_player
                    mochi1.direction = 'right' 
                    is_moving = True

        time_elapsed_player += clock.get_time()
        time_elapsed_background += clock.get_time()
        time_elapsed_portal += clock.get_time()
        
        if first_move:
            game_time += clock.get_time() / 1000

        if is_moving:
            if walk_sound_flag == False:
                pygame.mixer.Sound.play(walk_sound, loops = -1)
                walk_sound_flag = True
            if time_elapsed_player > anim_delay:
                mochi1.sheet.set_clip(pygame.Rect(mochi1.get_frame(mochi1.states)))
                time_elapsed_player = 0
        else:
            mochi1.sheet.set_clip(pygame.Rect(37,15,21,19))
            walk_sound_flag = False
            pygame.mixer.Sound.stop(walk_sound)
            
        if in_portal == False:  
            if mochi1.direction == 'right':
                mochi1.image = pygame.transform.scale(mochi1.sheet.subsurface(mochi1.sheet.get_clip()),(31,28))
            if mochi1.direction == 'left':
                mochi1.image = pygame.transform.flip(pygame.transform.scale(mochi1.sheet.subsurface(mochi1.sheet.get_clip()),(31,28)), True, False)

        background1.image = pygame.transform.scale(background1.sheet.subsurface(background1.sheet.get_clip()),(700,700))
        if time_elapsed_background > anim_background_delay:
            background1.sheet.set_clip(pygame.Rect(background1.get_frame(background1.states)))
            time_elapsed_background = 0

        portal1.image = pygame.transform.scale(portal1.sheet.subsurface(portal1.sheet.get_clip()),(86,86))
        if time_elapsed_portal > anim_portal_delay and in_portal == False:
            portal1.sheet.set_clip(pygame.Rect(portal1.get_frame(portal1.standing_states)))
            time_elapsed_portal = 0

        mochi1.rect.x = mochi1.rect.x + mochi1.vel_x
        mochi1.rect.y = mochi1.rect.y + mochi1.vel_y
        window.blit(background1.image,background1.rect)
        wall_list = walls(window)
        #collisions
        # for wall in wall_list:
        #     if mochi1.rect.colliderect(wall):
        #         hurt_animation = True

        if mochi1.rect.colliderect(portal1.rect_collision):
            in_portal = True

        if mochi1.rect.colliderect(pygame.Rect(0,100,1,45)):
            mochi1.rect.x += 1
            is_moving = False

        #animations
        #character collide with walls
        if hurt_animation == True:
            if hurt_sound_flag == False:
                pygame.mixer.Sound.play(hurt_sound)
                hurt_sound_flag = True
            time_elapsed_hurt += clock.get_time()
            input_enabled = False
            if mochi1.direction == 'right':
                    mochi1.image = pygame.transform.scale(mochi1.sheet_hurt.subsurface(mochi1.sheet_hurt.get_clip()),(31,28))
            if mochi1.direction == 'left':
                mochi1.image = pygame.transform.flip(pygame.transform.scale(mochi1.sheet_hurt.subsurface(mochi1.sheet_hurt.get_clip()),(31,28)), True, False)
            window.blit(mochi1.image,mochi1.rect)
            mochi1.vel_x = 0
            mochi1.vel_y = 0
            if time_elapsed_hurt > anim_hurt_delay:
                print("hurt",time_elapsed_hurt)    
                mochi1.rect.x = 50
                mochi1.rect.y = 110
                is_moving = False
                hurt_animation = False
                input_enabled = True
                time_elapsed_hurt = 0
                hurt_sound_flag = False
                if mochi1.direction == 'left':
                    mochi1.direction = 'right'

        if time_elapsed_portal > anim_portal_delay and in_portal and portal1.closed_frame == False:
            if enter_portal_sound_flag == False:
                is_moving = False
                pygame.mixer.Sound.play(enter_portal_sound)
                enter_portal_sound_flag = True
            input_enabled = False
            mochi1.vel_x = 0
            mochi1.vel_y = 0
            portal1.sheet.set_clip(pygame.Rect(portal1.get_closing_frame(portal1.closed_states)))
            time_elapsed_portal = 0
            if scale_percent >= 0.3:
                scale_percent -= 0.18
            else:
                scale_percent = 0
            mochi1.image = pygame.transform.scale(mochi1.image,(int(mochi1.rect.width * scale_percent), int(mochi1.rect.height * scale_percent)))

        if portal1.closed_frame:
            text_surface = font.render("¡¡YOU WIN!!", True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.center = (size[0] // 2, size[1] // 2 - 40)
            time_text = font.render("Time: {}:{}".format(int(game_time//60),round(game_time % 60,2)), True, (255, 255, 255))
            time_rect = time_text.get_rect()
            time_rect.center = (size[0] // 2, size[1] // 2 + 40)
            window.blit(text_surface, text_rect)
            window.blit(time_text, time_rect)
            pygame.display.update()
            pygame.mixer.music.load('sonidos/finish.mp3')
            pygame.mixer.music.play(0)
            for i in range(180): # pausa de 2 segundos (60 ticks x 2)
                    pygame.time.delay(16) # espera 16 milisegundos (aproximadamente 1 tick a 60 fps)
                    pygame.display.update()
            game_over = True
            pygame.quit()
            os.system("py -m menu.py")
            sys.exit()

        #counter
        minutes = int(game_time // 60)
        seconds = int(game_time % 60)
        time_str = f"{minutes}:{seconds}"
        text = font.render(time_str, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (530,50)

        #draw zone
        window.blit(portal1.image,portal1.rect)
        window.blit(mochi1.image,mochi1.rect)
        window.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()  

laberinto_game()

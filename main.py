import pygame
import os
import random
 
# These are the dimensions of the background image for our game
screen_length = 600
screen_height = 427 
dim_field = (screen_length, screen_height)

screen = pygame.display.set_mode(dim_field)
	
background = pygame.image.load(os.path.join("assets","background.jpg"))
background = pygame.transform.scale(background, dim_field)


(x, y) = (200, 200)
(width, height) = (24, 26)

rect_player_1 = pygame.Rect(x, y, width, height)
rect_player_1.topleft = (10, screen_height - 50)
# Location 1

floor = pygame.Rect(0, screen_height - 10, screen_length, 10)


platform_1 = pygame.Rect(10, 310, 200, 10)
platform_2 = pygame.Rect(200, 210, 100, 10)
platform_3 = pygame.Rect(300, 120, 50, 10)

final = pygame.Rect(screen_length - 75, 50, 75, 10)
flag_rect = pygame.Rect(screen_length - 60, 5, 50, 50)

platform_list = [floor, platform_1, platform_2, platform_3, final]

'''Creating Players'''

player = pygame.image.load(os.path.join("assets", "player.png")).convert()
player.set_colorkey((101, 141, 209))

'''Creating Flag'''
flag = pygame.image.load(os.path.join("assets", "flag.png"))
(w2,h2) = flag.get_size()
(w2,h2) = (w2//8,h2//8)
flag = pygame.transform.scale(flag,(w2,h2))

# Game loop
clock = pygame.time.Clock()
running = True
FPS = 60

step_size_hor = 0
step_size_ver = 0

dx = 4
dx1 = -3
dx2 = 2

while running:
    clock.tick(FPS)
    player = pygame.image.load(os.path.join("assets", "player.png")).convert()
    player.set_colorkey((101, 141, 209))
  
    # Location 2
    # Processing events
    for event in pygame.event.get():
      # Quit game
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q:
                running = False
            # elif event.key == pygame.K_LEFT:
            #         step_size_hor = -2
            # elif event.key == pygame.K_RIGHT:
            #         step_size_hor = 2
        
    step_size_hor = 0

    index = rect_player_1.collidelist(platform_list)

    if index == 4:
        running = False
        print("You Win!")
    
    # Location 3
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_LEFT]:
	    # move the rect_player to the left by step_size
        if rect_player_1.left >= 8:
            step_size_hor = -4
        elif rect_player_1.left >=0:
            step_size_hor = -rect_player_1.left

    if keys[pygame.K_RIGHT]:
	    # move the rect_player to the right by step_size
        if rect_player_1.right < screen_length - 8:
            step_size_hor = 4
        elif rect_player_1.right <= screen_length:
            step_size_hor = (screen_length - rect_player_1.right)

    if index != -1:
        if keys[pygame.K_UP] and step_size_ver >= 0:
            step_size_ver = -10
    else:
        player = pygame.image.load(os.path.join("assets", "player_jump.png")).convert()
        player.set_colorkey((101, 141, 209))

        
        if step_size_ver <= 19.5:
            step_size_ver += 0.5
        for rect in platform_list:
            if rect_player_1.right > rect.left and rect_player_1.left < rect.right and rect.top - rect_player_1.bottom < step_size_ver and rect_player_1.bottom < rect.bottom:
                rect_player_1.move_ip(step_size_hor, rect.top - rect_player_1.bottom + 1)
                step_size_ver = 0
        

    '''Have platforms move side to side'''
    if platform_1.right > 550:
        dx = -dx
    elif platform_1.left < 10:
        dx = -dx

    if platform_2.right > 550:
        dx1 = -dx1
    elif platform_2.left < 10:
        dx1 = -dx1

    if platform_3.right > 550:
        dx2 = -dx2
    elif platform_3.left < 10:
        dx2 = -dx2
    
    rect_player_1.move_ip(step_size_hor, step_size_ver)
    platform_1.move_ip(dx, 0)
    platform_2.move_ip(dx1, 0)
    platform_3.move_ip(dx2, 0)
    
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, (0, 255,0), floor)
    pygame.draw.rect(screen, (0, 0, 255), platform_1)
    pygame.draw.rect(screen, (0, 0, 200), platform_2)
    pygame.draw.rect(screen, (0, 0, 255), platform_3)
    pygame.draw.rect(screen, (255,0,0), final)
    screen.blit(player, rect_player_1)
    screen.blit(flag, flag_rect)
    pygame.display.update()

# pygame.display.quit()
# pygame.quit()
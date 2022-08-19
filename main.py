import pygame
import os
 
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
rect_player_1.topleft = (200, 100)
# Location 1

platform_1 = pygame.Rect(0, screen_height - 10, screen_length, 10)
platform_2 = pygame.Rect(200, 300, 200, 10)

platform_list = [platform_1, platform_2]

'''Creating Players'''

player = pygame.image.load(os.path.join("assets", "player.png")).convert()
player.set_colorkey((101, 141, 209))

# Game loop
clock = pygame.time.Clock()
running = True
FPS = 60

step_size_hor = 0
step_size_ver = 0

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

    
    # Location 3
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
	    # move the rect_player to the left by step_size
        if rect_player_1.left >= 8:
            step_size_hor = -8
        elif rect_player_1.left >=0:
            step_size_hor = -rect_player_1.left

    if keys[pygame.K_RIGHT]:
	    # move the rect_player to the right by step_size
        if rect_player_1.right < screen_length - 8:
            step_size_hor = 8
        elif rect_player_1.right <= screen_length:
            step_size_hor = (screen_length - rect_player_1.right)

    
    if index != -1:
        step_size_ver = 0
        if keys[pygame.K_UP]:
            step_size_ver = -15
    else:
        player = pygame.image.load(os.path.join("assets", "player_jump.png")).convert()
        player.set_colorkey((101, 141, 209))
        if (rect_player_1.right < 205 or rect_player_1.left > 405) or (rect_player_1.bottom < 310 and (rect_player_1.right > 200 and rect_player_1.left < 400)):
            if step_size_ver <= 17:
                step_size_ver += 0.5
            elif rect_player_1.bottom > screen_height - 20:
                step_size_ver = (screen_height - 10) - rect_player_1.bottom
            else:
                step_size_ver = 20
        else:
            step_size_ver = 10
            if keys[pygame.K_UP]:
                if ((platform_2.bottom - rect_player_1.top) > 10):
                    step_size_ver = -10
                else:
                    step_size_ver = platform_2.bottom - rect_player_1.top
            


    rect_player_1.move_ip(step_size_hor, step_size_ver)
    
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, (0, 255,0), platform_1)
    pygame.draw.rect(screen, (0, 0, 255), platform_2)
    # pygame.draw.rect(screen, (255,0,0), rect_player_1)
    screen.blit(player, rect_player_1)
    pygame.display.update()

# pygame.display.quit()
# pygame.quit()
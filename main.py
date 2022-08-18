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
rect_player_1.topleft = (150,50)
# Location 1

'''Creating Players'''

# Game loop
clock = pygame.time.Clock()
running = True
FPS = 60

step_size_l_r = 0
step_size_u_d = 0

while running:
    clock.tick(FPS)
  
    # Location 2
    # Processing events
    for event in pygame.event.get():
      # Quit game
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q:
                running = False
            # elif event.key == pygame.K_LEFT:
            #         step_size_l_r = -2
            # elif event.key == pygame.K_RIGHT:
            #         step_size_l_r = 2
                
    # rect_player_1.move_ip(step_size_l_r, step_size_u_d)
    
    # Location 3
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
	    # move the rect_player to the left by step_size
        if rect_player_1.left >=12:
            step_size_l_r = -12
            rect_player_1.move_ip(step_size_l_r, step_size_u_d)
        elif rect_player_1.left >=0:
            step_size_l_r = -rect_player_1.left
            rect_player_1.move_ip(step_size_l_r, step_size_u_d)

    if keys[pygame.K_RIGHT]:
	    # move the rect_player to the left by step_size
        if rect_player_1.right <= screen_length - 12:
            step_size_l_r = 12
            rect_player_1.move_ip(step_size_l_r, step_size_u_d)
        elif rect_player_1.right <= screen_length:
            step_size_l_r = (screen_length - rect_player_1.right)
            rect_player_1.move_ip(step_size_l_r, step_size_u_d)
  
    screen.blit(background, (0,0))
    pygame.draw.rect(screen, (255,0,0), rect_player_1)
    pygame.display.update()

# pygame.display.quit()
# pygame.quit()
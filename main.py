import pygame
from sys import exit
import math
from random import randint, choice
from Obstacle import Obstacle
from Player import Player
import setup

# methods
# function to consistantly update and redraw score_surface
def display_score():
    current_time = (pygame.time.get_ticks() - start_time) / 1000
    score_surface = setup.test_font.render(f"Score: {math.floor(current_time)}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(midtop = (400, 27))
    setup.screen.blit(score_surface, score_rect)
    return current_time

# checks to see if a collision has occured between sprites, returns boolean value (to game_active)
    # spritecollide(sprite_to_check, group_to_check, dokill) returns list of collided sprites
        # if dokill is set to true on contact the group sprite would be deleted
def collision_sprite():
    sprite_to_check = setup.player.sprite
    group_to_check = setup.obstacle_group
    dokill = False
    if pygame.sprite.spritecollide(sprite_to_check, group_to_check, dokill):
        setup.obstacle_group.empty()
        return False
    else:
        return True


# game loop
while True:
    # event loop
    for event in pygame.event.get():
        # if user clicks the window close button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if setup.game_active:      
            # timers
            # enemy/obstacle deployment timer 
            if event.type == setup.obstacle_timer:
                # add an instance of Obstacle to obstacle_group, the type is random 25%chance fly 75% chance snail
                setup.obstacle_group.add(Obstacle(choice(["fly", "snail", "snail", "snail"])))
        else:
            # user presses space bar to restart game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    setup.game_active = True
                    # snail_rect.left = 800
                    start_time = pygame.time.get_ticks()
        
    # game display
    if setup.game_active:
        # if score is 0 (new game) start bg music and loop it forever
        if setup.music_on == False:
            pygame.mixer.music.play(-1)
            setup.music_on = True
            
        # display sky_surface
        sky_pos_x = 0
        sky_pos_y = 0
        setup.screen.blit(setup.sky_surface, (sky_pos_x, sky_pos_y))

        # # display moving ground_surface
        rel_x = setup.ground_surface_x % setup.ground_surface.get_rect().width
        setup.screen.blit(setup.ground_surface, (rel_x - setup.ground_surface.get_rect().width, 300))
        if rel_x < setup.screen_width:
            setup.screen.blit(setup.ground_surface, (rel_x, 300))
        setup.ground_surface_x -= 1

        # store score and display
        setup.score = display_score()
        # display player
        setup.player.draw(setup.screen)
        setup.player.update()
        # display obstacles
        setup.obstacle_group.draw(setup.screen)
        setup.obstacle_group.update()

        # checks to see if collision has occured, if collision game_active is turned to False ending the game
        setup.game_active = collision_sprite()

    # if game_active is false(new game/player death) display intro/game over screen
    else:
        pygame.mixer.music.pause()
        setup.music_on = False
        # draw screen
        setup.screen.fill((94, 129, 162))
        setup.screen.blit(setup.player_stand, setup.player_stand_rect)
        score_msg = setup.test_font.render(f"Your score: {math.floor(setup.score)}", False, (111, 196, 169))
        score_msg_rect = score_msg.get_rect(center = (400, 330))
        setup.screen.blit(setup.game_name, setup.game_name_rect)
        # if no score prompt to start game, if score display score
        if setup.score == 0:
            setup.screen.blit(setup.game_msg, setup.game_msg_rect)
        else:
            setup.screen.blit(score_msg, score_msg_rect)

    # update what is displayed on screen
    pygame.display.update()
    # sets so that while True loop should not run faster than framerate_ceiling times per second
    framerate_ceiling = 60
    setup.clock.tick(framerate_ceiling)













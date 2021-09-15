import pygame
from Obstacle import Obstacle
from Player import Player

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


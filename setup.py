import pygame, math
from Player import Player


# setup
# initialize pygame
pygame.init()
# setup display surface
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
# rename screen title
pygame.display.set_caption("Pixel Runner")
# controlling the framerate
clock = pygame.time.Clock()
# creating a font
font_type = "font/Pixeltype.ttf"
font_size = 50
test_font = pygame.font.Font(font_type, font_size)
# Setting up game states
    # setting to false starts game from intro/game over screen
game_active = False
# building to be able to reset the score/timer count to zero with new game
start_time = 0
# store the score for global use
score = 0
# bg music
path_to_music = "audio/Juhani_Junkala_[Retro_Game_Music_Pack]_Level_1.wav"
pygame.mixer.music.load(path_to_music)
# set sound volume. Between 0(silent) and 1(full volume)
pygame.mixer.music.set_volume(0.2)
# create a GroupSingle instance of Player 
player = pygame.sprite.GroupSingle()
player.add(Player())
# create a sprite group for obstacles
obstacle_group = pygame.sprite.Group()

# create a surface with an image
sky_surface = pygame.image.load('img/Sky.png').convert()

# create a ground surface with an image
ground_surface = pygame.image.load('img/ground.png').convert()
# ground_surface_rect = ground_surface.get_rect(topleft = (0, 300))
ground_surface_x = 0

# creating the intro/game over screen
# creating player surface for game over/intro screen
player_stand = pygame.image.load("img/player/player_stand.png").convert_alpha()
pss_surface_to_use = player_stand
pss_rotation_angle = 0
pss_scale = 2
player_stand = pygame.transform.rotozoom(pss_surface_to_use, pss_rotation_angle, pss_scale)
player_stand_rect = player_stand.get_rect(center = (400, 200))

# game name to be displayed
game_name = test_font.render("Pixel Runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

# message to be shown if score = 0 (ie new game)
game_msg = test_font.render("Press space to run", False, (111, 196, 169))
game_msg_rect = game_msg.get_rect(center = (400, 330))


# timers
# controls when new obstacles are generated
obstacle_timer = pygame.USEREVENT + 1
event_to_trigger = obstacle_timer
how_often_to_trigger = 1500
pygame.time.set_timer(event_to_trigger, how_often_to_trigger)

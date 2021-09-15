import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # animating the player
        player_walk_1 = pygame.image.load("img/player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("img/player/player_walk_2.png").convert_alpha()
        # list containing the two walk animation pics controlled by player_index
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("img/player/jump.png").convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

        path_to_sound = "audio/jump.mp3"
        self.jump_sound = pygame.mixer.Sound(path_to_sound)
        # set sound volume. Between 0(silent) and 1(full volume)
        self.jump_sound.set_volume(0.2)

    def player_input(self):
        keys = pygame.key.get_pressed()
        # if player is on the ground and space bar is pressed player jump
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -21
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        # creates appearance of solid floor
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        # display jump surface when player is in the air
        if self.rect.bottom < 300:
            self.image = self.player_jump
        # play walking animation if the player is on the floor    
        else:
            # increasing the index by small increments extends how many frames an index position is displayed for
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


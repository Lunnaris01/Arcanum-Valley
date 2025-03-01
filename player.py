import pygame
from sprite import Sprite
from input import is_key_pressed
from camera import set_camera_center

class Player(Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.movement_speed = 1
        set_camera_center(x,y)

    def update(self):
        if is_key_pressed(pygame.K_w):
            self.y -= self.movement_speed
        if is_key_pressed(pygame.K_d):
            self.x += self.movement_speed
        if is_key_pressed(pygame.K_s):
            self.y += self.movement_speed
        if is_key_pressed(pygame.K_a):
            self.x -= self.movement_speed
        set_camera_center(self.x,self.y)
import pygame
from mods.vector import Vector2

class Entity:
    sprite = None
    collider = None
    hitbox = None

    def __init__(self, sprite, collider, hitbox, position) -> None:
        self.sprite = sprite
        self.collider = collider
        self.hitbox = hitbox
        self.position = position

####################
# CONTROLS
####################
class Controls:
    def __init__(self, speed:int, jump_power:int, up:int,down:int,left:int,right:int,jump:int):
        self.speed = speed
        self.jump_power = jump_power

        self.up=up
        self.down=down
        self.left=left
        self.right=right
        self.jump=jump

    def get_key_just_pressed(self, key:int):
        pass

class SideScrollControls(Controls):
    pass

class BirdseyeControls(Controls):
    def return_controls(self, window) -> bool:
        w = False
        a = False
        s = False
        d = False

        if window.is_key_held(self.up):
            w = True
        if window.is_key_held(self.down):
            s = True
        if window.is_key_held(self.left):
            a = True
        if window.is_key_held(self.right):
            d = True

        return w, a, s, d

class Player(Entity):
    def __init__(self, sprite, collider, hitbox, position, controls=BirdseyeControls(300, 100, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE)) -> None:
        # Super the abstract Entity class
        super().__init__(sprite, collider, hitbox, position)

        self.controls = controls

    def warp_to(self, position):
        self.position = position

    def move(self, window):
        w, a, s, d = self.controls.return_controls(window)

        # Up-down
        if w:
            self.warp_to(Vector2(self.position.x, self.position.y - (self.controls.speed * window.delta)))
        elif s:
            self.warp_to(Vector2(self.position.x, self.position.y + (self.controls.speed * window.delta)))

        # Left-right
        if a:
            self.warp_to(Vector2(self.position.x - (self.controls.speed * window.delta), self.position.y))
        elif d:
            self.warp_to(Vector2(self.position.x + (self.controls.speed * window.delta), self.position.y))

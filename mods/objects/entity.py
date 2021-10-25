import pygame

class Entity:
    sprite = None
    collider = None
    hitbox = None

    def __init__(self, sprite, collider, hitbox) -> None:
        self.sprite = sprite
        self.collider = collider
        self.hitbox = hitbox

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



        return False, False, False, False


class Player(Entity):
    def __init__(self, sprite, collider, hitbox, controls=BirdseyeControls(100, 100, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE)) -> None:
        # Super the abstract Entity class
        super().__init__(sprite, collider, hitbox=hitbox)

        self.controls = controls

    def move(self, window):
        pass


##################
# IMPORTS
##################
import pygame
from mods.vector import Vector2

#############################################################
# ENTITIES
# Basic entity class. All different entites extend this.
# AI is only implemented on EnemyEntity, AllyEntity, and
# NeutralEntity.
class Entity:
    # Base values
    sprite = None
    collider = None
    hitbox = None

    # Initiate the Entity class
    def __init__(self, sprite, collider, hitbox, position) -> None:
        self.sprite = sprite
        self.collider = collider
        self.hitbox = hitbox
        self.position = position

####################
# CONTROLS
####################
# The base controls class.
class Controls:
    def __init__(self, speed:int, jump_power:int, up:int,down:int,left:int,right:int,jump:int):
        # Set speed and jump power
        self.speed = speed
        self.jump_power = jump_power

        # Set the movement keys
        self.up=up
        self.down=down
        self.left=left
        self.right=right
        self.jump=jump

# SideScrolling controls, use for platformers. Not implemented yet.
class SideScrollControls(Controls):
    pass

class BirdseyeControls(Controls):
    def return_controls(self, window):
        # Get the actual controls
        w = False
        a = False
        s = False
        d = False

        # Get all input
        if window.is_key_held(self.up):
            w = True
        if window.is_key_held(self.down):
            s = True
        if window.is_key_held(self.left):
            a = True
        if window.is_key_held(self.right):
            d = True

        return w, a, s, d


#########################################################################
# PLAYER
# This is the player class. The player is what the user will control
# directly. The only parameter you don't need to set is the controls.
#
class Player(Entity):
    # Initiate the player, setting all the data variables such as controls.
    def __init__(self, sprite, collider, hitbox, position, controls=BirdseyeControls(300, 100, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE)) -> None:
        # Super the abstract Entity class
        super().__init__(sprite, collider, hitbox, position)

        # Set the controls
        self.controls = controls

    # Teleport the player
    def warp_to(self, position):
        self.position = position

    # Move the player. This is using the controls variable.
    def move(self, window):
        w, a, s, d = self.controls.return_controls(window)

        # Up-down movement
        if w:
            self.warp_to(Vector2(self.position.x, self.position.y - (self.controls.speed * window.delta)))
        elif s:
            self.warp_to(Vector2(self.position.x, self.position.y + (self.controls.speed * window.delta)))

        # Left-right movement
        if a:
            self.warp_to(Vector2(self.position.x - (self.controls.speed * window.delta), self.position.y))
        elif d:
            self.warp_to(Vector2(self.position.x + (self.controls.speed * window.delta), self.position.y))

##################
# IMPORTS
##################
import pygame
from mods.vector import Vector2
import mods.objects.collider as collider

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
    position = None

    # Initiate the Entity class
    def __init__(self, sprite, c, hitbox, position) -> None:
        self.sprite = sprite
        self.collider = c
        self.hitbox = hitbox
        self.position = position

        self.collider.warp(position)

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
    def __init__(self, sprite, collide, hitbox, position, controls=BirdseyeControls(300, 100, pygame.K_w, pygame.K_s, pygame.K_a,
                                                           pygame.K_d, pygame.K_SPACE), c_lock:bool=False) -> None:
        # Super the abstract Entity class
        super().__init__(sprite, collide, hitbox, position)

        # Set the controls
        self.controls = controls
        self.c_lock = c_lock

        # If the camera is locked
        if c_lock:
            self.sprite.is_plr = True

    # Teleport the player
    def warp_to(self, position, window=None):
        if window is not None and self.c_lock == True:
            window.change_offset(position)
            return

        self.position = position
        self.collider.warp(self.position)

    def check_collision(self, colliders, direc:int, window):
        for i in range(len(colliders)):
            if direc == 0:
                if colliders[i].is_colliding(self.collider.ghost_move(Vector2(self.position.x, self.position.y - (self.controls.speed * window.delta))), self): return True
            if direc == 1:
                if colliders[i].is_colliding(self.collider.ghost_move(Vector2(self.position.x, self.position.y + (self.controls.speed * window.delta))), self): return True
            if direc == 2:
                if colliders[i].is_colliding(self.collider.ghost_move(Vector2(self.position.x - (self.controls.speed * window.delta), self.position.y)), self): return True
            if direc == 3:
                if colliders[i].is_colliding(self.collider.ghost_move(Vector2(self.position.x + (self.controls.speed * window.delta), self.position.y)), self): return True
        return False

    # Move the player. This is using the controls variable.
    def move(self, window):
        # Fix the offset
        w, a, s, d = self.controls.return_controls(window)

        colliders = collider.colliders

        # Up-down movement
        if w:
            if self.check_collision(colliders, 0, window): return
            """
            if self.c_lock:
                self.ghost_pos = Vector2(self.ghost_pos.x, self.ghost_pos.y + (self.controls.speed * window.delta))
                return
                """
            self.warp_to(Vector2(self.position.x, self.position.y - (self.controls.speed * window.delta)))
            if self.c_lock:
                window.change_offset(self.position)
        elif s:
            if self.check_collision(colliders, 1, window): return
            """
            if self.c_lock:
                self.ghost_pos = Vector2(self.ghost_pos.x, self.ghost_pos.y - (self.controls.speed * window.delta))
                return
            """
            self.warp_to(Vector2(self.position.x, self.position.y + (self.controls.speed * window.delta)))
            if self.c_lock:
                window.change_offset(self.position)

        # Left-right movement
        if a:
            if self.check_collision(colliders, 2, window): return
            """
            if self.c_lock:
                self.ghost_pos = Vector2(self.ghost_pos.x + (self.controls.speed * window.delta), self.ghost_pos.y)
                return
                """
            self.warp_to(Vector2(self.position.x - (self.controls.speed * window.delta), self.position.y))
            if self.c_lock:
                window.change_offset(self.position)
        elif d:
            if self.check_collision(colliders, 3, window): return
            """
            if self.c_lock:
                self.ghost_pos = Vector2(self.ghost_pos.x - (self.controls.speed * window.delta), self.ghost_pos.y)
                return
            """
            self.warp_to(Vector2(self.position.x + (self.controls.speed * window.delta), self.position.y))
            if self.c_lock:
                window.change_offset(self.position)
            pass

    def __repr__(self):
        return "PLR"
from mods.vector import Vector2
import pygame

colliders = []

class RectCollider:
    # Data
    x_size = 0
    y_size = 0

    rect = None

    position = None

    trigger = False
    triggered = False

    # Warp the collider
    def warp(self, new_pos:Vector2):
        # Tried this before
        #to_warp = Vector2(new_pos.x - self.position.x, new_pos.y - self.position.y)
        #self.rect = self.rect.move(to_warp.x, to_warp.y)

        self.position = new_pos
        self.rect.x = new_pos.x
        self.rect.y = new_pos.y
        #self.rect.move_ip(self.position.x - new_pos.x, self.position.y - new_pos.y)

        """
        Position of rect: 0, 0
        Position we want to warp to: 100, 100
        
        If we do position - r_position, we get 100, 100! 
        
        
        Position of rect: 50, 100
        Position we want to warp to: 1100, 50
        
        If we do position - rposition, we get 1050, -50
        That should work...
        """

    # Return a special collider
    def ghost_move(self, newPos):
        ghost = self
        ghost.rect.x = newPos.x
        ghost.rect.y = newPos.y

        return ghost

    # Get collision
    def is_colliding(self, collider, sender):
        if self == sender.collider: return False
        if self.trigger and self.rect.colliderect(collider.rect):
            self.trigger = True
            return False

        return self.rect.colliderect(collider.rect)

    # Initiate the collider
    def __init__(self, x_size:int, y_size:int, start_pos:Vector2=Vector2(0,0), trigger:bool=False) -> None:
        self.x_size = x_size
        self.y_size = y_size
        self.position = start_pos
        self.trigger = trigger

        self.rect = pygame.Rect(start_pos.x, start_pos.y, x_size, y_size)
        colliders.append(self)
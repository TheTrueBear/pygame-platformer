from mods.vector import Vector2
import pygame

colliders = []

class RectCollider:
    # Data
    x_size = 0
    y_size = 0

    rect = None

    position = None

    # Warp the collider
    def warp(self, new_pos:Vector2):
        to_warp = Vector2(new_pos.x - self.position.x, new_pos.y - self.position.y)
        self.rect = self.rect.move(to_warp.x, to_warp.y)

        """
        Position of rect: 0, 0
        Position we want to warp to: 100, 100
        
        If we do position - r_position, we get 100, 100! 
        
        
        Position of rect: 50, 100
        Position we want to warp to: 1100, 50
        
        If we do position - rposition, we get 1050, -50
        That should work...
        """

    # Get collision
    def is_colliding(self, collider, sender):
        if self == sender.collider: return False
        print(self.rect.x)
        print(f'C:{collider.rect.x}')
        return self.rect.colliderect(collider.rect)

    # Initiate the collider
    def __init__(self, x_size:int, y_size:int, start_pos:Vector2=Vector2(0,0)):
        self.x_size = x_size
        self.y_size = y_size
        self.position = start_pos

        self.rect = pygame.Rect(start_pos.x, start_pos.y, x_size, y_size)
        colliders.append(self)
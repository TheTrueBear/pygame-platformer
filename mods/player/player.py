import mods.gfx.image as img
import mods.vector as v
import mods.gfx.color as color
import pygame

# Movement
default_movement = [
    pygame.K_w,
    pygame.K_a,
    pygame.K_s,
    pygame.K_d
]
# Binding
default_binding = [
    "up",
    "left",
    "down",
    "right"
]

# Player
class Player:
    movement = [

    ]
    bind = [

    ]
    pos = None
    image = None

    speed = 0
    dt = 0

    move_k = [False] * 250

    def warp(self, new_pos):
        self.pos = new_pos

    def get_movement(self, window):
        self.move_k = window.keys


    """
    Movement
    """
    # Left
    def left(self) -> None:
        print("l")
        self.warp(v.Vector2(self.pos.x - self.speed * self.dt, self.pos.y))

    # Right
    def right(self) -> None:
        print("r")
        self.warp(v.Vector2(self.pos.x + self.speed * self.dt, self.pos.y))

    # Up
    def up(self) -> None:
        print("u")
        self.warp(v.Vector2(self.pos.x, self.pos.y - self.speed * self.dt))

    # Down
    def down(self) -> None:
        print("d")
        self.warp(v.Vector2(self.pos.x, self.pos.y + self.speed * self.dt))

    def move(self, window) -> None:
        i = 0
        for k in self.move_k:
            if k is True:
                if self.move_k.index(k) in self.movement:
                    a = getattr(self, self.bind[ self.movement.index(i) ] )
                    a()
            i += 1
        pass
    """
    Movement
    """

    def update(self, window):
        self.dt = window.delta
        self.get_movement(window)
        self.move(window)
        window.render(self.pos, self.image)

    def __init__(self, movement:list=default_movement, bind:list=default_binding, image:img.Image=img.Image("mods/gfx/defaults/default.png"), startPos:v.Vector2=v.Vector2(0, 0), speed=100) -> None:
        self.movement = movement
        self.bind = bind
        self.pos = startPos
        self.image = image






































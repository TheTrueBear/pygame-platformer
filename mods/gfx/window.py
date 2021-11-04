import pygame
import sys

# My modules
import mods.vector as vector
import mods.gfx.color as color
import mods.gfx.image as image

class Window :
    # Screen
    screen = None

    # Values
    size = None
    name = "None"
    bgc = None
    bgi = image.Image("background.png")

    # For non-frame-rate tied calculations
    delta = 0
    # To calculate delta
    previous = 0
    now = pygame.time.get_ticks()

    # Key
    k_events = []
    keys = []

    # Framerates
    current_fps = 0
    delta_to_frame = 0.1

    # Frame-rate
    fps = 1 / 60
    frame_time = 0

    # Offset
    offset = vector.Vector2(0,0)

    # Clear the screen
    def cls(self, flags="col") -> None:
        if flags == "img":
            self.render(vector.Vector2(0, 0), self.bgi)
        else:
            pygame.draw.rect(self.screen, (self.bgc.r, self.bgc.g, self.bgc.b), (0,0, self.size.x,self.size.y))
        # pygame.draw.rect(self.screen, (self.bgc.r, self.bgc.g, self.bgc.b), (0, 0, self.size.x, self.size.y))

    # Render at the middle
    def render_mid(self, img):
        img_x = img.raw.get_width()
        img_y = img.raw.get_height()

        xpos = (self.size.x / 2) - (img_x / 2)
        ypos = (self.size.y / 2) - (img_y / 2)

        self.screen.blit(img.raw, (xpos, ypos))

    # Render an image
    def render(self, pos: vector.Vector2, img) -> None:
        if img.is_plr: self.render_mid(img); return
        self.screen.blit(img.raw, (pos.x + self.offset.x, pos.y + self.offset.y))

    # Update the window
    def update(self) -> None:
        # Frame update
        if self.frame_time >= self.fps:
            self.current_fps = round(1 / self.delta_to_frame)
            self.delta_to_frame = 0
            pygame.display.update()
            self.frame_time -= self.fps

            events = pygame.event.get()
            for event in events:
                # Input
                self.keys = pygame.key.get_pressed()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # Clear screen
        self.cls()

        # Get delta
        self.previous = self.now
        self.now = pygame.time.get_ticks()
        self.delta = (self.now - self.previous) / 1000.0
        self.delta_to_frame += self.delta

        # Set frame-rate
        self.frame_time += self.delta

    # Input
    def is_key_held(self, key:int) -> bool:
        return self.keys[key]

    def change_offset(self, offset):
        self.offset = vector.Vector2(-offset.x + (self.size.x / 2) - 16, -offset.y + (self.size.y / 2) - 16)

    def __init__(self, size : vector.Vector2, bgc : color.Color3 = color.Color3(255, 0, 255), name : str = "Default", icon:image.Image = image.Image("mods/gfx/defaults/default.png"), framerate:int=60) -> None:
        # Set attributes
        self.size = size
        self.bgc = bgc
        self.name = name

        # Frame-rate
        self.fps = 1 / framerate

        # Make the screen
        self.screen = pygame.display.set_mode((self.size.x, self.size.y))
        pygame.display.set_caption(self.name)
        pygame.display.set_icon(icon.raw)

        #
        self.bgi.transform_size(self.size)

        # Init
        pygame.init()

        # Keys
        self.keys = pygame.key.get_pressed()
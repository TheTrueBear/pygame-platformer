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

    # Clear the screen
    def cls(self) -> None:
        pygame.draw.rect(self.screen, (self.bgc.r, self.bgc.g, self.bgc.b), (0, 0, self.size.x, self.size.y))

    # Render an image
    def render(self,  pos:vector.Vector2, img:image.Image=image.Image("mods/gfx/defaults/default.png")) -> None:
        self.screen.blit(img.raw, (pos.x, pos.y))

    # Update the window
    def update(self) -> None:
        pygame.display.update()
        self.cls()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def __init__(self, size : vector.Vector2, bgc : color.Color3 = color.Color3(255, 0, 255), name : str = "Default", icon:image.Image = image.Image("mods/gfx/defaults/default.png")) -> None:
        self.size = size
        self.bgc = bgc
        self.name = name

        # Make the screen
        self.screen = pygame.display.set_mode((self.size.x, self.size.y))
        pygame.display.set_caption(self.name)
        pygame.display.set_icon(icon.raw)

        # Init
        pygame.init()
#################
# IMPORTS
#################
import pygame
from mods.gfx.color import Color3

#############################################
# A basic text-to-texture renderer. Y   ou can
# set font, text, size, and color.
class Text:
    text = ""
    font_name = ""
    size = 0
    raw = None

    color = None

    is_plr = False

    def __init__(self, font, size, text, color:Color3=Color3(0,0,0)):
        self.size = size
        self.font_name = font
        self.text = text
        self.color = color

        font_tex = pygame.font.SysFont(font, size)
        raw = font_tex.render(text, False, (color.r, color.g, color.b))
        self.raw = raw

    def modify(self, text):
        font_tex = pygame.font.SysFont(self.font_name, self.size)
        raw = font_tex.render(text, False, (self.color.r, self.color.g, self.color.b))
        self.raw = raw

import mods.vector as vec
import mods.gfx.window as wind
import mods.gfx.image as img
from mods.objects.entity import *
from mods.objects.collider import RectCollider
from mods.gfx.text import Text
import pygame

window_size = vec.Vector2(800, int((800 / 16) * 10))
window = wind.Window(window_size, name="Game", framerate=1)

image = img.Image("test.png")
image.transform_size(vec.Vector2(200, 200))

plr = Player(image, None, None, vec.Vector2(100, 0))

text = Text("Menlo", 30, "FPS:0")

print(pygame.KMOD_SHIFT)

y = 0
x = 0

while True:
    plr.move(window)
    text.modify(f'FPS:{window.delta}')

    window.render(plr.position, plr.sprite)
    window.render(vec.Vector2(0,0), text)
    window.update()
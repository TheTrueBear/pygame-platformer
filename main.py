import mods.vector as vec
import mods.gfx.window as wind
import mods.gfx.image as img
import mods.gfx.color as color
import pygame

window_size = vec.Vector2(800, int((800 / 16) * 10))
window = wind.Window(window_size, name="Game", framerate=30)

image = img.Image("test.png")
image.transform_size(vec.Vector2(400, 400))

y = 0
x = 0

while True:
    y += 100 * window.delta
    window.render(vec.Vector2(100 + x, 100 + y), img=image)
    if window.is_key_held(pygame.K_x):
        x += 100 * window.delta
    window.update()
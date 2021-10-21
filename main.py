import mods.vector as vec
import mods.gfx.window as wind
import mods.gfx.image as img
import mods.player.player as player
import pygame

window_size = vec.Vector2(800, int((800 / 16) * 10))
window = wind.Window(window_size, name="Game", framerate=30)

image = img.Image("test.png")
image.transform_size(vec.Vector2(200, 200))

plr = player.Player(image = image)

y = 0
x = 0

while True:


    plr.update(window)

    window.update()
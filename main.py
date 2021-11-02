import mods.vector as vec
import mods.gfx.window as wind
import mods.gfx.image as img
from mods.objects.entity import Player, Entity
from mods.world.level import Level
from mods.gfx.color import Color3
from mods.objects.collider import RectCollider
#from mods.gfx.text import Text
import pygame

window_size = vec.Vector2(800, int((800 / 16) * 10))
window = wind.Window(window_size, name="Game", framerate=60, bgc=Color3(0,0,0))

image = img.Image("plr.png", is_plr=True, is_locked=True)
#image.transform_size(vec.Vector2(200, 200))

level = Level("l1.lvl")
l_tiles = level.draw({
    "#": "test.png"
    }, 10)

plr = Player(image, RectCollider(30, 30), None, level.spawn, c_lock=True)
#entity = Entity(image, RectCollider(30, 30), None, vec.Vector2(100, 100))

print(pygame.K_DOWN)

y = 0
x = 0

while True:
    plr.move(window)
    #text.modify(f'FPS:{window.current_fps}')

    for tile in l_tiles:
        window.render(tile.position, tile.sprite)

    window.render(plr.position, plr.sprite)
    #window.render(entity.position, entity.sprite)
    #window.render(vec.Vector2(0,0), text)
    window.update()
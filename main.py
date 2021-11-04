from mods.gfx.window import Window
from mods.gfx.image import Image
from mods.gfx.color import Color3

from mods.objects.entity import Player
from mods.objects.collider import RectCollider

from mods.world.level import Level

from mods.vector import Vector2

window_size = Vector2(1200, int((1200 / 16) * 10))
window_c    = Color3(0, 0, 0)
window = Window(window_size, name="Gold Hunter", bgc=window_c, framerate=60)

level = Level("l1.lvl")
tiles = level.draw({
    "#": "background.png",
    "X": "Dig Spot.png"
}, 50)

collider = RectCollider(32, 32)
image = Image("plr.png")
player = Player(image, RectCollider(32, 32), None, Vector2(0, 0), c_lock=True)

while True:
    player.move(window)
    window.render(player.position, player.sprite)
    for tile in tiles:
        window.render(tile.position, tile.sprite)
    window.update()

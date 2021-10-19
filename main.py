import mods.vector as vec
import mods.gfx.window as wind
import mods.gfx.image as img
import mods.gfx.color as color

window_size = vec.Vector2(800, int((800 / 16) * 10))
window = wind.Window(window_size, name="Game")

image = img.Image("test.png")
image.transform_size(vec.Vector2(400, 400))

while True:
    window.render(vec.Vector2(100, 100), img=image)
    window.update()
from mods.gfx.image import Image
from mods.vector import Vector2
from mods.objects.collider import RectCollider
from mods.objects.entity import Entity

class Level:
    lines = []
    spawn = Vector2(0,0)

    def __init__(self, path):
        level = open(path, "r")
        level_raw = level.read()
        level.close()

        lines = [[]]

        x = False
        line = 0
        newl = True
        i = 0

        while x == False:
            # Try to set the current level character
            try:
                current = level_raw[i]
            # Otherwise, level is loaded
            except:
                break

            # If it is a new line
            if current.isspace() and current != " ":
                lines.append([])
                line += 1

            # Add to the line
            else:
                lines[line].append(current)


            i += 1

        self.lines = lines

    def draw(self, key, size) -> list:
        tiles = []
        for line in range(len(self.lines)):
            for tile in range(len(self.lines[line])):
                if self.lines[line][tile] != " " and self.lines[line][tile] != "0":
                    tile_sprite = Image(key[self.lines[line][tile]])
                    tile_sprite.transform_size(Vector2(50, 50))

                    cur_tile = Entity(tile_sprite, RectCollider(50, 50), None, Vector2(tile * 50, line * 50))
                    tiles.append(cur_tile)
                if self.lines[line][tile] == "0":
                    self.spawn = Vector2(tile * 50, line * 50)

        return tiles

    def __repr__(self):
        return self.lines

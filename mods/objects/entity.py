class Entity:
    sprite = None
    collider = None
    hitbox = None

    def __init__(self, sprite, collider, hitbox=collider) -> None:
        self.sprite = sprite
        self.collider = collider
        self.hitbox = hitbox

####################
# CONTROLS
####################
class Controls:
    def __init__(self, speed:int, jump_power:int, up:int,down:int,left:int,right:int,jump:int):
        self.speed = speed
        self.jump_power = jump_power

        self.up=up
        self.down=down
        self.left=left
        self.right=right
        self.jump=jump

    def get_key_just_pressed(self, key:int):
        pass

class SideScrollControls(Controls):
    pass

class BirdseyeControls(Controls):
    pass


class Player(Entity):
    pass
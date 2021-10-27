colliders = []

class RectCollider:
    top = 0
    right = 0
    bottom = 0
    left = 0

    x_size = 0
    y_size = 0

    def move(self, newPos):
        self.top += newPos.y
        self.bottom += newPos.y
        self.left += newPos.x
        self.right += newPos.x

    def warp(self, newPos):
        pass

    def is_colliding(self, coll, sender):
        x_col = False
        y_col = False
        col = False

        print(f'TOP: {self.top}, THAT AREA: {coll.top},{coll.bottom}, BOTTOM: {self.bottom}')

        if self.left <= coll.left <= self.right   and   self.right <= coll.right <= self.left: x_col = True
        if self.top <= coll.top <= self.bottom   and   self.bottom <= coll.bottom <= self.top: y_col = True

        return x_col and y_col

    def __init__(self, top, bottom, left, right):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

        colliders.append(self)
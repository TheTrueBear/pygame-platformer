class RectCollider:
    top = 0
    right = 0
    bottom = 0
    left = 0

    def move(self, newPos):
        self.top += newPos.y
        self.bottom += newPos.y
        self.left += newPos.x
        self.right += newPos.x

    def is_colliding(self, obj):
        x_col = False
        y_col = False
        if self.right >= obj.x >= self.left:
            x_col = True
        if self.top >= obj.y >= self.bottom:
            y_col = True

        return x_col, y_col

    def __init__(self, top, bottom, left, right):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
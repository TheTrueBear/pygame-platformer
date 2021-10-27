class Vector2:
    x=0
    y=0

    def mult(self, size:int=1):
        self.x *= size
        self.y *= size

    def __init__(self, x, y) -> None:
        self.x=x
        self.y=y

    def __repr__(self):
        return self.x, self.y
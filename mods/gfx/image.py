"""

The image class. Use this in all the rendering as we need images for it all.
If you want to access the raw image, get your variable and get the property
"raw" on it. Example:

img = image.Image("say.png")
print(img.raw)

That will print the image's raw data.

"""



import pygame

class Image :
    raw = None
    old_variants = []
    path = ""

    lock = False
    is_plr = False

    # Resize the image
    def transform_size(self, new_size) -> None:
        self.old_variants.append(self.raw)
        self.raw = pygame.transform.scale(self.raw, (new_size.x, new_size.y))

    # Return all the old variants
    def get_variants(self) -> list:
        return self.old_variants

    # Initiate the class
    def __init__(self, path:str, is_plr:bool=False, is_locked:bool=False) -> None:
        self.path = path
        self.raw = pygame.image.load(self.path)
        self.lock = is_locked
        self.is_plr=is_plr

    def __repr__(self):
        return self.raw
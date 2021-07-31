from ursina import *

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,     # Specifies sky parent to scale properly
            model = 'cube',
            color = color.rgb(115, 180, 255),
            scale = 1000,
            double_sided = True # See the sphere when you are inside it
        )

from ursina import *

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,     # Specifies sky parent to scale properly
            model = 'sphere',
            texture = '../resources/skybox.jpg',
            scale = 1000,
            double_sided = True # See the sphere when you are inside it
        )

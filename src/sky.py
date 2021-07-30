from ursina import *

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,     # Specifies parent of sky so it scales properly
            model = 'sphere',
            texture = '/resources/skybox.jpg',
            scale = 1000,       # Increases size drastically
            double_sided = True # See the sphere when you are in it
        )

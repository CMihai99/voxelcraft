from ursina import *

class Arm(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui, # Specifies parent of the arm which is the player
            model = './resources/player/arm/models/arm',
            texture = './resources/player/arm/textures/arm.png',
            scale = 0.2,
            rotation = Vec3(160,-5,0),
            position = Vec2(0.5,-0.6)
        )

    # Arm animations
    def active(self):
        self.rotation = Vec3(160,-5,0)
        self.position = Vec2(0.4,-0.5)

    def passive(self):
        self.position = Vec2(0.5,-0.6)

from CollidableObject import CollidableObject
from WolfAndEggConsts import WolfAndEggConsts as consts
import random

class Egg(CollidableObject):
    def __init__(self):
        super().__init__()
        self.width = 30
        self.height = 30
        self.egg_speed = 3

    def move(self):
        self.y += self.egg_speed

    def spawn(self):
        self.x = random.randint(0, consts.screen_width - self.width)
        self.y = 0
        self.egg_speed = 3  # Reset speed to initial value on spawn

    def border_touch(self):
        if self.collide_with_bottom_border():
            self.spawn()
            return True
        return False
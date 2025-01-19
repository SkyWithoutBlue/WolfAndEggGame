from CollidableObject import CollidableObject
from WolfAndEggConsts import WolfAndEggConsts as consts

class Player(CollidableObject):
    def __init__(self):
        super().__init__()
        self.width = 50
        self.height = 50
        self.x = consts.screen_width / 2 - self.width / 2
        self.y = consts.screen_height - self.height
        self.player_speed = 5

    def not_left_border(self):
        return self.x > 0

    def not_right_border(self):
        return self.x + self.width < consts.screen_width

    def move_left(self):
        if self.not_left_border():
            self.x -= self.player_speed

    def move_right(self):
        if self.not_right_border():
            self.x += self.player_speed
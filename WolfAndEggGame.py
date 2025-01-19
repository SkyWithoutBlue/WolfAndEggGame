import pygame
from WolfAndEggConsts import WolfAndEggConsts as consts
from Player import Player
from Egg import Egg
from Counters import Counters

class Game():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((consts.screen_width, consts.screen_height))
        pygame.display.set_caption("Волк и яица")
        self.font = pygame.font.SysFont(None, 30)
        self.counters = Counters()
        self.player = Player()
        self.eggs = [Egg()]
        self.is_running = True

    def update_scene(self):
        self.screen.fill(consts.white)
        pygame.draw.rect(self.screen, consts.black, self.player.get_parametres())
        for egg in self.eggs:
            pygame.draw.ellipse(self.screen, consts.red, egg.get_parametres())
        score_text = self.font.render("Score: " + str(self.counters.score), True, consts.black)
        self.screen.blit(score_text, (10, 10))
        pygame.display.update()
        self.clock.tick(consts.clock_ticks)

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.is_running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        for egg in self.eggs:
            egg.move()
            if self.player.collide(egg):
                egg.spawn()
                self.counters.score += 1
            if egg.border_touch():
                egg.spawn()
                self.counters.score -= 1

    def start_run(self):
        while self.is_running:
            self.update_scene()
            self.run()
        pygame.quit()


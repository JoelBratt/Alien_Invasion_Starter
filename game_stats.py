import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():

    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats() 

    def reset_stats(self):
        self.ships_left = self.settings.ships_left
        self.score = 0
        self.level = 1

    def update(self, collisions):
        #update self.score
        self._update_score(collisions)

        self._update_max_score()

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
            print(f'Max: {self.max_score}')

    def _update_score(self, collisions):
        for alien in collisions.values():
            self.score += math.ceil(self.settings.alien_points ** (1 + self.level/4))
            print(f'Basic: {self.score}')
        #update self.max_score


        #update hi_score
    def update_level(self):
        self.level += 1
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invatsion import AlienInvasion

class GameStats():

    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()
    
    def reset_stats(self):
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, points):
        #update score
        self._update_score(points)
        #update max score
        self._update_max_score()
        #update high score
    
    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f"Max score: {self.max_score}")
    
    def _update_score(self, collisions):
        for alien in collisions:
            self.score += self.settings.alien_points
        #print(f"Score: {self.score}")

    def update_level(self):
        self.level += 1
        #print(f"Level: {self.level}")
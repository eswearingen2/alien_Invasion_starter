from pathlib import Path
class Settings:
    def __init__(self):
        base_path = Path(__file__).parent
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 600
        self.FPS = 60
        self.bg_file = base_path / 'Assets'/ 'images' / 'Starbasesnow.png'

        self.ship_file = base_path / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_file = base_path / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = base_path / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = base_path / 'Assets' / 'sound' / 'impactSound.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        self.alien_file = base_path / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 30
        self.alien_h = 30
        self.fleet_speed = 1
        self.fleet_direction = 1
        self.fleet_drop_speed = 40

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)

        self.button_text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = base_path / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'
        
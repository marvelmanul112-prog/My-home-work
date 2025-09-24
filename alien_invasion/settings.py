class Settings:
    def __init__(self):
        self.screen_width = 800  # Ширина экрана
        self.screen_height = 1200   # Высота экрана
        self.bg_color = (28,28,28)  # Цвет фона
        self.ship_speed_factor = 1.5  # Скорость корабля

        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (150, 60, 60)
        self.bullets_allowed = 5
        self.alien_speed_factor = 0.4  #скорость пришельца
        self.fleet_drop_speed = 10  # скорость смещения вниз
        self.fleet_direction = 1  # 1 - движение вправо, -1 - влево


        self.ship_limit = 3  # количество жизней
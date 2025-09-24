import pygame
from pygame.sprite import Sprite
from random import randint, choice, uniform


class Star(Sprite):
    """Класс для звезд, создающих эффект движения корабля вверх"""

    def __init__(self, ai_settings, screen):
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Разные слои звезд для эффекта глубины
        layer = choice(['far', 'medium', 'near'])

        if layer == 'far':  # Далёкие звезды - медленные, маленькие
            self.size = 1
            self.speed = uniform(0.1, 0.1)  # случайная скорость в диапазоне
            self.brightness = 120
        elif layer == 'medium':  # Средние звезды
            self.size = 2
            self.speed = uniform(0.1, 0.1)
            self.brightness = 180
        else:  # Близкие звезды - быстрые, большие
            self.size = 3
            self.speed = uniform(0.1, 0.1)
            self.brightness = 255

        # Создаем поверхность для звезды
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill((self.brightness, self.brightness, self.brightness))
        self.rect = self.image.get_rect()

        # Начальная позиция - заполняем весь экран + немного выше
        self.rect.x = randint(0, ai_settings.screen_width)
        self.rect.y = randint(-50, ai_settings.screen_height)  # некоторые начинаются выше экрана

        # Точные координаты для плавного движения
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Двигает звезды вниз (создает эффект движения корабля вверх)"""
        self.y += self.speed
        self.rect.y = int(self.y)

        # Если звезда ушла за нижний край, перемещаем ее наверх
        if self.rect.top > self.ai_settings.screen_height:
            self.reset_position()

    def reset_position(self):
        """Перемещает звезду на верх экрана с новыми случайными параметрами"""
        self.y = -self.rect.height
        self.rect.y = int(self.y)
        self.rect.x = randint(0, self.ai_settings.screen_width)
        self.x = float(self.rect.x)

        # Можно добавить небольшое изменение скорости для разнообразия
        if randint(1, 10) == 1:  # 10% chance to change speed slightly
            self.speed = max(0.1, self.speed + uniform(-0.2, 0.2))
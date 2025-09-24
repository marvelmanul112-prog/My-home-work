import pygame.font


class Button:
    def __init__(self, ai_settings, screen, msg):
        """Инициализирует атрибуты кнопки."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Назначение размеров и свойств кнопок.
        self.width, self.height = 200, 50
        self.button_color = (250, 100, 90)  # Темно-зеленый
        self.hover_color = (50, 200, 200)  # Ярко-зеленый при наведении
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # Сообщение кнопки
        self.msg = msg
        self.prep_msg(msg)

        # Состояние наведения
        self.is_hovered = False

    def prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def check_hover(self, mouse_pos):
        """Проверяет, находится ли мышь над кнопкой."""
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def draw_button(self):
        """Отображение кнопки с эффектом наведения."""
        # Выбираем цвет в зависимости от состояния
        color = self.hover_color if self.is_hovered else self.button_color

        # Рисуем кнопку
        pygame.draw.rect(self.screen, color, self.rect, border_radius=10)
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect, 2, border_radius=10)  # Белая рамка

        # Центрируем текст
        self.msg_image_rect.center = self.rect.center
        self.screen.blit(self.msg_image, self.msg_image_rect)
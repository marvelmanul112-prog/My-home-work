import pygame
from pygame.sprite import Group
from ship import Ship
from settings import Settings
from game_stats import GameStats
from button import Button
import game_functions as gf  # Добавьте этот импорт


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Создаем экземпляр для хранения статистики
    stats = GameStats(ai_settings)

    # Создаем кнопки
    play_button = Button(ai_settings, screen, "Играть")
    exit_button = Button(ai_settings, screen, "Выйти")
    restart_button = Button(ai_settings, screen, "Заново")

    # Размещаем кнопки вертикально
    play_button.rect.center = (ai_settings.screen_width // 2, ai_settings.screen_height // 2 - 60)
    exit_button.rect.center = (ai_settings.screen_width // 2, ai_settings.screen_height // 2 + 60)
    restart_button.rect.center = (ai_settings.screen_width // 2, ai_settings.screen_height // 2)

    # Обновляем текст на кнопках
    play_button.prep_msg("Играть")
    exit_button.prep_msg("Выйти")
    restart_button.prep_msg("Заново")

    # Создаем игровые объекты
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stars = Group()

    # Создаем пришельцев и звезды
    gf.create_fleet(ai_settings, screen, ship, aliens)
    gf.create_stars(ai_settings, screen, stars)

    while True:
        # Получаем позицию мыши для эффекта наведения
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Проверяем наведение на кнопки
        if not stats.game_active:
            play_button.check_hover((mouse_x, mouse_y))
            exit_button.check_hover((mouse_x, mouse_y))
            restart_button.check_hover((mouse_x, mouse_y))

        gf.check_events(ai_settings, screen, stats, play_button, exit_button, restart_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, ship, aliens, bullets)
            gf.update_stars(stars)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, stars,
                         play_button, exit_button, restart_button)

if __name__ == "__main__":
    run_game()
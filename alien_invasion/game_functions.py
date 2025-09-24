import sys
import pygame
from bullet import Bullet
from alien import Alien
from random import randint, choice
from stars import Star

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, play_button, exit_button, restart_button, ship, aliens, bullets):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверяем все кнопки
            check_play_button(ai_settings, screen, stats, play_button, mouse_x, mouse_y, ship, aliens, bullets)
            check_exit_button(exit_button, mouse_x, mouse_y)
            check_restart_button(ai_settings, screen, stats, restart_button, mouse_x, mouse_y, ship, aliens, bullets)


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, stars,
                  play_button, exit_button, restart_button):
    """Обновляет изображения на экране и отображает новый экран."""
    screen.fill(ai_settings.bg_color)

    if not stats.game_active:
        # Показываем меню
        screen.fill((0, 0, 0))  # Черный фон для меню

        # Заголовок игры
        font = pygame.font.SysFont(None, 72)
        title = font.render("ALIEN INVASION", True, (255, 255, 255))
        title_rect = title.get_rect()
        title_rect.centerx = screen.get_rect().centerx
        title_rect.top = 100
        screen.blit(title, title_rect)

        # Рисуем кнопки
        play_button.draw_button()
        exit_button.draw_button()
        restart_button.draw_button()
    else:
        # Показываем игровой процесс
        stars.draw(screen)

        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)

    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Обновляет позиции пуль и уничтожает старые пули."""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Проверка попаданий в пришельцев
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # Уничтожение существующих пуль и создание нового флота
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)



def get_number_aliens_x(ai_settings, alien_width):
    """Вычисляет количество пришельцев в ряду."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x  # ← ПРАВИЛЬНЫЙ ОТСТУП!


def get_number_rows(ai_settings, ship_height, alien_height):
    """Определяет количество рядов, помещающихся на экране."""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Создает пришельца и размещает его в ряду."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Создает флот пришельцев."""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    # Создание флота пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                         row_number)





def create_stars(ai_settings, screen, stars):
    """Создает звездное поле для эффекта движения вверх"""
    # Создаем больше звезд для плотного звездного поля
    number_stars = 200

    for _ in range(number_stars):
        star = Star(ai_settings, screen)
        stars.add(star)


def update_stars(stars):
    """Обновляет позиции всех звезд"""
    stars.update()

def check_aliens_bottom(ai_settings, screen, ship, aliens, bullets):
    """Проверяет, добрались ли пришельцы до нижней границы экрана"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, screen, ship, aliens, bullets):
    """Обновляет позиции всех пришельцев"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Проверяем столкновения "пришелец-корабль"
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, ship, aliens, bullets)

    # Проверяем, достигли ли пришельцы нижнего края
    check_aliens_bottom(ai_settings, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    """Реагирует на достижение края"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

        # Проверка коллизий "пришелец-корабль".


def change_fleet_direction(ai_settings, aliens):
    """Опускает флот и меняет направление"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, ship, aliens, bullets):
    """Обрабатывает столкновение корабля с пришельцем"""
    print("Корабль уничтожен! Создаем новый флот...")

    # Удаляем всех пришельцев и пули
    aliens.empty()
    bullets.empty()

    # Создаем новый флот и центрируем корабль
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # Пауза для визуального эффекта
    pygame.time.delay(1000)

def check_play_button(ai_settings, screen, stats, play_button, mouse_x, mouse_y, ship, aliens, bullets):
    """Запускает новую игру при нажатии кнопки Play."""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        stats.game_active = True
        reset_game(ai_settings, screen, ship, aliens, bullets)

def check_exit_button(exit_button, mouse_x, mouse_y):
    """Выходит из игры при нажатии кнопки Exit."""
    if exit_button.rect.collidepoint(mouse_x, mouse_y):
        pygame.quit()
        sys.exit()



def draw_menu(screen, play_button, exit_button, restart_button):
    """Отрисовывает меню с кнопками."""
    screen.fill((0, 0, 0))  # Черный фон

    # Заголовок игры
    font = pygame.font.SysFont(None, 72)
    title = font.render("ALIEN INVASION", True, (255, 255, 255))
    title_rect = title.get_rect()
    title_rect.centerx = screen.get_rect().centerx
    title_rect.top = 100
    screen.blit(title, title_rect)

    # Рисуем кнопки
    play_button.draw_button()
    exit_button.draw_button()
    restart_button.draw_button()

    pygame.display.flip()




def check_restart_button(ai_settings, screen, stats, restart_button, mouse_x, mouse_y, ship, aliens, bullets):
    """Перезапускает игру при нажатии кнопки Restart."""
    if restart_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
        reset_game(ai_settings, screen, ship, aliens, bullets)




def reset_game(ai_settings, screen, ship, aliens, bullets):
    """Сбрасывает игру в начальное состояние."""
    # Очищаем пришельцев и пули
    aliens.empty()
    bullets.empty()

    # Создаем новый флот и центрируем корабль
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
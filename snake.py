import pygame
import random
import time

pygame.init()

# размер окна
width = 600
height = 400
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

clock = pygame.time.Clock()

block_size = 20
snake_speed = 15


def message(msg, color):
    font_style = pygame.font.SysFont(None, 35)
    render_message = font_style.render(msg, True, color)
    game_display.blit(render_message, [width / 6, height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    apple_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    apple_y = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not game_over:
        # Обработка событий (нажатия клавиш)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                if event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                if event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # ДВИЖЕНИЕ ЗМЕЙКИ
        x1 += x1_change
        y1 += y1_change

        # ПРОВЕРКА СТОЛКНОВЕНИЯ СО СТЕНАМИ
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # ПРОВЕРКА СЪЕДАНИЯ ЯБЛОКА
        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, width - block_size) / block_size) * block_size
            apple_y = round(random.randrange(0, height - block_size) / block_size) * block_size
            print("Яблоко съедено!")

        # ОТРИСОВКА
        game_display.fill(black)

        # Рисуем яблоко
        pygame.draw.rect(game_display, red, [apple_x, apple_y, block_size, block_size])

        # Рисуем змейку
        pygame.draw.rect(game_display, green, [x1, y1, block_size, block_size])

        # Обновляем экран
        pygame.display.update()

        # Устанавливаем скорость игры
        clock.tick(snake_speed)

        # ЭКРАН ПРОИГРЫША
        while game_close == True:
            game_display.fill(black)
            message("GG! Нажми q -выйти r - играть снова", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()


# ЗАПУСК ИГРЫ
def gameLoop():
    game_over = False
    game_close = False

    # Начальная позиция головы змейки
    x1 = width / 2
    y1 = height / 2

    # Начальное движение
    x1_change = 0
    y1_change = 0


    # Пока в хвосте только голова
    snake_List = []
    Length_of_snake = 1  # Начальная длина змейки

    # Позиция яблока
    apple_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    apple_y = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not game_over:

        # ЭКРАН ПРОИГРЫША
        while game_close:
            game_display.fill(black)
            message("GG! Нажми Q-выход или R-играть снова", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()

        # цикл игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if game_over:
            break

        # ДВИЖЕНИЕ ЗМЕЙКИ
        x1 += x1_change
        y1 += y1_change

        # ПРОВЕРКА СТОЛКНОВЕНИЯ СО СТЕНАМИ
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # ПРОВЕРКА СЪЕДАНИЯ ЯБЛОКА
        if x1 == apple_x and y1 == apple_y:
            # Генерируем новое яблоко
            apple_x = round(random.randrange(0, width - block_size) / block_size) * block_size
            apple_y = round(random.randrange(0, height - block_size) / block_size) * block_size
            # УВЕЛИЧИВАЕМ ДЛИНУ ЗМЕЙКИ
            Length_of_snake += 1
            print("Яблоко съедено! Длина змейки:", Length_of_snake)

        # ОТРИСОВКА
        game_display.fill(black)
        pygame.draw.rect(game_display, red, [apple_x, apple_y, block_size, block_size])

        #  ПОЗИЦИИ ХВОСТА ЗМЕЙКИ
        # позицию головы в начало списка
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Если хвост стал длиннее чем нужно - удаляем лишние сегменты
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Змейка (голову + хвост)
        for segment in snake_List:
            pygame.draw.rect(game_display, green, [segment[0], segment[1], block_size, block_size])

        pygame.display.update()
        clock.tick(snake_speed)


# ЗАПУСК ИГРЫ
gameLoop()
pygame.quit()
quit()





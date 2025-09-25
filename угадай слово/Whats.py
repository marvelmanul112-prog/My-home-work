import random

def w_words():
    stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        ---|-------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        ---|-------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        ---|-------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        ---|-------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        ---|-------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        ---|-------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ---|-------
        """
    ]

    words = 'Сюда введи список слов которые будут учавствовать в игре'
    funny_texts = [
        "Ты не угадал!",
        "Опять мимо!",
        "Не повезло!",
        "Эх, почти...",
        "Промах!",
        "Фейл!",
        "GG"]
    error_count = 0
    random_word = random.choice(words)
    error_max = 6
    kpr = ''
    while error_count <= error_max:
        slovo = input('Я загадал слово, попробуй его отгадать, введи букву): ')

        if slovo in random_word:
            print('Да эта буква имеется')

            kpr += slovo
        else:
            print(funny_texts[error_count])
            print(stages[error_count])
            error_count += 1


            # Новая проверка: все ли буквы слова есть в угаданных
        if all(letter in kpr for letter in random_word):
            print('Поздравляю вы угадали слово:', random_word)
            break
    else:
         print('Игра окончена. Загаданное слово было:', random_word)

    return
w_words()
import tkinter as tk
from tkinter import mainloop
from tkinter import messagebox
from click import command


#основное окно
root = tk.Tk()
# root.geometry("300x300")
root.title('Крестики(x0)нолики')

buttons =[]
current_player = "X"

def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтальные линии
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикальные линии
        [0, 4, 8], [2, 4, 6]              # Диагональные линии
    ]

    for combo in winning_combinations:
        a, b, c = combo
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            buttons[a].config(bg='light green')
            buttons[b].config(bg='light green')
            buttons[c].config(bg='light green')
            return True
    return False





def on_click(index):
    global current_player
    if buttons[index]['text'] == "":
        buttons[index]['text'] = current_player

        if check_winner():  # Проверяем победу
            messagebox.showinfo("Победа!", f"Победил {current_player}!")  # Всплывающее окно с победителем
        elif all(button["text"] != "" for button in buttons):  # Проверяем ничью
            messagebox.showinfo("Ничья!", "Игра окончена. Ничья!")  # Всплывающее окно с ничьей
        else:
            # Меняем игрока
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"


def reset_game():
    global current_player
    current_player = "X"  # Первый ход всегда за "X"

    # Очищаем все кнопки, возвращая им стандартный цвет и убирая текст
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")








for i in range(9):  # Создаём 9 кнопок (от 0 до 8)
    button = tk.Button(
        root,
        text="",  # Пока без текста
        font=("Arial", 30),  # Крупный шрифт
        width=5,  # Ширина кнопки
        height=2,  # Высота кнопки
        command = lambda index=i: on_click(index),
    )
    button.grid(row=i//3, column=i%3)  # Размещаем кнопку в сетке
    buttons.append(button)  # Добавляем кнопку в список

reset_button = tk.Button(root, text="Новая игра", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="we")






root.mainloop()
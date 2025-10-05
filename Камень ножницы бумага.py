import random
import tkinter as tk
from tkinter import messagebox




class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Камень-Ножницы-Бумага")
        self.window.geometry("750x480")
        self.window.resizable(False, False)
        self.rock_img = tk.PhotoImage(file=r)

        self.spells = ['камень', 'ножницы', 'бумага']
        self.create_widgets()

    def play_game(self, user_choice):
        """Основная логика игры"""
        computer_choice = random.choice(self.spells)

        # Определяем победителя
        if user_choice == computer_choice:
            result = "Ничья!"
        elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
                (user_choice == 'ножницы' and computer_choice == 'бумага') or \
                (user_choice == 'бумага' and computer_choice == 'камень'):
            result = "Вы выиграли!"
        else:
            result = "Вы проиграли!"

        # Обновляем текст в окне приложения
        self.result_label.config(
            text=f"Вы: {user_choice}\nКомпьютер: {computer_choice}\n\n{result}"
        )














    def create_widgets(self):
        # Заголовок
        title_label = tk.Label(
            self.window,
            text="Давай сыграем в игру!",
            font=("Arial", 16, "bold"),  
            pady=20
        )
        title_label.pack()

        """кнопки выбора"""
        buttons_frame = tk.Frame(self.window)
        buttons_frame.pack(pady=20)

        # Поле для результата (добавьте после buttons_frame)
        self.result_label = tk.Label(
            self.window,
            text="Сделайте ваш выбор!",
            font=("Arial", 14),
            pady=20
        )
        self.result_label.pack()


        self.rock_btn = tk.Button(
            buttons_frame,
            text='Камень',
            font=('Arial', 12),
            width=10,
            height=2,
            command=lambda: self.play_game('камень')
        )
        self.rock_btn.pack(side=tk.LEFT, padx=5)

        self.scissors_btn = tk.Button(
            buttons_frame,
            text='ножницы',
            font=('Arial', 12),
            width=10,
            height=2,
            command=lambda: self.play_game('ножницы')
        )
        self.scissors_btn.pack(side=tk.LEFT, padx=5)

        self.papper_btn = tk.Button(
            buttons_frame,
            text = 'бумага',
            font=('Arial', 12),
            width=10,
            height=2,
            command=lambda: self.play_game('бумага')

        )
        self.papper_btn.pack(side=tk.LEFT, padx=5)




    def run(self):
        self.window.mainloop()


# Запуск приложения
if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()
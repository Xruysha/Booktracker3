import tkinter as tk
from tkinter import ttk
import random
import string
import json


# Функция генерации пароля
def generate_password():
    length = length_slider.get()
    chars = ""

    if use_digits.get():
        chars += string.digits
    if use_letters.get():
        chars += string.ascii_letters
    if use_special.get():
        chars += string.punctuation

    if not chars:
        return "Выберите хотя бы один тип символов"

    password = ''.join(random.choice(chars) for _ in range(length))
    history_listbox.insert(tk.END, password)
    save_history()


# Функция сохранения истории паролей
def save_history():
    history = history_listbox.get(0, tk.END)
    with open('history.json', 'w') as f:
        json.dump(list(history), f)


# Функция загрузки истории паролей
def load_history():
    try:
        with open('history.json', 'r') as f:
            history = json.load(f)
            for password in history:
                history_listbox.insert(tk.END, password)
    except FileNotFoundError:
        pass


# Создаем главное окно
root = tk.Tk()
root.title("Random Password Generator")

# Ползунок длины пароля
length_label = tk.Label(root, text="Длина пароля:")
length_label.pack()
length_slider = tk.Scale(root, from_=8, to=32, orient=tk.HORIZONTAL)
length_slider.pack()

# Чекбоксы
checkbox_frame = ttk.LabelFrame(root, text="Выберите символы")
checkbox_frame.pack(padx=10, pady=10)

use_digits = tk.BooleanVar()
use_letters = tk.BooleanVar()
use_special = tk.BooleanVar()

tk.Checkbutton(checkbox_frame, text="Цифры", variable=use_digits).pack(anchor=tk.W)
tk.Checkbutton(checkbox_frame, text="Буквы", variable=use_letters).pack(anchor=tk.W)
tk.Checkbutton(checkbox_frame, text="Спецсимволы", variable=use_special).pack(anchor=tk.W)

# Кнопка генерации
generate_button = tk.Button(root, text="Генерировать пароль", command=generate_password)
generate_button.pack(pady=10)

# Таблица истории
history_label = tk.Label(root, text="История паролей:")
history_label.pack()
history_listbox = tk.Listbox(root, width=50)
history_listbox.pack(pady=10)

# Загружаем историю при запуске
load_history()

# Запускаем главный цикл приложения
root.mainloop()
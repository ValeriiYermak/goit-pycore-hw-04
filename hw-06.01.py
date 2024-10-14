"""У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.
"""

import tkinter as tk
from tkinter import filedialog


def total_salary(path):
    total = 0
    count = 0

    with open(path, "r") as file:
        for line in file:
            name, salary = line.strip().split(",")
            total += int(salary)
            count += 1
    average_salary = total / count if count > 0 else 0
    return total, average_salary


try:
    root = tk.Tk()
    root.withdraw()
    data_source = filedialog.askopenfilename(
        title="Виберіть файл", filetypes=[("Файл з даними", "*.txt")]
    )

    if data_source:
        total, average = total_salary(data_source)
        print(f"Загальна сума зарплат: {total}")
        print(f"Середня зарплата: {average:.2f}")
    else:
        print("Файл не був обраний.")
except Exception as e:
    print("An error occurred:", e)

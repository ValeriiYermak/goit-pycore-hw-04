"""
Розробіть скрипт, який приймає шлях до директорії в якості аргументу 
командного рядка і візуалізує структуру цієї директорії, виводячи імена 
всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена 
директорій та файлів мають відрізнятися за кольором.
"""

import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def visualize_directory(path, indent=0):
    if not path.exists() or not path.is_dir():
        print(f"{Fore.RED}Вказаний шлях не існує або не є директорією: {path}")
        return

    for item in path.iterdir():
        if item.is_dir():
            print(f"{' ' * indent}{Fore.BLUE}{item.name}/")
            visualize_directory(item, indent + 4)
        else:
            print(f"{' ' * indent}{Fore.GREEN}{item.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.YELLOW}Використання: python hw-06.03.py <шлях_до_директорії>")
        sys.exit(1)

    directory_path = Path(sys.argv[1])
    visualize_directory(directory_path)

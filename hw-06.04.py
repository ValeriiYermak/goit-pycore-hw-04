"""
Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.
У цій домашній роботі зосередимося на інтерфейсі самого бота. Найпростіший і найзручніший на початковому етапі розробки інтерфейс - це консольний застосунок CLI (Command Line Interface). CLI достатньо просто реалізувати.

Будь-який CLI складається з трьох основних елементів:

Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, виділення з рядка ключових слів та модифікаторів команд.
Функції обробники команд - набір функцій, які ще називають handler, вони відповідають за безпосереднє виконання команд.
Цикл запит-відповідь. Ця частина застосунку відповідає за отримання від користувача даних та повернення користувачеві відповіді від функції - handler-а.


На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону, знаходити номер телефону за ім'ям, змінювати записаний номер телефону, виводити в консоль всі записи, які зберіг. Щоб реалізувати таку нескладну логіку, скористаємося словником. У словнику будемо зберігати ім'я користувача, як ключ, і номер телефону як значення.
"""
import re

def parse_input(user_input):
    parts = user_input.split()
    cmd = parts[0].strip().lower()
    args = parts[1:]  # Отримати всі аргументи як плоский список
    return cmd, args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Error: Provide both name and phone number."
    name, phone = args
    if name in contacts:
        return "Error: Contact already exists."
    normalized_phone = normalize_phone(phone)  # Нормалізація номера
    contacts[name] = normalized_phone
    save_contacts(contacts)  # Зберігаємо контакти у файл
    return "Contact added."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Error: Provide both name and new phone number."
    name, new_phone = args
    if name not in contacts:
        return "Error: Contact not found."
    normalized_phone = normalize_phone(new_phone)  # Нормалізація нового номера
    contacts[name] = normalized_phone
    save_contacts(contacts)  # Зберігаємо контакти у файл
    return "Contact updated."


def normalize_phone(phone_number):
    normalized_number = re.sub(r'[^\d+]', '', phone_number)

    if normalized_number.startswith('+'):
        if normalized_number.startswith('+380'):
            return normalized_number
        elif normalized_number.startswith('+38'):
            return normalized_number
        elif normalized_number.startswith('+0'):
            return '+38' + normalized_number[2:]
        else:
            return normalized_number
    elif normalized_number.startswith('0'):
        normalized_number = '+38' + normalized_number[1:]
    elif normalized_number.startswith('380'):
        normalized_number = '+' + normalized_number[2:]
    else:
        normalized_number = '+38' + normalized_number
    return normalized_number

def show_phone(args, contacts):
    if len(args) == 0:
        return "Error: Provide a name."
    
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."

def get_contact_info(path):
    contacts = {}
    try:
        with open(path, "r") as file:
            for line in file:
                contact_name, contact_phone = line.strip().split(",")
                contacts[contact_name.strip()] = contact_phone.strip()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return contacts

def save_contacts(contacts, path="contacts_info.txt"):
    # Зберігаємо контакти у файл
    try:
        with open(path, "w") as file:
            for name, phone in contacts.items():
                file.write(f"{name.strip()}, {phone.strip()}\n")  # Записуємо контакти у файл
    except Exception as e:
        print(f"Error saving contacts: {e}")

def main():
    contacts = {}
    path_to_file = "contacts_info.txt"
        
    try:
        contacts_info = get_contact_info(path_to_file)
        for contact_name, contact_phone in contacts_info.items():
            contacts[contact_name] = contact_phone
    except FileNotFoundError:
        print(f"File '{path_to_file}' not found. Starting with empty contacts.")

    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)  # Змінено на плоский список аргументів

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            if len(args) < 2:
                print("Error: Provide both name and new phone number.")
            else:
                print(change_contact(args, contacts))
        elif command == "phone":
            if not args:
                print("Error: Provide a name.")
            else:
                print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))  # Виводимо всі контакти
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

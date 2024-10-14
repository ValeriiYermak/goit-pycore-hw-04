"""
У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.
Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.
"""



def get_cats_info(path):
    cats = []
    with open(path, "r") as file:
        for line in file:
            cat_id, name, age = line.strip().split(",")
            cats.append({'id': cat_id, 'name': name, 'age': int(age)})
    return cats

path_to_file = "cats_file.txt"

cats_info = get_cats_info(path_to_file)

for cat in cats_info:
    print(f"Ідентифікатор: {cat['id']}, Ім'я: {cat['name']}, Вік: {cat['age']}")

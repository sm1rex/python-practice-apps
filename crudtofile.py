import os

file_name = "data.txt"

# Функция для создания нового элемента в файле
def create():
    item = input("Введите значение для добавления: ")
    with open(file_name, "a") as f:
        f.write(item + "\n")
    print("Элемент успешно добавлен")

# Функция для чтения всех элементов из файла
def read():
    with open(file_name, "r") as f:
        items = f.readlines()
    if not items:
        print("Файл пуст")
    else:
        print("Элементы:")
        for item in items:
            print(item.strip())

# Функция для обновления элемента в файле
def update():
    items = read_file()
    if not items:
        return
    index = int(input("Введите номер элемента для обновления: "))
    if index < 1 or index > len(items):
        print("Неверный номер элемента")
        return
    new_item = input("Введите новое значение: ")
    items[index-1] = new_item + "\n"
    with open(file_name, "w") as f:
        f.writelines(items)
    print("Элемент успешно обновлен")

# Функция для удаления элемента из файла
def delete():
    items = read_file()
    if not items:
        return
    index = int(input("Введите номер элемента для удаления: "))
    if index < 1 or index > len(items):
        print("Неверный номер элемента")
        return
    del items[index-1]
    with open(file_name, "w") as f:
        f.writelines(items)
    print("Элемент успешно удален")

# Функция для чтения всех элементов из файла
def read_file():
    with open(file_name, "r") as f:
        items = f.readlines()
    if not items:
        print("Файл пуст")
    return items

# Главная функция для управления приложением
def main():
    # Создание файла, если он не существует
    if not os.path.exists(file_name):
        open(file_name, "w").close()
    while True:
        print("Выберите действие:")
        print("1. Добавить элемент")
        print("2. Просмотреть все элементы")
        print("3. Обновить элемент")
        print("4. Удалить элемент")
        print("5. Выйти из приложения")
        choice = input()
        if choice == "1":
            create()
        elif choice == "2":
            read()
        elif choice == "3":
            update()
        elif choice == "4":
            delete()
        elif choice == "5":
            break
        else:
            print("Неверный выбор")
    print("Работа приложения завершена")

if __name__ == "__main__":
    main()

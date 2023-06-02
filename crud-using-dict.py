import json

# Функция для создания нового товара


def create_product():
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))

    # Создаем словарь с информацией о товаре
    product = {
        'name': name,
        'price': price
    }

    # Открываем файл для записи
    with open('products.txt', 'a') as file:
        # Записываем информацию о товаре в формате JSON
        file.write(json.dumps(product) + '\n')

    print("Товар успешно создан!")

# Функция для чтения всех товаров


def read_products():
    with open('products.txt', 'r') as file:
        for line in file:
            # Читаем каждую строку и преобразуем ее из JSON в словарь
            product = json.loads(line)
            print("Название: " + product['name'])
            print("Цена: " + str(product['price']))
            print("")

# Функция для обновления информации о товаре


def update_product():
    name = input("Введите название товара для обновления: ")

    # Открываем файл для чтения и записи
    with open('products.txt', 'r+') as file:
        lines = file.readlines()
        file.seek(0)  # Перемещаем указатель в начало файла

        for line in lines:
            product = json.loads(line)

            if product['name'] == name:
                # Запрашиваем новые данные для обновления товара
                new_name = input("Введите новое название товара: ")
                new_price = float(input("Введите новую цену товара: "))

                # Обновляем информацию о товаре
                product['name'] = new_name
                product['price'] = new_price

            # Записываем обновленную информацию о товаре
            file.write(json.dumps(product) + '\n')

    print("Информация о товаре успешно обновлена!")

# Функция для удаления товара


def delete_product():
    name = input("Введите название товара для удаления: ")

    # Открываем файл для чтения и записи
    with open('products.txt', 'r+') as file:
        lines = file.readlines()
        file.seek(0)  # Перемещаем указатель в начало файла

        for line in lines:
            product = json.loads(line)

            if product['name'] != name:
                # Записываем информацию о товаре обратно в файл, исключая товар для удаления
                file.write(json.dumps(product) + '\n')

        file.truncate()  # Обрезаем файл до текущей позиции

    print("Товар успешно удален!")

# Главная функция для работы с системой учета товаров


def main():
    while True:
        print("1. Создать товар")
        print("2. Просмотреть все товары")
        print("3. Обновить информацию о товаре")
        print("4. Удалить товар")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            create_product()
        elif choice == '2':
            read_products()
        elif choice == '3':
            update_product()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")


if __name__ == '__main__':
    main()

def show_menu():
    print("1. Додати запис")
    print("2. Показати всі записи")
    print("3. Видалити запис")
    print("4. Вийти")


def add_record():
    record = input("Введіть запис: ")
    with open("data.txt", "a") as file:
        file.write(record + "\n")
    print("Запис успішно додано!")


def show_records():
    with open("data.txt", "r") as file:
        records = file.readlines()
    if len(records) > 0:
        print("Записи:")
        for index, record in enumerate(records, start=1):
            print(f"{index}. {record.strip()}")
    else:
        print("Немає записів.")


def delete_record():
    show_records()
    record_index = int(
        input("Введіть номер запису, який хочете видалити: ")) - 1
    with open("data.txt", "r") as file:
        records = file.readlines()
    if record_index >= 0 and record_index < len(records):
        deleted_record = records.pop(record_index)
        with open("data.txt", "w") as file:
            file.writelines(records)
        print(f"Запис '{deleted_record.strip()}' успішно видалено!")
    else:
        print("Невірний номер запису.")


def main():
    while True:
        show_menu()
        choice = input("Виберіть опцію (1-4): ")
        if choice == "1":
            add_record()
        elif choice == "2":
            show_records()
        elif choice == "3":
            delete_record()
        elif choice == "4":
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()

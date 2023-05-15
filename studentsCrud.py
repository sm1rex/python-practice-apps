import os


class Student:
    def __init__(self, name, surname, grades=[]):
        self.name = name
        self.surname = surname
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)


def read_students_from_file(file_path):
    students = []
    if not os.path.isfile(file_path):
        return students
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            values = line.strip().split(',')
            name, surname = values[0], values[1]
            grades = list(map(float, values[2:]))
            students.append(Student(name, surname, grades))
    return students


def write_students_to_file(file_path, students):
    with open(file_path, 'w') as file:
        for student in students:
            grades_str = ','.join(str(g) for g in student.grades)
            file.write(f"{student.name},{student.surname},{grades_str}\n")


def display_students(students):
    for i, student in enumerate(students):
        print(
            f"{i+1}. {student.name} {student.surname} (Средний балл: {student.get_average_grade():.2f})")


def add_student(students):
    name = input("Введите имя ученика: ")
    surname = input("Введите фамилию ученика: ")
    grades = input("Введите оценки ученика (через запятую): ")
    grades = list(map(float, grades.split(',')))
    student = Student(name, surname, grades)
    students.append(student)
    print("Ученик успешно добавлен в систему.")


def delete_student(students):
    index = int(input("Введите номер удаляемого ученика: ")) - 1
    if 0 <= index < len(students):
        students.pop(index)
        print("Ученик успешно удален из системы.")
    else:
        print("Ученика с таким номером не существует.")


def calculate_average_grade(students):
    index = int(input("Введите номер ученика: ")) - 1
    if 0 <= index < len(students):
        student = students[index]
        print(
            f"Средний балл ученика {student.name} {student.surname}: {student.get_average_grade():.2f}")
    else:
        print("Ученика с таким номером не существует.")


def display_all_students(file_path):
    students = read_students_from_file(file_path)
    if len(students) == 0:
        print("Нет данных об учениках.")
        return
    for i, student in enumerate(students):
        print(
            f"{i+1}. {student.name} {student.surname} (Средний балл: {student.get_average_grade():.2f})")


def main():
    file_path = "students.txt"
    students = read_students_from_file(file_path)
    display_students(students)

    while True:
        print()
        print("1 - Добавить ученика")
        print("2 - Удалить ученика")
        print("3 - Посчитать средний балл ученика")
        print("4 - Отобразить всех учеников")
        print("5 - Выйти из программы")
        choice = input("Выберите действие (1-4): ")

        if choice == "1":
            add_student(students)
            write_students_to_file(file_path, students)
        elif choice == "2":
            delete_student(students)
        elif choice == "3":
            calculate_average_grade(students)
        elif choice == "4":
            display_all_students(file_path)
        elif choice == "5":
            write_students_to_file(file_path, students)
            print("Данные сохранены в файл.")
            break
        else:
            print("Неверный выбор. Пожалуйста, повторите попытку.")


if __name__ == '__main__':
    main()

import random
import string

alphabets = list(string.ascii_letters)
numbers = list(string.digits)
specchar = list("!@#$%^&*()_+")

characters = list(alphabets + numbers + specchar)


def generate_password():
    length = int(input("Яка довжина паролю? - "))

    alphabet_length = int(input("Яка кількість літер? - "))
    numbers_length = int(input("Яка кількість чисел? - "))
    specchar_length = int(input("Яка кількість спец. символів? - "))

    alllength = alphabet_length + numbers_length + specchar_length

    if alllength > length:
        print("Не може так бути!")
        return

    password = []

    for i in range(alphabet_length):
        password.append(random.choice(alphabets))

    for i in range(numbers_length):
        password.append(random.choice(numbers))

    for i in range(specchar_length):
        password.append(random.choice(specchar))

    if alllength < length:
        random.shuffle(characters)
        for i in range(length - alllength):
            password.append(random.choice(characters))

    for i in range(5):
        random.shuffle(password)

    print("".join(password))

generate_password()
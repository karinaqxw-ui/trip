users = {
    "Анна": "дитина",
    "Іван": "підліток",
    "Олег": "дорослий"
}

name = input("Введи ім'я: ")

if name in users:
    print(users[name])
else:
    print("Нема такого імені")

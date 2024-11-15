import random

students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}

def add_student(students, name, age, email, phone=None, average_score=0.0):
    if phone is None:
        phone = '+380999999999'  # если телефона нет, используем номер родителей
    students[name] = {
        'Email': email,
        'Age': age,
        'Number': phone,
        'Total': average_score
    }

add_student(students,
            'Дмитро Іванов',
            random.randint(18, 40),
            'dmitro.ivanov@gmail.com',
            None,  # телефон оставляем None
            random.uniform(60, 100))

print("Students:")
for name, info in students.items():
    print(f"{name}: {info}")

high_achievers = [
    name for name, info in students.items() if info['Total Graduate'] > 90
]

print("\n More 90:")
for student in high_achievers:
    print(student)

total_score = 0
student_count = len(students)
for info in students.values():
    total_score += info['Total Graduate']\

average_group_score = total_score / student_count if student_count > 0 else 0
print(f"\n  Group: {average_group_score:.2f}")

print("\n Stats (Parents):")
for name, info in students.items():
    if info['Number'] is None:
        info['Number'] = '+380999999999'
    print(f"{name}: {info}")



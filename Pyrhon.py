імя = input("Введіть своє ім'я: ")

while True:
    вік = input("Введіть свій вік: ")
    if вік.isdigit() and int(вік) >= 12:
        break
    else:
        print("Будь ласка, введіть вік у вигляді числа, яке є не меншим за 12 років.")

while True:
    номер_телефону = input("Введіть свій номер телефону: ")
    if номер_телефону.isdigit() and len(номер_телефону) >= 10:
        break
    else:
        print("Будь ласка, введіть номер телефону у вигляді числа без пробілів та інших символів, що містить не менше 10 цифр.")

print("Ваше ім'я:", імя)
print("Ваш вік:", вік)
print("Ваш номер телефону:", номер_телефону)

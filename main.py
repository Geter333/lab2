import math
from series import calculate_series_sum  # Імпорт функції з модуля series


# Функція для першого завдання
def calculate_z(a, b):
    alpha = float(input("Введіть значення α: "))
    if alpha >= 15:
        z = math.sin(2 * a) + math.cos(2 * b)
    else:
        z = math.sqrt(a + b ** 2)
    return z


# Основна частина програми
def main():
    try:
        # Введення значень a та b для першого завдання
        a = float(input("Введіть значення a: "))
        b = float(input("Введіть значення b: "))

        # Обчислення z
        z = calculate_z(a, b)
        print(f"Значення z: {z}")

        # Введення n для другого завдання
        n = int(input("Введіть натуральне число n: "))
        if n <= 0:
            print("n повинно бути натуральним числом!")
            return

        # Обчислення суми ряду за допомогою імпортованої функції
        series_sum = calculate_series_sum(n)
        print(f"Сума ряду: {series_sum}")

    except ValueError:
        print("Помилка: введені значення повинні бути числами.")


# Виклик основної функції
if __name__ == "__main__":
    main()

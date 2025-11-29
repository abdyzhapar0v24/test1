import time
def main():
    print("Калькулятор")
    time.sleep(1)
    print("Доступные операторы")
    time.sleep(1)
    print("1 - Сложение")
    time.sleep(0.2)
    print("2 - Вычитание")
    time.sleep(0.2)
    print("3 - Умножение")
    time.sleep(0.2)
    print("4 - Деление")
    time.sleep(0.2)
    print("5 - Выход с калькулятора")
    time.sleep(0.2)

while True:
    main()
    time.sleep(0.5)
    choice = input("Выберите операцию:")

    if choice == "5":
        time.sleep(0.5)
        print("Вы вышли из калькулятора")
        break

    elif choice not in ["1", "2", "3", "4", "5"]:
        print("Ошибка")
        break


    num1 = float(input("Введите первое число"))
    time.sleep(0.5)
    num2 = float(input("Введите второе число"))
    time.sleep(0.5)

    if choice == "1":
        summa = num1 + num2
        print("Сумма ", summa)
        time.sleep(0.5)
    elif choice == "2":
        defference = num1 - num2
        print("Разность ", defference)
        time.sleep(0.5)
    elif choice == "3":
        product = num1 * num2
        print("Произведение ", product)
        time.sleep(0.5)
    elif choice == "4":
        quetient = num1 / num2
        print("Частное ", quetient)
        time.sleep(0.5) 
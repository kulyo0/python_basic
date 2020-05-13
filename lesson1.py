#Задание 1
a = input("ваше имя:\n")
print("Привет, " + a)
b = int(input("ваш год рождения:\n"))
c = 2020 - b
print("ваш возраст - " + str(c))

#Задание 2
timeseconds = input("Введите время в секундах:\n")
if timeseconds.isdigit():
    timeseconds = int(timeseconds)
    hours = timeseconds // 3600
    minutes = (timeseconds - hours * 3600) // 60
    seconds = timeseconds - hours * 3600 - minutes * 60
    timeformat = "{0}:{1}:{2}".format(hours, minutes, seconds)
    print("Вот так в формате ч - м - с: ", timeformat)
else:
   print("Неверный формат ввода")

#Задание 3
number1 = input("Введи число\n")
number1 = int(number1)
number2 = number1 * 11
number3 = number1 * 111
print("сложение вида:", number1, "+", number2, "+", number3)
finalnumber = number1 + number2 + number3
print("итого: ", finalnumber)

#Задание 4
number = input("Введи целое положительное число\n")
if number.isdigit():
    number = int(number)
    high_number = number % 10
    number = number // 10
    while number > 0:
        if number % 10 > high_number:
            high_number = number % 10
        number = number // 10
print("Самая большая цифра: ", high_number)

#Задание 5
revenue = input("Введи выручку компании\n")
revenue = int(revenue)
expenses = input("Введи расходы фирмы\n")
expenses = int(expenses)
if revenue > expenses:
    print("Прибыль")
    profitability = revenue % expenses
    print("Рентабельность:", profitability)
    personal = input("Сколько человек работает?")
    personal = int(personal)
    profit_per_person = profitability // personal
    print("выручка на человека составляет: ", profit_per_person)
else:
    print("Убыток")

#Задание 6
distance = input("Сколько пробежал?\n")
distance = int(distance)
wanted = input("Цель\n")
wanted = int(wanted)
day = 1
while distance < wanted:
    distance = distance * 1.1
    day = day + 1
print("день достижения цели: ", day)

#Спасибо!!!



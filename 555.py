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
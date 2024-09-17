# 5. Баланс по сметка
# Напишете програма, която пресмята колко общо пари има в сметката, след като направите определен брой вноски.
# На всеки ред ще получавате сумата, която трябва да внесете в сметката, до получаване на команда "NoMoreMoney ".
# При всяка получена сума на конзолата трябва да се извежда "Increase: " + сумата и тя да се прибавя в сметката.
# Ако получите число по-малко от 0 на конзолата трябва да се изведе "Invalid operation!" и програмата да приключи.
# Когато програмата приключи трябва да се принтира "Total: " + общата сума в сметката форматирана до втория знак
# след десетичната запетая.

input_balance = input()
total_balance = 0
while input_balance != "NoMoreMoney":
    if float(input_balance) >= 0:
        print(f"Increase: {float(input_balance):.2f}")
        total_balance += float(input_balance)
        input_balance = input()
    else:
        print("Invalid operation!")
        break
print(f"Total: {total_balance:.2f}")












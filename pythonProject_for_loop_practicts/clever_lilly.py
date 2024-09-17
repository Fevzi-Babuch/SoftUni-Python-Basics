# 4. Умната Лили
# Лили вече е на N години. За всеки свой рожден ден тя получава подарък.
# · За нечетните рождени дни (1, 3, 5...n) получава играчки.
# · За четните рождени дни (2, 4, 6...n) получава пари.
# За втория рожден ден получава 10.00 лв, като сумата се увеличава с 10.00 лв., за всеки следващ четен рожден ден
# (2 -> 10, 4 -> 20, 6 -> 30...и т.н.). През годините Лили тайно е спестявала парите. Братът на Лили, в годините,
# които тя получава пари, взима по 1.00 лев от тях. Лили продала играчките получени през годините, всяка за P лева и
# добавила сумата към спестените пари. С парите искала да си купи пералня за X лева. Напишете програма, която да
# пресмята, колко пари е събрала и дали ѝ стигат да си купи пералня.
# Вход
# Програмата прочита 3 числа, въведени от потребителя, на отделни редове:
# · Възрастта на Лили - цяло число в интервала [1...77]
# · Цената на пералнята - число в интервала [1.00...10 000.00]
# · Единична цена на играчка - цяло число в интервала [0...40]

BROTHERS_TAX = 1
INCREMENT = 10
age_of_lilly = int(input())
price_for_washing_machine = float(input())
price_per_toy = int(input())
odd_birthdays = 0
even_birthdays = 0
sold_toys = 0

saved_money = 0

for age in range(1, age_of_lilly + 1):
    if age % 2 == 0:
        even_birthdays += INCREMENT
        saved_money += even_birthdays - BROTHERS_TAX

    else:
        odd_birthdays += 1

sold_toys = price_per_toy * odd_birthdays
saved_money += sold_toys

if saved_money >= price_for_washing_machine:
    print(f"Yes! {saved_money - price_for_washing_machine:.2f}")
else:
    print(f"No! {abs(saved_money - price_for_washing_machine):.2f}")






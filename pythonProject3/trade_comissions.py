# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите:
# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число), въведени от потребителя,
# и изчислява и извежда размера на търговската комисионна според горната таблица. Резултатът да се изведе форматиран
# до 2 цифри след десетичната точка. При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error"

city = str(input())
sales = float(input())
commission = -1
if city == "Sofia":
    if 0 <= sales <= 500:
        commission = 0.05
    if 500 < sales <= 1000:
        commission = 0.07
    if 1000 < sales <= 10000:
        commission = 0.08
    if sales > 10000:
        commission = 0.12
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = 0.045
    if 500 < sales <= 1000:
        commission = 0.075
    if 1000 < sales <= 10000:
        commission = 0.10
    if sales > 10000:
        commission = 0.13
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 0.055
    if 500 < sales <= 1000:
        commission = 0.08
    if 1000 < sales <= 10000:
        commission = 0.12
    if sales > 10000:
        commission = 0.145

if commission >= 0:
    print(f"{commission * sales:.2f}")
else:
    print("error")


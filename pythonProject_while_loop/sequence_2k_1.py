# 4. Редица числа 2k + 1
# Напишете програма, която чете число n, въведено от потребителя, и отпечатва всички числа ≤ n от редицата:
# 1, 3, 7, 15, 31, …. Всяко следващо число се изчислява като умножим предишното с 2 и добавим 1

number = int(input())
new_number = 1
while True:
    if new_number <= number:
        print(new_number)
        new_number = ((new_number * 2) + 1)
    else:
        break















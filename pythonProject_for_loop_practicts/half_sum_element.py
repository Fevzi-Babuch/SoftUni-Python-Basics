# 2. Елемент, равен на сумата на останалите
# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя,и проверява дали сред тях
# съществува число, което е равно на сумата на всички останали.
# · Ако има такъв елемент печата "Yes" и на нов ред "Sum = " + неговата стойност
# · Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между най-големия елемент и
# сумата на останалите (по абсолютна стойност)
import sys
n = int(input())
max_value = -sys.maxsize
sum_of_element = 0
for i in range(n):
    element = int(input())
    sum_of_element += element
    if element >= max_value:
        max_value = element

sum_of_element -= max_value
if max_value == sum_of_element:
    print("Yes")
    print(f"Sum = {max_value}")
else:
    print("No")
    print(f"Diff = {abs(max_value- sum_of_element)}")

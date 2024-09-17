# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,
# намира най-голямото измежду тях и го принтира. Въвежда се по едно число на ред.

from sys import maxsize

number = input()
min_number = maxsize
max_number = -maxsize
while number != "Stop":
    if int(number) > max_number:
        max_number = int(number)
    number = input()
print(max_number)













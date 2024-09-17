# 6. Сумиране на гласните букви
# Да се напише програма, която чете текст (стринг), въведен от потребителя, и изчислява и отпечатва сумата от
# стойностите на гласните букви според таблицата по-долу

sequence = input()
total = 0

for char in sequence:
    if char == "a":
        total += 1
    if char == "e":
        total += 2
    if char == "i":
        total += 3
    if char == "o":
        total += 4
    if char == "u":
        total += 5
print(total)








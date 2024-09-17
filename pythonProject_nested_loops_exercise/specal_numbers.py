# 5. Специални числа
# Да се напише програма, която чете едно цяло число N, въведено от потребителя, и генерира всички възможни "специални"
# числа от 1111 до 9999. За да бъде “специално” едно число, то трябва да отговаря на следното условие:
# · N да се дели на всяка една от неговите цифри без остатък.

number = int(input())
max_range = 9999
min_range = 1111
jump_number = False
for total_range in range(min_range, max_range + 1):

    if str(0) in str(total_range):
        continue
    for index, special_number in enumerate(str(total_range)):
        if number % int(special_number) == 0:
            jump_number = True
        else:
            jump_number = False
            break
    if jump_number:
        print(total_range, end=" ")















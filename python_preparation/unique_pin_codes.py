# Задача 6. Уникални PIN кодове
# Да се напише програма, която генерира трицифрени PIN кодове, като цифрите на всеки PIN код са в определен интервал.
# За да бъде валиден един PIN код той трябва да отговаря на следните условия:
# Първата и третата цифра трябва да бъдат четни
# Втората цифра трябва да бъде просто число в диапазона [2...7]
# Вход:
# От конзолата се четат 3 реда:
# Горната граница на първото число - цяло число в диапазона [1...9]
# Горната граница на второто число - цяло число в диапазона [1...9]
# Горната граница на третото число - цяло число в диапазона [1...9]
# Изход:
# Да се отпечатат на конзолата всички валидни трицифрени PIN кодове, чиито цифри отговарят на съответните интервали

first_number_max_value = int(input())
second_number_max_value = int(input())
third_number_max_value = int(input())
simple_numbers_in_range_2_to_7 = 2, 3, 5, 7
for first_number in range(2, first_number_max_value + 1, 2):
    for second_number in range(2, second_number_max_value + 1):
        if second_number in simple_numbers_in_range_2_to_7:
            for third_number in range(2, third_number_max_value + 1, 2):
                print(f"{first_number} {second_number} {third_number}")



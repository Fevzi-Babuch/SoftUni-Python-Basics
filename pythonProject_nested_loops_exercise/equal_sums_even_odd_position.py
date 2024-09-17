# 2. Еднакви суми на четни и нечетни позиции
# Напишете програма, която чете от конзолата две шестцифрени цели числа. Винаги първото въведено число ще бъде по-малко
# от второто. На конзолата да се отпечатат на 1, ред разделени с интервал, всички числа, които се намират между двете,
# прочетени от конзолата числа и отговарят на условието сумата от цифрите на четни и нечетни позиции да са равни.
# Ако няма числа, отговарящи на условието на конзолата не се извежда резултат.

number_1 = int(input())
number_2 = int(input())

for current_number in range(number_1, number_2 +1):
    sum_even = 0
    sum_odd = 0
    str_from_number = str(current_number)
    for index, value in enumerate(str_from_number):
        if index % 2 == 0:
            sum_even += int(value)
        else:
            sum_odd += int(value)
    if sum_even == sum_odd:
        print(current_number, end=" ")












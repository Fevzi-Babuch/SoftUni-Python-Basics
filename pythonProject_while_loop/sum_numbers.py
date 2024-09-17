# Напишете програма, която чете цяло число от конзолата и на всеки следващ ред цели числа, докато тяхната сума стане
# по-голяма или равна на първоначалното число. След приключване на четенето да се отпечата сумата на въведените числа

number = int(input())
sum_of_numbers = int(input())
while sum_of_numbers < number:
    new_number = int(input())
    sum_of_numbers += new_number

print(sum_of_numbers)







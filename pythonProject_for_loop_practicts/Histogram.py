# 3. Хистограма
# Дадени са n цели числа в интервала [1…1000]. От тях някакъв процент p1 са под 200, друг процент p2 са от 200 до 399,
# друг процент p3 са от 400 до 599, друг процент p4 са от 600 до 799 и останалите p5 процента са от 800 нагоре.
# Да се напише програма, която изчислява и отпечатва процентите p1, p2, p3, p4 и p5.
# Пример: имаме n = 20 числа: 53, 7, 56, 180, 450, 920, 12, 7, 150, 250, 680, 2, 600, 200, 800, 799, 199, 46, 128, 65.
# Получаваме следното разпределение и визуализация:

RIGHT_BOUNDARY_P1 = 199
LEFT_BOUNDARY_P2 = 200
RIGHT_BOUNDARY_P2 = 399
LEFT_BOUNDARY_P3 = 400
RIGHT_BOUNDARY_P3 = 599
LEFT_BOUNDARY_P4 = 600
RIGHT_BOUNDARY_P4 = 799
LEFT_BOUNDARY_P5 = 800

num_count = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for _ in range(num_count):
    current_number = int(input())

    if current_number <= RIGHT_BOUNDARY_P1:
        p1_count += 1
    elif LEFT_BOUNDARY_P2 <= current_number <= RIGHT_BOUNDARY_P2:
        p2_count += 1
    elif LEFT_BOUNDARY_P3 <= current_number <= RIGHT_BOUNDARY_P3:
        p3_count += 1
    elif LEFT_BOUNDARY_P4 <= current_number <= RIGHT_BOUNDARY_P4:
        p4_count += 1
    elif LEFT_BOUNDARY_P5 <= current_number:
        p5_count += 1

print(f"{p1_count / num_count * 100:.2f}%")
print(f"{p2_count / num_count * 100:.2f}%")
print(f"{p3_count / num_count * 100:.2f}%")
print(f"{p4_count / num_count * 100:.2f}%")
print(f"{p5_count / num_count * 100:.2f}%")






# 9. Лява и дясна сума
# Да се напише програма, която чете 2 * n-на брой цели числа, подадени от потребителя, и проверява дали сумата на
# първите n числа (лява сума) е равна на сумата на вторите n числа (дясна сума).
# При равенство печата "Yes, sum = " + сумата; иначе печата "No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).

n = int(input())
left_sum = 0
right_sum = 0

for i in range(1, n+1):
    left_sum = left_sum + int(input())
for i in range(2, n+2):
    right_sum = right_sum + int(input())

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(right_sum - left_sum)
    print(f"No, diff = {diff}")



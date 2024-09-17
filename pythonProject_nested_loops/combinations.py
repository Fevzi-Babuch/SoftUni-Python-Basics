# Напишете програма, която изчислява колко решения в естествените числа (включително и нулата) има уравнението:
# x1 + x2 + x3 = n
# Числото n е цяло число и се въвежда от конзолата.

n = int(input())
combinations_count = 0

for i in range(0, n + 1):
    for j in range(0, n + 1):
        for h in range(0, n + 1):
            if (i + j + h) == n:
                combinations_count += 1
print(combinations_count)







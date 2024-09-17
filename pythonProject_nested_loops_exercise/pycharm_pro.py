number = int(input())
number_count = 1
col_count = 1
while number_count <= number:
    for _ in range(col_count):
        print(number_count, end=" ")
        number_count += 1
        if number_count > number:
            break
    print()
    col_count += 1






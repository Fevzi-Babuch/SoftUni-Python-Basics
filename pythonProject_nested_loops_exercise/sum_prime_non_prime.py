# 3. Суми прости и непрости числа
# Напишете програма, която чете от конзолата цели числа, докато не се получи команда "stop".
# Да се намери сумата на всички въведени прости и сумата на всички въведени непрости числа.
# Тъй като по дефиниция от математиката отрицателните числа не могат да бъдат прости, ако на входа се
# подаде отрицателно число, да се изведе следното съобщение "Number is negative.". В този случай въведено
# число се игнорира и не се прибавя към нито една от двете суми, а програмата продължава своето изпълнение,
# очаквайки въвеждане на следващо число.
# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
# · "Sum of all prime numbers is: {prime numbers sum}"
# · "Sum of all non prime numbers is: {nonprime numbers sum}"

STOP_STRING = "stop"
sum_primes = 0
sum_non_primes = 0
current_number = ""
while True:
    current_number = input()
    if current_number == STOP_STRING:
        break

    current_number = int(current_number)
    if current_number < 0:
        print("Number is negative.")
        continue

    for number_count in range(2, current_number + 1):
        if current_number % number_count == 0 and current_number != number_count:
            sum_non_primes += current_number
            break
        if current_number == number_count:
            sum_primes += current_number
print(f"Sum of all prime numbers is: {sum_primes}")
print(f"Sum of all non prime numbers is: {sum_non_primes}")













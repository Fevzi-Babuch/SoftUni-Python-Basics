# Да се напише програма, която чете час и минути от 24-часово денонощие, въведени от потребителя и изчислява колко
# ще е часът след 15 минути. Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23,
# а минутите винаги са между 0 и 59. Часовете се изписват с една или две цифри. Минутите се изписват винаги с по
# две цифри, с водеща нула, когато е необходимо.

current_hours = int(input())
current_minutes = int(input())

next_minutes = current_minutes + 15
next_hours = current_hours

if next_minutes >= 60:
    next_hours += 1
    next_minutes = next_minutes - 60
if next_hours >= 24:
    next_hours -= 24

result_hours = str(next_hours)
result_minutes = str(next_minutes)

if next_minutes < 10:
    result_minutes = str("0" + result_minutes)

print(f"{result_hours}:{result_minutes}")






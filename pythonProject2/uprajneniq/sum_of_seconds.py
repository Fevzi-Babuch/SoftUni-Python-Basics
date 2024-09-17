# Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50). Да се напише програма, която чете
# времената на състезателите в секунди, въведени от потребителя и пресмята сумарното им време във формат "минути:секунди".
# Секундите да се изведат с водеща нула (2 à "02", 7 à "07", 35 à "35").

first_contestant = int(input())
second_contestant = int(input())
third_contestant = int(input())

sum_seconds = first_contestant + second_contestant + third_contestant

minutes = sum_seconds // 60
seconds = sum_seconds % 60

# print(f"{minutes}:{seconds:02d}")

if seconds < 10:
    print(f"{minutes}:0{seconds}")

else:
    print(f"{minutes}:{seconds}")





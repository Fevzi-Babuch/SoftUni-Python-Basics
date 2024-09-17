# Иван решава да подобри Световния рекорд по плуване на дълги разстояния. На конзолата се въвежда рекордът в секунди,
# който Иван трябва да подобри, разстоянието в метри, което трябва да преплува и времето в секунди,
# за което плува разстояние от 1 м. Да се напише програма, която изчислява дали се е справил със задачата,
# като се има предвид, че: съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.
# Когато се изчислява колко пъти Иван ще се забави, в резултат на съпротивлението на водата,
# резултатът трябва да се закръгли надолу до най-близкото цяло число.
# Да се изчисли времето в секунди, за което Иван ще преплува разстоянието и разликата спрямо Световния рекорд.
import math

SLOW_EVERY_X_METERS = 15
SLOWED_BY = 12.5

current_record = float(input())
distance = float(input())
time_per_meter = float(input())

total_time = distance * time_per_meter
rest_of_distance = distance // 15
time_discount = rest_of_distance * SLOWED_BY
total_time += time_discount
if total_time < current_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    not_enough_time = abs(current_record - total_time)
    print(f"No, he failed! He was {not_enough_time:.2f} seconds slower.")





# Григор Димитров е тенисист, чиято следваща цел е изкачването в световната ранглиста по тенис за мъже.
# През годината Гришо участва в определен брой турнири, като за всеки турнир получава точки, които зависят от позицията,
# на която е завършил в турнира. Има три варианта за завършване на турнир:
# § W - ако е победител получава 2000 точки
# § F - ако е финалист получава 1200 точки
# § SF - ако е полуфиналист получава 720 точки
# Напишете програма, която изчислява колко ще са точките на Григор след изиграване на всички турнири, като знаете с
# колко точки стартира сезона. Също изчислете колко точки средно печели от всички изиграни турнири и колко процента
# от турнирите е спечелил.
# Вход
# От конзолата първо се четат два реда:
# · Брой турнири, в които е участвал – цяло число в интервала [1…20]
# · Начален брой точки в ранглистата - цяло число в интервала [1...4000]
# За всеки турнир се прочита отделен ред:
# · Достигнат етап от турнира – текст – "W", "F" или "SF"
# Изход
# Отпечатват се три реда в следния формат:
# · "Final points: {брой точки след изиграните турнири}
# "Average points: {средно колко точки печели за турнир}"
# · "{процент спечелени турнири}%"
# Средните точки да бъдат закръглени към най-близкото цяло число надолу, а процентът да се форматира
# до втората цифра след десетичния знак.
import math

WINNER = "W"
FINALIST = "F"
SEMIFINAL = "SF"
WINNER_POINTS = 2000
FINALIST_POINTS = 1200
SEMIFINALIST_POINTS = 720
tournament_points = 0
tournaments_winner = 0
tournament_count = int(input())
initial_points = int(input())
for _ in range(tournament_count):
    stage_of_tournament = input()
    if stage_of_tournament == WINNER:
        tournament_points += WINNER_POINTS
        tournaments_winner += 1
    elif stage_of_tournament == FINALIST:
        tournament_points += FINALIST_POINTS
    elif stage_of_tournament == SEMIFINAL:
        tournament_points += SEMIFINALIST_POINTS

final_points = initial_points + tournament_points
average_points = tournament_points / tournament_count
percentage_winner = tournaments_winner / tournament_count * 100

print(f"Final points: {math.floor(final_points)}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percentage_winner:.2f}%")




















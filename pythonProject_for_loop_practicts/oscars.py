
LIMIT_POINTS = 1250.5
points_for_actor = 0
actors_name = input()
points_from_academy = float(input())
number_of_judges = int(input())
total_points = points_from_academy
for _ in range(number_of_judges):
    judge_name = input()
    points_from_judge = float(input())
    juror_points = (len(judge_name) * points_from_judge) / 2
    points_for_actor += juror_points
    total_points = points_for_actor + points_from_academy
    if total_points >= LIMIT_POINTS:
        break

if total_points >= LIMIT_POINTS:
    print(f"Congratulations, {actors_name} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actors_name} you need {(LIMIT_POINTS - total_points):.1f} more!")






# Снимките за дългоочаквания филм "Годзила срещу Конг" започват. Сценаристът Адам Уингард ви моли да напишете програма,
# която да изчисли, дали предвидените средства са достатъчни за снимането на филма.
# За снимките ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
# · Декорът за филма е на стойност 10% от бюджета.
# · При повече от 150 статиста, има отстъпка за облеклото на стойност 10%.

movie_budget = float(input())
number_of_statists = int(input())
each_statist_clothing_cost = float(input())
DECORATION_FOR_MOVIE = 10 / 100 * movie_budget
discount_for_total_clothing = 10 / 100 * each_statist_clothing_cost
if number_of_statists > 150:
    each_statist_clothing_cost = each_statist_clothing_cost - discount_for_total_clothing
total_clothing_cost = number_of_statists * each_statist_clothing_cost
movie_cost = total_clothing_cost + DECORATION_FOR_MOVIE
if movie_cost > movie_budget:
    not_enough = movie_cost - movie_budget
    print("Not enough money!")
    print(f"Wingard needs {not_enough:.02f} leva more.")

else:
    rest_of_the_money = movie_budget - movie_cost
    print("Action!")
    print(f"Wingard starts filming with {rest_of_the_money:.02f} leva left.")








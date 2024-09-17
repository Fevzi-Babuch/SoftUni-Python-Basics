# 7. Трекинг мания
# Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване. Според размера на
# групата, катерачите ще изкачват различни върхове.
# · Група до 5 човека – изкачват Мусала
# · Група от 6 до 12 човека – изкачват Монблан
# · Група от 13 до 25 човека – изкачват Килиманджаро
# · Група от 26 до 40 човека – изкачват К2
# · Група от 41 или повече човека – изкачват Еверест
# Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# · На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
# · За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]
# Изход
# Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00% с точност до
# втората цифра след десетичната запетая.
group_musala = 0
group_montblanc = 0
group_kilimanjaro = 0
group_k2 = 0
group_everest = 0
group_of_climbers = int(input())
for _ in range(group_of_climbers):
    people_in_group = int(input())
    if 0 < people_in_group <= 5:
        group_musala += people_in_group
    elif 5 < people_in_group < 13:
        group_montblanc += people_in_group
    elif 12 < people_in_group < 26:
        group_kilimanjaro += people_in_group
    elif 25 < people_in_group < 41:
        group_k2 += people_in_group
    elif 40 < people_in_group:
        group_everest += people_in_group

total_climbers = group_musala + group_montblanc + group_kilimanjaro + group_k2 + group_everest

percent_musala = group_musala / total_climbers * 100
percent_montblanc = group_montblanc / total_climbers * 100
percent_kilimanjaro = group_kilimanjaro / total_climbers * 100
percent_k2 = group_k2 / total_climbers * 100
percent_everest = group_everest / total_climbers * 100
print(f"{percent_musala:.2f}%")
print(f"{percent_montblanc:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")









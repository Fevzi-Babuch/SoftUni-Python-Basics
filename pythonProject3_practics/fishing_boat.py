# Тони и приятели много обичат да ходят за риба и са толкова запалени по риболова, че решават да отидат на риболов
# с кораб. Цената за наема на кораба зависи от сезона и броя рибари:
# В зависимост от сезона:
# Цената за наем на кораба през пролетта е 3000 лв.;
# Цената за наем на кораба през лятото и есента е 4200 лв.;
# Цената за наем на кораба през зимата е 2600 лв.
# В зависимост от броя на групата има различна отстъпка:
# Ако групата е до 6 човека включително - отстъпка от 10%;
# Ако групата е от 7 до 11 човека включително - отстъпка от 15%;
# Ако групата е от 12 нагоре - отстъпка от 25%.
# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен - тогава нямат допълнителна
# отстъпка, която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.
# От конзолата се четат три реда:
# Бюджет на групата - цяло число;
# Сезон - текст: "Spring", "Summer", "Autumn" или "Winter";
# Брой рибари - цяло число.

SPRING_PRICE = 3000
SUMMER_PRICE = 4200
AUTUMN_PRICE = SUMMER_PRICE
WINTER_PRICE = 2600

discount = 0/100
additional_discount = 0
ship_cost = 0

budget = int(input())
season = str(input())
fishers_count = int(input())

if (fishers_count % 2 == 0) and (season != "Autumn"):
    additional_discount = 5 / 100
    pass
if fishers_count <= 6:
    discount = 10 / 100
elif 6 < fishers_count <= 11:
    discount = 15 / 100
else:
    discount = 25 / 100
if season == "Spring":
    ship_cost = SPRING_PRICE
elif (season == "Summer") or (season == "Autumn"):
    ship_cost = SUMMER_PRICE
elif season == "Winter":
    ship_cost = WINTER_PRICE

fishing_total_cost = ship_cost - (ship_cost * discount)
fishing_total_cost_2 = fishing_total_cost - (fishing_total_cost * additional_discount)

if fishing_total_cost_2 <= budget:
    rest_money = budget - fishing_total_cost_2
    print(f"Yes! You have {rest_money:.2f} leva left.")
elif budget < fishing_total_cost_2:
    not_enough_money = fishing_total_cost_2 - budget
    print(f"Not enough money! You need {not_enough_money:.2f} leva.")







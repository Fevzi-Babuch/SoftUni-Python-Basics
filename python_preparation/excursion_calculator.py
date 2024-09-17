# Задача 3. Калкулатор за екскурзии
# Туристическа агенция предлага екскурзии на различни цени, според сезона и броя на хората.
# Напишете програма, която да изчислява цената, според данните от таблицата:

# SUMMER_DISCOUNT = 15 / 100
# WINTER_EXPENSE = 8 / 100
# SPRING = "spring"
# SUMMER = "summer"
# AUTUMN = "autumn"
# WINTER = "winter"
# persons_count = int(input())
# season = input()
# price = 0
# if persons_count <= 5:
#     if season == SPRING:
#         price = 50
#     elif season == SUMMER:
#         price = 48
#     elif season == AUTUMN:
#         price = 60
#     elif season == WINTER:
#         price = 86
# else:
#     if season == SPRING:
#         price = 48
#     elif season == SUMMER:
#         price = 45
#     elif season == AUTUMN:
#         price = 49.50
#     elif season == WINTER:
#         price = 85
#
# total_price = price * persons_count
# if season == SUMMER:
#     total_price -= total_price * SUMMER_DISCOUNT
# elif season == WINTER:
#     total_price += total_price * WINTER_EXPENSE
#
# print(f"{total_price:.2f} leva.")

people_count = int(input())
season = input()
price_per_person = 0

if people_count <= 5:
    if season == "spring":
        price_per_person = 50
    elif season == "summer":
        price_per_person = 48.50
    elif season == "autumn":
        price_per_person = 60
    elif season == "winter":
        price_per_person = 86
else:
    if season == "spring":
        price_per_person = 48
    elif season == "summer":
        price_per_person = 45
    elif season == "autumn":
        price_per_person = 49.50
    elif season == "winter":
        price_per_person = 85

price = people_count * price_per_person

if season == "summer":
    price *= 0.85
elif season == "winter":
    price *= 1.08

print(f"{price:.2f} leva.")



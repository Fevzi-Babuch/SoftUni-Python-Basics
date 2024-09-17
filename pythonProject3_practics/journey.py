# Млад програмист разполага с определен бюджет и свободно време в даден сезон. Напишете програма, която да приема на
# входа бюджета и сезона, а на изхода да изкарва къде ще почива програмистът и колко ще похарчи.
# Бюджетът определя дестинацията, а сезонът - колко от бюджета ще изхарчи. Ако е лято ще почива на къмпинг,
# а зимата в хотел. Ако е в Европа, независимо от сезона, ще почива в хотел. Всеки къмпинг или хотел,
# според дестинацията, има собствена цена, която отговаря на даден процент от бюджета:
# · При 100 лв. или по-малко - някъде в България:
# Лято - 30% от бюджета;
# Зима - 70% от бюджета.
# · При 1000 лв. или по малко - някъде на Балканите:
# Лято - 40% от бюджета;
# Зима - 80% от бюджета.
# · При повече от 1000 лв. - някъде из Европа:
# При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.

DESTINATION_1 = "Bulgaria"
DESTINATION_2 = "Balkans"
DESTINATION_3 = "Europe"
REST_PLACE_1 = "Camp"
REST_PLACE_2 = "Hotel"

budget = float(input())
season = str(input())
destination = ""
money_spend = 0
rest_place = ""
if budget <= 1000:
    if season == "summer":
        rest_place = REST_PLACE_1
        if budget <= 100:
            destination = DESTINATION_1
            money_spend = 30 / 100
        if 100 < budget <= 1000:
            destination = DESTINATION_2
            money_spend = 40 / 100
    elif season == "winter":
        rest_place = REST_PLACE_2
        if budget <= 100:
            destination = DESTINATION_1
            money_spend = 70 / 100
        if 100 < budget <= 1000:
            destination = DESTINATION_2
            money_spend = 80 / 100
else:
    destination = DESTINATION_3
    money_spend = 90 / 100
    rest_place = REST_PLACE_2

journey_cost = money_spend * budget
print(f"Somewhere in {destination}")
print(f"{rest_place} - {journey_cost:.2f}")


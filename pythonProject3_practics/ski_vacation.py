# Атанас решава да прекара отпуската си в Банско и да кара ски. Преди да отиде обаче, трябва да резервира хотел и да
# изчисли колко ще му струва престоя. Налични са следните видове помещения, със следните цени за престой:
# "room for one person" – 18.00 лв за нощувка
# "apartment" – 25.00 лв за нощувка
# "president apartment" – 35.00 лв за нощувка
# Според броят на дните, в които ще остане в хотела (пример: 11 дни = 10 нощувки) и видът на помещението,
# което ще избере, той може да ползва различно намаление.

SINGLE_ROOM_NIGHT = 18
APARTMENT_NIGHT = 25
PRESIDENT_NIGHT = 35
residence_days = int(input())
type_of_room = input()
feedback = input()

single_room = "room for one person"
apartment = "apartment"
president = "president apartment"


feedback_positive = "positive"
feedback_negative = "negative"
feedback_discount = 10 / 100
feedback_expense = 25 / 100
residence_nights = residence_days - 1
discount = 0
price_for_night = 0
if type_of_room == single_room:
    price_for_night = SINGLE_ROOM_NIGHT
elif type_of_room == apartment:
    price_for_night = APARTMENT_NIGHT
elif type_of_room == president:
    price_for_night = PRESIDENT_NIGHT

residence_cost = residence_nights * price_for_night
if type_of_room == single_room:
    discount = 0
elif type_of_room == apartment:
    if residence_days < 10:
        discount = residence_cost * (30 / 100)
        final_price = residence_cost - discount
    elif 10 <= residence_days <= 15:
        discount = residence_cost * (35 / 100)
        final_price = residence_cost - discount
    elif residence_days > 15:
        discount = residence_cost * (50 / 100)
elif type_of_room == president:
    if residence_days < 10:
        discount = residence_cost * (10 / 100)
    elif 10 <= residence_days <= 15:
        discount = residence_cost * (15 / 100)
    elif residence_days > 15:
        discount = residence_cost * (20 / 100)

final_price = residence_cost - discount
if feedback == feedback_positive:
    final_price = final_price + (final_price * feedback_expense)
elif feedback == feedback_negative:
    final_price = final_price - (final_price * feedback_discount)
print(f"{final_price:.2f}")











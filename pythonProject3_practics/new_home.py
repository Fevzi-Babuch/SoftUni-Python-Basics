# Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята, че Ви убеждава да напишете програма,
# която да изчисли колко ще им струва, за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен.
# Различните цветя са с различни цени
# Съществуват следните отстъпки:
# Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# Ако Нели купи повече от 90 Далии - 15% отстъпка от крайната цена;
# Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
# От конзолата се четат 3 реда:
# Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# Брой цветя - цяло число;
# Бюджет - цяло число.
# Да се отпечата на конзолата на един ред:
# Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.

ROSES_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

flowers_type = str(input())
flowers_count = int(input())
budget = int(input())
flower_price = 0
discount = 0
total_cost = 0
if flowers_type == "Roses":
    flower_price = ROSES_PRICE
    if flowers_count > 80:
        discount = 0.10

elif flowers_type == "Dahlias":
    flower_price = DAHLIAS_PRICE
    if flowers_count > 90:
        discount = 0.15

elif flowers_type == "Tulips":
    flower_price = TULIPS_PRICE
    if flowers_count > 80:
        discount = 0.15

elif flowers_type == "Narcissus":
    flower_price = NARCISSUS_PRICE
    if flowers_count < 120:
        discount = -0.15

elif flowers_type == "Gladiolus":
    flower_price = GLADIOLUS_PRICE
    if flowers_count < 80:
        discount = -0.20

total_cost = flowers_count * flower_price
price_with_discount = total_cost - (total_cost * discount)

if price_with_discount <= budget:
    rest_of_money = budget - price_with_discount
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {rest_of_money:.2f} leva left.")
else:
    not_enough = price_with_discount - budget
    print(f"Not enough money, you need {not_enough:.2f} leva more.")












# Петър иска да купи N видеокарти, M процесора и P на брой рам памет. Ако броя на видеокартите е по-голям от този на
# процесорите получава 15% отстъпка от крайната сметка. Важат следните цени:
# · Видеокарта – 250 лв./бр.
# · Процесор – 35% от цената на закупените видеокарти/бр.
# · Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.
# Входът се състои от четири реда:
# 1. Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# 2. Броят видеокарти - цяло число в интервала [1…100]
# 3. Броят процесори - цяло число в интервала [1…100]
# 4. Броят рам памет - цяло число в интервала [1…100]
import math

GRAPHIC_CARD = 250
PROCESSOR = 35 / 100
RAM_CARD = 10 / 100
DISCOUNT_TO_TOTAL_PRICE = 15 / 100

budget = float(input())
graphics_count = int(input())
processors_count = int(input())
ram_cards_count = int(input())

graphics_total = graphics_count * GRAPHIC_CARD

single_cpu = graphics_total * PROCESSOR
processors_total = processors_count * single_cpu

single__ram = graphics_total * RAM_CARD
ram_total = ram_cards_count * single__ram

total_purchase_cost = graphics_total + processors_total + ram_total
grand_total = total_purchase_cost

if graphics_count > processors_count:
    grand_total = total_purchase_cost - total_purchase_cost * DISCOUNT_TO_TOTAL_PRICE


if budget >= grand_total:
    rest_budget = budget - grand_total
    print(f"You have {rest_budget:.2f} leva left!")
else:
    money_needed = grand_total - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")



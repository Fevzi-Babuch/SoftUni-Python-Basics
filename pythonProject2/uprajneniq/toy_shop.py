# Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни.
# С парите, които ще спечели иска да отиде на екскурзия.
# Цени на играчките:
# · Пъзел - 2.60 лв.
# · Говореща кукла - 3 лв.
# · Плюшено мече - 4.10 лв.
# · Миньон - 8.20 лв.
# · Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.
# · Ако парите са достатъчни се отпечатва:
# "Yes! {оставащите пари} lv left."
# · Ако парите НЕ са достатъчни се отпечатва:
# "Not enough money! {недостигащите пари} lv needed."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

# TOYS LIST PRICES => Constants

PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

excursion_cost = float(input())
puzzle_orders = int(input())
doll_orders = int(input())
bear_orders = int(input())
minion_orders = int(input())
truck_orders = int(input())

puzzle_total = puzzle_orders * PUZZLE_PRICE
doll_total = doll_orders * TALKING_DOLL_PRICE
bear_total = bear_orders * TEDDY_BEAR_PRICE
minion_total = minion_orders * MINION_PRICE
truck_total = truck_orders * TRUCK_PRICE

total_order_toys = puzzle_orders + doll_orders + bear_orders + minion_orders + truck_orders
total_order_price = puzzle_total + doll_total + bear_total + minion_total + truck_total
shop_discount = 25 / 100
shop_rent = 10 / 100
if total_order_toys >= 50:
    total_order_price = total_order_price - (total_order_price*shop_discount)
    total_order_price -= (total_order_price * shop_rent)
else:
    total_order_price = total_order_price - (total_order_price * shop_rent)
if total_order_price >= excursion_cost:
    rest_price = total_order_price - excursion_cost
    print(f"Yes! {rest_price:.2f} lv left.")
else:
    print(f"Not enough money! {excursion_cost - total_order_price:.2f} lv needed.")




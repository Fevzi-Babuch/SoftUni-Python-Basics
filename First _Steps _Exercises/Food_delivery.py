# Ресторант отваря врати и предлага няколко менюта на преференциални цени:
# • Пилешко меню – 10.35 лв.
# • Меню с риба – 12.40 лв.
# • Вегетарианско меню – 8.15 лв.
# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
# Цената на доставка е 2.50 лв и се начислява най-накрая.

chicken_menu = float(10.35)
fish_menu = float(12.40)
vegetarian_menu = float(8.15)
delivery_price = float(2.50)

chicken_menu_order = int(input())
fish_menu_order = int(input())
vegetarian_menu_order = int(input())

total_orders = (chicken_menu_order * chicken_menu) + (fish_menu_order * fish_menu) + \
               (vegetarian_menu_order * vegetarian_menu)
desert_price = total_orders * (20 / 100)
total_order_price = total_orders + desert_price + delivery_price
print(total_order_price)


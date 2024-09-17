# Задача 1. PC Store
# Иван искал да си купи няколко части за неговия компютър и отишъл в магазин. Понеже там нямало частите в наличност,
# те трябвало да ги поръчат. Той искал да си купи процесор, видео карта и RAM памет, като за процесора и видео картата
# магазинът му прави няколко процента отстъпка. Всичко трябвало да плати в долари, затова трябва цените да се обърнат в
# лева, като приемем, че 1 долар = 1.57 лева.
# Да се напише програма, която пресмята колко общо пари ще му трябват в лева, за да може да си закупи частите.
# Вход
# От конзолата се прочитат 5 реда:
# •	На първи ред: цената в долари за процесора – реално число в интервала [200.00 … 3000.00]
# •	На втори ред: цената в долари за видео карта – реално число в интервала [100.00 … 1500.00]
# На трети ред: цената в долари за една RAM памет – реално число в интервала [80.00 ... 500.00]
# •	На четвърти: ред брой RAM памети – цяло число в интервала [1 ... 4]
# •   На пети ред: процент отстъпка – реално число в интервала [0.01 … 0.1]
# Изход
# Да се отпечата на конзолата на един ред:
# •   Колко общо лева ще му трябват, за да си закупи частите.
#    "Money needed - {общо лева} leva."

DOLLAR_RATE = 1.57

cpu_price = float(input()) * DOLLAR_RATE
gpu_price = float(input()) * DOLLAR_RATE
ram_price = float(input()) * DOLLAR_RATE
ram_quantity = int(input())
discount = float(input())

discounted_products = (cpu_price + gpu_price) * discount
total_price = (cpu_price + gpu_price + (ram_price * ram_quantity))
total_price -= discounted_products


print(f"Money needed - {total_price:.2f} leva.")












# 7. Преместване
# На осемнадесетия си рожден ден Хосе взел решение, че ще се изнесе да живее на квартира. Опаковал багажа си в кашони
# и намерил подходяща обява за апартамент под наем. Той започва да пренася своя багаж на части, защото не може наведнъж.
# Има ограничено свободно пространство в новото си жилище, където може да разположи вещите, така че мястото да
# бъде подходящо за живеене.
# Напишете програма, която изчислява свободния обем от жилището на Хосе, който остава, след като пренесе багажа си.
# Всеки кашон е с точни размери: 1m x 1m x 1m.
# Вход
# Потребителят въвежда следните данни на отделни редове:
# 1. Широчина на свободното пространство - цяло число;
# 2. Дължина на свободното пространство - цяло число;
# 3. Височина на свободното пространство - цяло число;
# 4. На следващите редове (до получаване на команда "Done") - брой кашони, които се пренасят в квартирата - цели числа
# Програмата трябва да приключи прочитането на данни при команда "Done" или ако свободното място свърши.

BOX_SIZE = 1 ** 3
FINAL_COMMAND = "Done"
length = int(input())
width = int(input())
height = int(input())
total_apartment_volume = length * width * height
total_space_for_boxes = total_apartment_volume // BOX_SIZE
while total_space_for_boxes >= 0:
    command = input()
    if command != FINAL_COMMAND:
        command = int(command)
        total_space_for_boxes -= command
        if total_space_for_boxes <= 0:
            print(f"No more free space! You need {abs(total_space_for_boxes)} Cubic meters more.")
            break
    else:
        print(f"{abs(total_space_for_boxes)} Cubic meters left.")
        break











# Задача 5. Разпродажба на екскурзии
# Туристическа фирма разпродава финални екскурзионни пакети за края на годината. Напишете програма,
# която да изчислява, печалбата от разпродажбата и дали са продадени всички пакети или не, като знаете първоначалния
# брой екскурзии и техните цени. Фирмата предлага два вида екскурзии – море ("sea") на цена 680 лева и
# планина ("mountain") на цена 499 лева. При избор на даден пакет, към общата сума се добавя съответната цена.
# При избор на пакет, който вече не е наличен (броят му е равен на 0), не трябва да се добавя към общата цена.
# Вход:
# От конзолата първоначално се четат 2 реда:
# Брой екскурзии за море – цяло число в интервала [1… 500]
# Брой екскурзии за планина – цяло число в интервала [1… 500]
# След това се чете по един ред до получаване на команда "Stop" или докато фирмата не продаде всички пакети:

# Име на пакет – текст с възможности "sea" или "mountain"
# Изход:
# На конзолата се отпечатват 1 или  2 реда, според случая:
# Ако фирмата е успяла да продаде всички пакети:
# " Good job! Everything is sold."
# Винаги се отпечатва:
# "Profit: {печалба от продажбите} leva."
SEA_PACKAGE_PRICE = 680
MOUNTAIN_PACKAGE_PRICE = 499
STOP_STRING = "Stop"
SEA_TYPE_STRING = "sea"
MOUNTAIN_TYPE_STRING = "mountain"

sea_packages_available = int(input())
mountain_packages_available = int(input())
sea_packages_sold = 0
mountain_packages_sold = 0
total_packages_available = sea_packages_available + mountain_packages_available
total_profit = 0


while True:
    package_type = input()
    if package_type == STOP_STRING:
        break
    if package_type == MOUNTAIN_TYPE_STRING and mountain_packages_sold < mountain_packages_available:
        mountain_packages_sold += 1
        total_profit += MOUNTAIN_PACKAGE_PRICE
        total_packages_available -= 1
    elif package_type == SEA_TYPE_STRING and sea_packages_sold < sea_packages_available:
        sea_packages_sold += 1
        total_profit += SEA_PACKAGE_PRICE
        total_packages_available -= 1
    if total_packages_available == 0:
        print("Good job! Everything is sold.")
        break

print(f"Profit: {total_profit} leva.")








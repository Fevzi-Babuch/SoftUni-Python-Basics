# Учебната година вече е започнала и отговорничката на 10Б клас - Ани трябва да купи определен брой пакетчета с химикали,
# пакетчета с маркери, както и препарат за почистване на дъска. Тя е редовна клиентка на една книжарница, затова има
# намаление за нея, което представлява някакъв процент от общата сума. Напишете програма, която изчислява колко пари ще
# трябва да събере Ани, за да плати сметката, като имате предвид следния ценоразпис:
# • Пакет химикали - 5.80 лв.
# • Пакет маркери - 7.20 лв.
# • Препарат - 1.20 лв (за литър)

PEN_PACK_PRICE = 5.8
MARKERS_PACK_PRICE = 7.2
CLEANING_PRODUCT_LITER_PRICE = 1.2

pens = int(input())
markers = int(input())
cleaning_product = int(input())
percent_of_discount = float(input()) / 100

total_pens = pens * PEN_PACK_PRICE
total_markers = markers * MARKERS_PACK_PRICE
total_cleaning_product = cleaning_product * CLEANING_PRODUCT_LITER_PRICE
total_purchases = total_markers + total_pens + total_cleaning_product

purchase_final_price = total_purchases - (total_purchases * percent_of_discount)

print(purchase_final_price)



# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони. Има три вида прожекции с
# билети на различни цени:
#  Premiere - премиерна прожекция, на цена 12.00 лева;
#  Normal - стандартна прожекция, на цена 7.50 лева;
#  Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която чете тип прожекция (текст), брой редове и брой колони в залата (цели числа),
# въведени от потребителя, и изчислява общите приходи от билети при пълна зала. Резултатът да се отпечата във
# формат 2 знака след десетичната точка

PREMIERE = 12.00
NORMAL = 7.50
DISCOUNT = 5.00

type_of_projection = str(input())
row_number = int(input())
column_number = int(input())
total_seats = row_number * column_number
ticket_price = 0
if type_of_projection == "Premiere":
    ticket_price = PREMIERE
elif type_of_projection == "Normal":
    ticket_price = NORMAL
elif type_of_projection == "Discount":
    ticket_price = DISCOUNT

cinema_profit = ticket_price * total_seats
print(f"{cinema_profit:.2f}")




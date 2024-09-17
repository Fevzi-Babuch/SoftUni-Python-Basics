# Лятото е сезон с много променливо време и Виктор има нужда от вашата помощ. Напишете програма, която спрямо времето
# от денонощието и градусите да препоръча на Виктор какви дрехи да облече. Вашият приятел има различни планове за всеки
# етап от деня, които изискват и различен външен вид - може да ги видите от таблицата.
# От конзолата се четат точно два реда:
# Градусите - цяло число;
# Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".

MORNING = "Morning"
AFTERNOON = "Afternoon"
EVENING = "Evening"

temperature = int(input())
part_of_day = str(input())

COLD = (10 <= temperature <= 18)
REGULAR = (18 < temperature <= 24)
HOT = (temperature >= 25)

if COLD:
    if part_of_day == MORNING:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif (part_of_day == AFTERNOON) or (part_of_day == EVENING):
        outfit = "Shirt"
        shoes = "Moccasins"
if REGULAR:
    if (part_of_day == MORNING) or (part_of_day == EVENING):
        outfit = "Shirt"
        shoes = "Moccasins"
    elif part_of_day == AFTERNOON:
        outfit = "T-Shirt"
        shoes = "Sandals"
if HOT:
    if part_of_day == MORNING:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif part_of_day == AFTERNOON:
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif part_of_day == EVENING:
        outfit = "Shirt"
        shoes = "Moccasins"
print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")


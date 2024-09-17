# Хотел предлага 2 вида стаи: студио и апартамент. Напишете програма, която изчислява цената за целия престой за
# студио и апартамент. Цените зависят от месеца на престоя:
# Предлагат се и следните отстъпки:
# · За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# · За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# · За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# · За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.
# Входът се чете от конзолата и съдържа точно 2 реда, въведени от потребителя:
# · На първия ред е месецът - May, June, July, August, September или October;
# На втория ред е броят на нощувките - цяло число.

month = str(input())
nights = int(input())
studio_price_per_night = 0
flat_price_per_night = 0
discount_for_studio = 0
discount_for_flat = 0

if (month == "May") or (month == "October"):
    studio_price_per_night = 50
    flat_price_per_night = 65
    if 7 < nights < 14:
        discount_for_studio = 5 / 100
    if nights > 14:
        discount_for_studio = 30 / 100
if (month == "June") or (month == "September"):
    studio_price_per_night = 75.20
    flat_price_per_night = 68.70
    if nights > 14:
        discount_for_studio = 20 / 100
if (month == "July") or (month == "August"):
    studio_price_per_night = 76
    flat_price_per_night = 77
if nights > 14:
    discount_for_flat = 10 / 100

studio_total_price = nights * studio_price_per_night
studio_total_price_with_discount = studio_total_price - (studio_total_price * discount_for_studio)
flat_total_price = nights * flat_price_per_night
flat_total_price_with_discount = flat_total_price - (flat_total_price * discount_for_flat)

print(f"Apartment: {flat_total_price_with_discount:.2f} lv.")
print(f"Studio: {studio_total_price_with_discount:.2f} lv.")






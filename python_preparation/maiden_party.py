# Задача 2. Моминско парти
# Михаела държи сама да организира и заплати моминското си парти. Тя планува плащането да стане с приходите от онлайн
# магазина й. Да се напише програма, която пресмята печалбата от продажбите й.
# Цени на различните артикули:
# Любовно послание - 0.60 лв.
# Восъчна роза - 7.20 лв.
# Ключодържател - 3.60 лв.
# Карикатура - 18.20 лв.
# Късмет изненада - 22 лв.
# Ако поръчаните артикули са 25 или повече магазинът прави отстъпка 35% от общата цена. От спечелените пари Михаела
# трябва да предвиди и 10% разход за хостинг. Да се пресметне дали парите ще й стигнат да си плати моминското парти.
# Вход
# От конзолата се четат 6 реда:
# Цена на моминското парти - реално число в интервала [1.00 … 10000.00]
# Брой любовни послания - цяло число в интервала [0… 1000]
# Брой восъчни рози - цяло число в интервала [0 … 1000]
# Брой ключодържатели - цяло число в интервала [0 … 1000]
# Брой карикатури - цяло число в интервала [0 … 1000]
# Брой късмети изненада - цяло число в интервала [0 … 1000]
# Изход
# На конзолата се отпечатва:
# Ако парите са достатъчни се отпечатва:
# "Yes! {оставащите пари} lv left."
# Ако парите НЕ са достатъчни се отпечатва:
# "Not enough money! {недостигащите пари} lv needed."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

LOVE_MESSAGE_PRICE = 0.60
WAX_ROSE_PRICE = 7.20
KEYCHAIN_PRICE = 3.60
CARICATURE_PRICE = 18.20
LUCKY_SURPRISE_PRICE = 22.00
DISCOUNT_PRICE = 35 / 100
HOSTING_PRICE = 10 / 100

party_cost = float(input())
love_messages = int(input())
wax_roses = int(input())
keychains = int(input())
caricatures = int(input())
lucky_surprises = int(input())


total_cost = ((love_messages * LOVE_MESSAGE_PRICE) + (wax_roses * WAX_ROSE_PRICE) + (keychains * KEYCHAIN_PRICE) +
              (caricatures * CARICATURE_PRICE) + (lucky_surprises * LUCKY_SURPRISE_PRICE))

budget = total_cost

if love_messages + wax_roses + keychains + caricatures + lucky_surprises >= 25:
    budget = (total_cost - (DISCOUNT_PRICE * total_cost))

budget -= HOSTING_PRICE * budget


if budget >= party_cost:
    print(f"Yes! {budget - party_cost:.2f} lv left.")
else:
    print(f"Not enough money! {party_cost - budget:.2f} lv needed.")












# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее да събере
# необходимата сума. Тя спестява или харчи част от парите си всеки ден. Ако иска да похарчи повече от наличните си пари,
# то тя ще похарчи колкото има и ще ѝ останат 0 лева.
# Вход
# От конзолата се четат:
# ⦁	Пари, нужни за екскурзията - реално число;
# ⦁	Налични пари - реално число.
# След това многократно се четат по два реда:
# ⦁	Вид действие – текст с две възможности: "spend" или "save";
# ⦁	Сумата, която ще спести/похарчи - реално число.
# Изход
# Програмата трябва да приключи при следните случаи:
# ⦁	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
# ⦁	"You can't save the money."
# ⦁	"{Общ брой изминали дни}"
# ⦁	Ако Джеси събере парите за почивката, на конзолата се изписва:
# ⦁	"You saved the money for {общ брой изминали дни} days."

ACTION_SPEND = "spend"
ACTION_SAVE = "save"
SPEND_DAYS_IN_A_ROW_LIMIT = 5

needed_money = float(input())
available_money = float(input())
spend_in_a_row_count = 0
total_days_count = 0

while available_money < needed_money:

    action = input()
    action_amount = float(input())
    total_days_count += 1

    if action == ACTION_SAVE:
        available_money += action_amount
        spend_in_a_row_count = 0

    elif action == ACTION_SPEND:
        available_money -= action_amount
        spend_in_a_row_count += 1

        if available_money < 0:
            available_money = 0

    if spend_in_a_row_count >= SPEND_DAYS_IN_A_ROW_LIMIT:
        break

if spend_in_a_row_count == SPEND_DAYS_IN_A_ROW_LIMIT:
    print("You can't save the money.")
    print(f"{total_days_count}")

if available_money >= needed_money:
    print(f"You saved the money for {total_days_count} days.")







# ACTION_SPEND = "spend"
# ACTION_SAVE = "save"
# SPEND_DAYS_IN_A_ROW_LIMIT = 5
#
# needed_money = float(input())
# available_money = float(input())
# action = input()
#
# spend_in_a_row_count = 0
# total_days_count = 0
#
# while action == ACTION_SPEND:
#     total_days_count += 1
#     action_money = float(input())
#     available_money -= action_money
#     spend_in_a_row_count += 1
#     if available_money < 0:
#         available_money = 0
#     if spend_in_a_row_count == SPEND_DAYS_IN_A_ROW_LIMIT:
#         print("You can't save the money.")
#         print(f"{total_days_count}")
#         break
#     action = input()
#
# while action == ACTION_SAVE:
#     total_days_count += 1
#     action_money = float(input())
#     available_money += action_money
#     if available_money >= needed_money:
#         print(f"You saved the money for {total_days_count} days.")
#         break
#     action = input()



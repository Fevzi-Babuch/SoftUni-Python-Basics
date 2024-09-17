# плод    banana      apple    orange grapefruit   kiwi    pineapple   grapes
# цена     2.50       1.20      0.85     1.45       2.70      5.50      3.85
#
# През събота и неделя магазинът работи на по-високи цени:
#
# плод    banana   apple   orange    grapefruit    kiwi    pineapple   grapes
# цена     2.70    1.25    0.90       1.60         3.00     5.60       4.20

fruit = str(input())
day_of_week = str(input())
quantity_fruits = float(input())
fruit_price = 0
if fruit in ("banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"):
    if day_of_week in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
        if fruit == "banana":
            fruit_price = 2.50
        elif fruit == "apple":
            fruit_price = 1.20
        elif fruit == "orange":
            fruit_price = 0.85
        elif fruit == "grapefruit":
            fruit_price = 1.45
        elif fruit == "kiwi":
            fruit_price = 2.70
        elif fruit == "pineapple":
            fruit_price = 5.50
        elif fruit == "grapes":
            fruit_price = 3.85

        final_price = fruit_price * quantity_fruits
        print(f"{final_price:.2f}")

    elif day_of_week == "Saturday" or day_of_week == "Sunday":

        if fruit == "banana":
            fruit_price = 2.70
        elif fruit == "apple":
            fruit_price = 1.25
        elif fruit == "orange":
            fruit_price = 0.90
        elif fruit == "grapefruit":
            fruit_price = 1.60
        elif fruit == "kiwi":
            fruit_price = 3.00
        elif fruit == "pineapple":
            fruit_price = 5.60
        elif fruit == "grapes":
            fruit_price = 4.20

        final_price = fruit_price * quantity_fruits
        print(f"{final_price:.2f}")

    else:
        print("error")
else:
    print("error")




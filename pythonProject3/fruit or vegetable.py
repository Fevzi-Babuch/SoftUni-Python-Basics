# Да се напише програма, която чете име на продукт, въведено от потребителя, и проверява дали е плод или зеленчук.
# · Плодовете "fruit" имат следните възможни стойности: banana, apple, kiwi, cherry, lemon и grapes;
# · Зеленчуците "vegetable" имат следните възможни стойности: tomato, cucumber, pepper и carrot;
# · Всички останали са "unknown".
# Да се изведе "fruit", "vegetable" или "unknown" според въведения продукт

product_name = str(input())
fruit_list = ("banana", "apple", "kiwi", "cherry", "lemon", "grapes")
vegetable_list = ("tomato", "cucumber", "pepper", "carrot")
if product_name in fruit_list:
    print("fruit")
elif product_name in vegetable_list:
    print("vegetable")
else:
    print("unknown")



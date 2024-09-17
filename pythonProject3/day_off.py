# Напишете програма която, чете ден от седмицата (текст), на английски език - въведен от потребителя.Ако денят е работен
# отпечатва на конзолата - "Working day", ако е почивен - "Weekend". Ако се въведе текст различен от ден от седмицата
# да се отпечата - "Error".

working_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekend_days = ("Saturday", "Sunday")
day_input = str(input())
if day_input in working_days:
    print("Working day")
elif day_input in weekend_days:
    print("Weekend")
else:
    print("Error")

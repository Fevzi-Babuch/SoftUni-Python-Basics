# Напишете програма, която чете цяло число, въведено от потребителя, и отпечатва ден от седмицата (на английски език),
# в граници [1...7] или отпечатва "Error" в случай, че въведеното число е невалидно.

day_number = int(input())
if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Error")






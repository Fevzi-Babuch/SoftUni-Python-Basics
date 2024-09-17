# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст) - въведени от потребителя
# и проверява дали офисът на фирма е отворен, като работното време на офисът е от 10-18 часа,
# от понеделник до събота включително

time = int(input())
day = str(input())
working_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

if day in working_days:
    if time in range(10, 19):
        print("open")
    else: print("closed")
else:
    print("closed")




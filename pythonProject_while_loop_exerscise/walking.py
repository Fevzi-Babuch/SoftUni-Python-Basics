# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден.
# Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си.
# Напишете програма, която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня и когато
# постигне целта си да се изписва "Goal reached! Good job!" и колко стъпки повече е
# извървяла "{разликата между стъпките} steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките, които
# е извървяла докато се прибира. След което, ако не е успяла да постигне целта си, на конзолата
# трябва да се изпише: "{разликата между стъпките} more steps to reach goal."


STEPS_TO_RUN = 10000
COMMAND_TO_STOP = "Going home"

command = input()
steps_difference = 0
total_steps = 0
steps_over_the_goal = 0

while command != COMMAND_TO_STOP:
    number_of_steps = int(command)
    total_steps += number_of_steps
    if total_steps >= STEPS_TO_RUN:
        steps_over_the_goal = total_steps - STEPS_TO_RUN
        print("Goal reached! Good job!")
        print(f"{steps_over_the_goal} steps over the goal!")
        break
    command = input()
if command == COMMAND_TO_STOP:
    command = int(input())
    total_steps += command
    steps_over_the_goal = STEPS_TO_RUN - total_steps
    if total_steps < STEPS_TO_RUN:
        steps_difference = STEPS_TO_RUN - total_steps
        print(f"{steps_difference} more steps to reach goal.")
    else:
        print("Goal reached! Good job!")
        print(f"{abs(steps_over_the_goal)} steps over the goal!")













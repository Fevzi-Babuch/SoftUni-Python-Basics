# Студент трябва да отиде на изпит в определен час (например в 9:30 часа). Той идва в изпитната зала в даден час на
# пристигане (например 9:40). Счита се, че студентът е дошъл навреме, ако е пристигнал в часа на изпита или до половин
# час преди това. Ако е пристигнал по-рано повече от 30 минути, той е подранил. Ако е дошъл след часа на изпита,
# той е закъснял. Напишете програма, която прочита време на изпит и време на пристигане и отпечатва дали студентът е
# дошъл навреме, дали е подранил или е закъснял и с колко часа или минути е подранил или закъснял.
# От конзолата се четат 4 цели числа (по едно на ред), въведени от потребителя:
# · Първият ред съдържа час на изпита - цяло число от 0 до 23;
# · Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
# · Третият ред съдържа час на пристигане - цяло число от 0 до 23;
# · Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59

DEFINITION_OF_EARLY = 30
MINUTES_IN_HOUR = 60
exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

if exam_hours == arrival_hours and exam_minutes == arrival_minutes:
    print("On time")
    exit()
exam_total_minutes = exam_hours * 60 + exam_minutes
arrival_total_minutes = arrival_hours * 60 + arrival_minutes

if arrival_total_minutes > exam_total_minutes:
    print("Late")
    difference = arrival_total_minutes - exam_total_minutes
    if difference < MINUTES_IN_HOUR:
        print(f"{difference} minutes after the start")
    else:
        hours_after = difference // MINUTES_IN_HOUR
        minutes_after = difference % MINUTES_IN_HOUR
        if minutes_after < 10:
            minutes_after = "0" + str(minutes_after)
        print(f"{hours_after}:{minutes_after} hours after the start")
else:
    difference = exam_total_minutes - arrival_total_minutes
    if difference <= DEFINITION_OF_EARLY:
        print("On time")
    else:
        print("Early")
    if difference < MINUTES_IN_HOUR:
        print(f"{difference} minutes before the start")
    else:
        hours_before = difference // MINUTES_IN_HOUR
        minutes_before = difference % MINUTES_IN_HOUR
        if minutes_before < 10:
            minutes_before = "0" + str(minutes_before)
        print(f"{hours_before}:{minutes_before} hours before the start")




# exam_hours = int(input())
# exam_minutes = int(input())
# arrival_hours = int(input())
# arrival_minutes = int(input())
#
# exam_total_minutes = exam_hours * 60 + exam_minutes
# arrival_total_minutes = arrival_hours * 60 + arrival_minutes
# difference = exam_total_minutes - arrival_total_minutes
#
# if (exam_hours == arrival_hours) and (exam_minutes == arrival_minutes):
#     print("On time")
#     exit()
# if 30 >= difference >= 0:
#     print("On time")
#     print(f"{difference} minutes before the start")
# elif 30 < difference < 60:
#     print("Early")
#     print(f"{difference} minutes before the start")
# if difference >= 60:
#     print("Early")
#     hours_early = difference // 60
#     minutes_early = difference % 60
#     if minutes_early < 10:
#         minutes_early = "0" + f"{minutes_early}"
#     print(f"{hours_early}:{minutes_early} hours before the start")
# elif difference < 0:
#     print("Late")
#     if -60 < difference:
#         print(f"{abs(difference)} minutes after the start")
#     if -60 > difference:
#         hours_late = abs(difference) // 60
#         minutes_late = abs(difference) % 60
#         if minutes_late < 10:
#             minutes_late = "0" + f"{minutes_late}"
#         print(f"{hours_late}:{minutes_late:} hours after the start")






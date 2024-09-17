# 4. Train the Trainers
# Курсът "Train the trainers" е към края си и финалното оценяване наближава. Вашата задача е да помогнете на журито,
# което ще оценява презентациите, като напишете програма, в която да изчислява средната оценка от представянето на всяка
# една презентация от даден студент, а накрая - средния успех от всички тях.
# От конзолата на първият ред се прочита броят на хората в журито n - цяло число.
# След това на отделен ред се прочита името на презентацията – текст.
# За всяка една презентация на нов ред се четат n - на брой оценки - реално число.
# След изчисляване на средната оценка за конкретна презентация, на конзолата се печата:
# "{името на презентацията} - {средна оценка}."
# След получаване на команда "Finish", на конзолата се печата
# "Student's final assessment is {среден успех от всички презентации}." и програмата приключва.
# Всички оценки трябва да бъдат форматирани до втория знак след десетичната запетая

END_COMMAND = "Finish"


total_grades = 0
presentation_counter = 0

judges_number = int(input())
while True:
    presentation_name = input()
    if presentation_name != END_COMMAND:
        presentation_counter += 1
        sum_of_grades = 0
        average_grade = 0
        for i in range(judges_number):
            grade = float(input())
            sum_of_grades += grade
        average_grade = sum_of_grades / judges_number
        total_grades += average_grade
        print(f"{presentation_name} - {average_grade:.2f}.")
    else:
        break
total_average = total_grades / presentation_counter
print(f"Student's final assessment is {total_average:.2f}.")




















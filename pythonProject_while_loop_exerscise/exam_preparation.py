# Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си.
# При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при команда "Enough"
# или ако Марин получи определения брой незадоволителни оценки. Незадоволителна е всяка оценка, която е
# по-малка или равна на 4.
# Вход
# ⦁	На първи ред - брой незадоволителни оценки - цяло число;
# ⦁	След това многократно се четат по два реда:
# ⦁	Име на задача – текст;
# ⦁	Оценка - цяло число в интервала [2…6]
# Изход
# ⦁	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
# ⦁	"Average score: {средна оценка}"
# ⦁	"Number of problems: {броя на всички задачи}"
# ⦁	"Last problem: {името на последната задача}"
# ⦁	Ако получи определеният брой незадоволителни оценки:
# ⦁	"You need a break, {брой незадоволителни оценки} poor grades."
# Средната оценка да бъде форматирана до втория знак след десетичната запетая.

negative_grades_limit = int(input())
exam_name = input()
negative_grades = 0
problems_count = 0
total_score = 0
last_problem = ""
while exam_name != "Enough":
    grade = int(input())
    problems_count += 1
    total_score += grade
    last_problem = exam_name
    if grade <= 4:
        negative_grades += 1
        if negative_grades >= negative_grades_limit:
            print(f"You need a break, {negative_grades} poor grades.")
            break
    exam_name = input()
if exam_name == "Enough":
    average_score = total_score / problems_count
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {last_problem}")









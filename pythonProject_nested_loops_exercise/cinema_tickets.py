# 6. Билети за кино
# Вашата задача е да напишете програма, която да изчислява процента на билетите за всеки тип от продадените билети:
# студентски(student), стандартен(standard) и детски(kid), за всички прожекции. Трябва да изчислите и колко процента от
# залата е запълнена за всяка една прожекция.
# Вход
# Входът е поредица от цели числа и текст:
# · На първия ред до получаване на командата "Finish" - име на филма – текст
# · На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# · За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на командата "End":
# o Типа на закупения билет - текст ("student", "standard", "kid"

FINAL_STOP_STRING = "Finish"
MOVIE_STOP_STRING = "End"
STUDENT_TICKET = "student"
STANDARD_TICKET = "standard"
KIDS_TICKET = "kid"

student_tickets_sold = 0
standard_tickets_sold = 0
kids_tickets_sold = 0
total_cinema_tickets_sold = 0

while True:
    movie_name = input()
    if movie_name == FINAL_STOP_STRING:
        break
    available_tickets = int(input())
    sold_tickets = 0

    while sold_tickets < available_tickets:
        type_cinema_ticket = input()
        if type_cinema_ticket == MOVIE_STOP_STRING or type_cinema_ticket == FINAL_STOP_STRING:
            break
        total_cinema_tickets_sold += 1
        sold_tickets += 1
        if type_cinema_ticket == STUDENT_TICKET:
            student_tickets_sold += 1
        if type_cinema_ticket == STANDARD_TICKET:
            standard_tickets_sold += 1
        if type_cinema_ticket == KIDS_TICKET:
            kids_tickets_sold += 1
    print(f"{movie_name} - {(sold_tickets / available_tickets) * 100:.2f}% full.")
print(f"Total tickets: {total_cinema_tickets_sold}")
print(f"{(student_tickets_sold / total_cinema_tickets_sold) * 100:.2f}% student tickets.")
print(f"{(standard_tickets_sold / total_cinema_tickets_sold) * 100:.2f}% standard tickets.")
print(f"{(kids_tickets_sold / total_cinema_tickets_sold) * 100:.2f}% kids tickets.")






























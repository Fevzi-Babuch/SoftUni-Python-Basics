# За лятната ваканция в списъка със задължителна литература на Жоро има определен брой книги. Понеже Жоро предпочита
# да играе с приятели навън, вашата задача е да му помогнете да изчисли колко часа на ден трябва да отделя,
# за да прочете необходимата литература.


pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_hours_for_read = pages // pages_per_hour

days_for_read = total_hours_for_read // days

print(days_for_read)

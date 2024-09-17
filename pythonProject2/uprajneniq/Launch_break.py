# По време на обедната почивка искате да изгледате епизод от своя любим сериал. Вашата задача е да напишете програма,
# с която ще разберете дали имате достатъчно време да изгледате епизода. По време на почивката отделяте време за обяд и
# време за отдих. Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.
# Вход
# От конзолата се четат 3 реда:
# 1. Име на сериал – текст
# 2. Продължителност на епизод – цяло число в диапазона [10… 90]
# 3. Продължителност на почивката – цяло число в диапазона [10… 120]
import math

LAUNCH_TIME_PART = 1 / 8
REST_TIME_PART = 1 / 4
movie_name = str(input())
episode_time = int(input())
total_launch_break = int(input())

launch_time = total_launch_break * LAUNCH_TIME_PART
rest_time = total_launch_break * REST_TIME_PART
free_time_from_break = total_launch_break - launch_time - rest_time

if free_time_from_break >= episode_time:
    extra_time_left = math.ceil(free_time_from_break - episode_time)

    print(f"You have enough time to watch {movie_name} and left with {extra_time_left} minutes free time.")
else:
    necessary_time = math.ceil(episode_time - free_time_from_break)
    print(f"You don't have enough time to watch {movie_name}, you need {necessary_time} more minutes.")





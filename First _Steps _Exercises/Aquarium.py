# За рождения си ден Любомир получил аквариум с формата на паралелепипед. Първоначално прочитаме от конзолата на
# отделни редове размерите му – дължина, широчина и височина в сантиметри. Трябва да се пресметне колко литра вода ще
# събира аквариума, ако се знае, че определен процент от вместимостта му е заета от пясък, растения, нагревател и помпа.
# Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/.
# Да се напише програма, която изчислява литрите вода, която са необходими за напълването на аквариума.
# 1. Дължина в см – цяло число в интервала [10 … 500]
# 2. Широчина в см – цяло число в интервала [10 … 300]
# 3. Височина в см – цяло число в интервала [10… 200]
# 4. Процент – реално число в интервала [0.000 … 100.000]

# V=S.h   S = (2a + 2b) * c V = a*b*c

aquarium_len = int(input())
aquarium_wide = int(input())
aquarium_high = int(input())
percents_of_used_space = float(input())

aquarium_capacity_cm = aquarium_high * aquarium_wide * aquarium_len
aquarium_capacity_dm = aquarium_capacity_cm * 0.001

water_capacity = aquarium_capacity_dm - (aquarium_capacity_dm * percents_of_used_space / 100)
print(water_capacity)





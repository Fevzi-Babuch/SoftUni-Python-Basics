# 6. Сграда
# Напишете програма, която извежда на конзолата номерата на стаите в една сграда (в низходящ ред),
# като са изпълнени следните условия:
# · На всеки четен етаж има само офиси;
# · На всеки нечетен етаж има само апартаменти;
# · Всеки апартамент се означава по следния начин : А{номер на етажа}{номер на апартамента},
# номерата на апартаментите започват от 0;
# · Всеки офис се означава по следния начин : О{номер на етажа}{номер на офиса}, номерата на офисите също започват от 0;
# · На последният етаж винаги има апартаменти и те са по-големи от останалите,
# затова пред номера им пише 'L', вместо 'А'. Ако има само един етаж, то има само големи апартаменти!
# От конзолата се прочитат две цели числа - броят на етажите и броят на стаите за един етаж

TOP_FLOOR_ROOM = "L"
OFFICE_ROOM = "O"
APARTMENT_ROOM = "A"
floors = int(input())
rooms = int(input())
rooms_in_current_floor = ""
for floor in range(floors, 0 - 1, -1):
    print(rooms_in_current_floor)
    top_floor_rooms_counter = ""
    office_rooms_counter = ""
    apartment_rooms_counter = ""
    for room in range(0, rooms):
        if floor == floors:
            top_floor_rooms_counter += f"{TOP_FLOOR_ROOM}{floor}{room} "
            rooms_in_current_floor = top_floor_rooms_counter
        elif floor < floors:
            if floor % 2 == 0:
                office_rooms_counter += f"{OFFICE_ROOM}{floor}{room} "
                rooms_in_current_floor = office_rooms_counter
            else:
                apartment_rooms_counter += f"{APARTMENT_ROOM}{floor}{room} "
                rooms_in_current_floor = apartment_rooms_counter















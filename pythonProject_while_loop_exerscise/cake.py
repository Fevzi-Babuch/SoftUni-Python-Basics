# 6. Торта
# Поканени сте на 30-ти рожден ден, на който рожденикът черпи с огромна торта. Той обаче не знае колко парчета могат да
# си вземат гостите от нея. Вашата задача е да напишете програма, която изчислява броя на парчетата, които гостите са
# взели преди тя да свърши. Ще получите размерите на тортата (широчина и
# дължина – цели числа и след това на всеки ред, до получаване на командата "STOP" или докато не свърши тортата,
# броят на парчетата, които гостите вземат от нея. Всяко парче торта е с размер 1х1 см.
# Да се отпечата на конзолата един от следните редове:
# · "{брой парчета} pieces are left." - ако стигнете до STOP и не са свършили парчетата торта;
# · "No more cake left! You need {брой недостигащи парчета} pieces more."

ONE_PIECE_OF_CAKE = 1 * 1
cake_length = int(input())
cake_width = int(input())
cake_size = cake_length * cake_width
total_pieces_of_cake = cake_size // ONE_PIECE_OF_CAKE
cake_needed = 0
while total_pieces_of_cake > 0:
    pieces_of_cake_taken = input()
    if pieces_of_cake_taken != "STOP":
        pieces_of_cake_taken = int(pieces_of_cake_taken)
        total_pieces_of_cake -= pieces_of_cake_taken

        if total_pieces_of_cake <= 0:
            cake_needed = total_pieces_of_cake
            print(f"No more cake left! You need {abs(cake_needed)} pieces more.")

    else:
        print(f"{abs(total_pieces_of_cake)} pieces are left.")
        break














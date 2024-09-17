# Ани обича да пътува и иска тази година да посети няколко различни дестинации. Като си избере дестинация,
# ще прецени колко пари ще й трябват, за да отиде до там, и ще започне да спестява.
# Когато е спестила достатъчно, ще може да пътува.
# От конзолата всеки път ще се четат първо дестинацията и минималния бюджет (десетично число),
# който ще е нужен за пътуването.
# След това ще се четат няколко суми (десетични числа), които Ани спестява като работи и когато успее да събере
# достатъчно за пътуването, ще заминава, като на конзолата трябва да се изпише: "Going to {дестинацията}!"
# Когато е посетила всички дестинации, които иска, вместо дестинация ще въведе "End" и програмата ще приключи.

while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    saved_money = 0

    while saved_money < budget:
        incoming_money = float(input())
        saved_money += incoming_money

    print(f"Going to {destination}!")

# destination = input()
# minimum_budget = float(input())
# END_OF_DESTINATIONS = "End"
# saved_money = 0
# end_of_journey = False
# while destination != END_OF_DESTINATIONS:
#     if saved_money < minimum_budget:
#         incoming_amount = float(input())
#         saved_money += incoming_amount
#     elif saved_money >= minimum_budget:
#         end_of_journey = True
#         print(f"Going to {destination}!")
#         saved_money = 0
#         destination = input()
#         if destination == END_OF_DESTINATIONS:
#             break
#         else:
#             minimum_budget = float(input())



















# Да се напише програма която чете ден от седмицата (текст) – въведен от потребителя и принтира на конзолата цената
# на билет за кино според деня от седмицата:
day = str(input())
ticket_price = 0
if day == "Monday":
    ticket_price = 12
if day == "Tuesday":
    ticket_price = 12
if day == "Wednesday":
    ticket_price = 14
if day == "Thursday":
    ticket_price = 14
if day == "Friday":
    ticket_price = 12
if day == "Saturday":
    ticket_price = 16
if day == "Sunday":
    ticket_price = 16
print(ticket_price)
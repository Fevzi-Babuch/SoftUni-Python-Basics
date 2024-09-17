# Напишете програма, която първоначално прочита име и парола на потребителски профил. След това чете парола за вход.
# · при въвеждане на грешна парола: потребителя да се подкани да въведе нова парола.
# · при въвеждане на правилна парола: отпечатваме "Welcome {username}!"

new_username = input()
new_password = input()

password = input()
while password != new_password:
    password = input()
print(f"Welcome {new_username}!")






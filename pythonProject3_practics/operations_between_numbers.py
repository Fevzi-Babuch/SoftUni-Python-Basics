# Напишете програма, която чете две цели числа (N1 и N2) и оператор, с който да се извърши дадена математическа операция.
# Възможните операции са: Събиране(+), Изваждане(-), Умножение(*), Деление(/) и Модулно деление(%). При събиране,
# изваждане и умножение на конзолата трябва да се отпечатат резултата и дали той е четен или нечетен.
# При обикновеното деление - резултата. При модулното деление - остатъка. Трябва да се има предвид, че делителят
# може да е равен на 0 (нула), а на нула не се дели. В този случай трябва да се отпечата специално съобщениe.

SUM = "+"
REST = "-"
DIV = "/"
MULT = "*"
MOD = "%"

n1 = int(input())
n2 = int(input())
op = str(input())
result = 0
even_odd = ""
if op == SUM or op == REST or op == MULT:
    if op == SUM:
        result = n1 + n2
    elif op == REST:
        result = n1 - n2
    elif op == MULT:
        result = n1 * n2
    if (result % 2) == 0:
        even_odd = "even"
    if (result % 2) != 0:
        even_odd = "odd"
    print(f"{n1} {op} {n2} = {result} - {even_odd}")
if (op == DIV) or (op == MOD):
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    elif op == DIV:
        result = n1 / n2
        print(f"{n1} / {n2} = {result:.2f}")
    elif op == MOD:
        result = n1 % n2
        print(f"{n1} % {n2} = {result}")















    # print(f"{n1} {op} {n2} = {result} - {even/odd}")
# 1. Конвертор: от USD към BGN
# Напишете програма за конвертиране на щатски долари (USD) в български лева (BGN).
# Използвайте фиксиран курс между долар и лев: 1 USD = 1.79549 BGN.

# usd = float(input())
#
# course_usd_to_bgn = 1.79549
# bgn = course_usd_to_bgn * usd
# print(bgn)

# 2. Конвертор: от радиани в градуси Напишете програма, която чете ъгъл в радиани (десетично число)
# и го преобразува в градуси. Използвайте формулата: градус = радиан * 180 / π.
# Числото π в Python може да достъпите чрез модула math. За да ползвате функционалността му,
# първо трябва да включите констатата pi.

from math import pi
from math import radians

radians = float(input())
degrees = (radians * 180)/pi

print(degrees)


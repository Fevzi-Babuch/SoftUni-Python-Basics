NYLON_PRICE_PER_SQUARE_METER = 1.5
PAINT_PRICE_PER_LITER = 14.5
THINNER_PRICE_PER_LITER = 5

EXTRA_PAINT = 10/100
EXTRA_NYLON = 2
MONEY_FOR_BAGS = 0.40

LABOR_PRICE = 30/100

nylon_quantity = int(input())
paint_quantity = int(input())
thinner_quantity = int(input())
labor_hours = int(input())

nylon_cost = (nylon_quantity + EXTRA_NYLON) * NYLON_PRICE_PER_SQUARE_METER
paint_cost = (paint_quantity + (paint_quantity * EXTRA_PAINT)) * PAINT_PRICE_PER_LITER
thinner_cost = thinner_quantity * THINNER_PRICE_PER_LITER


total_materials_cost = nylon_cost + paint_cost + thinner_cost + MONEY_FOR_BAGS
labor_price_per_hour = total_materials_cost * LABOR_PRICE

total_labor_cost = labor_hours * labor_price_per_hour
reform_costs = total_materials_cost + total_labor_cost

print(reform_costs)




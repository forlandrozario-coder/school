import math
consumption_per_day = 2.5
number_of_people = 5
galon_to_liters = 19
aqua_price = 19.000
total_water_needed_per_week = consumption_per_day * number_of_people
total_galons_needed = math.ceil(total_water_needed_per_week / galon_to_liters)
total_cost = total_galons_needed * aqua_price
print(f"the total water needed per week is {total_water_needed_per_week:,} liters.")
print(f"you will need {total_galons_needed} gallons of water per week.")
print(f"the total cost for the water is (RP) {total_cost:,.3f} ")
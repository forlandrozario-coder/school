travel_distance = float(input("Enter the distance to be traveld (km) : "))
motorcycle_consumption = float(input("enter motorcycle fuel consumption (km) : "))
fuel_price = float(input("Enter the price of fuel per liter (RP) : "))
fuel_needed = travel_distance / motorcycle_consumption
total_cost = fuel_needed * fuel_price
print(f"total fuel needed : {fuel_needed:,} liters")
print(f"total fuel cost : RP {total_cost:,.3f}")
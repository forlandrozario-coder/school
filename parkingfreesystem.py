vehicle_type = input("Enter the type of vehicle (car, motorcycle, bus) : ")
hours_parked = float(input("Enter the number of hours parked : "))
if vehicle_type == "car":
    if hours_parked <= 1:
        parking_fee = 2.0
    else: parking_fee = 2.0 + (hours_parked - 1) * 1.0
elif vehicle_type == "motorcycle":
    if hours_parked <= 1:
            parking_fee = 1.0
    else: parking_fee = 1.0 + (hours_parked - 1) * 0.5
elif vehicle_type == "bus":
    if hours_parked <= 1:
                parking_fee = 3.0
    else: parking_fee = 3.0 + (hours_parked - 1) * 2.0
print(f"The parking fee for the {vehicle_type} is : ${parking_fee:.2f}")


hours = int(input("Enter the number of hours worked: "))
minutes = int(input("Enter the number of minutes worked: "))
pay_rate = float(input("Enter hourly pay rate (RP): "))
total_hours_decimal = hours + (minutes / 60)
total_pay = total_hours_decimal * pay_rate
print(f"total payment is : RP {total_pay:,.2f}")
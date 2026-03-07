laptop_price = float(input("Enter laptop price (RP): "))
monthly_savings = float(input("Enter your savings per month (RP): "))
import math
months_needed = math.ceil(laptop_price / monthly_savings)
print(f"you will need {months_needed:,.2f} months to save enough money to buy the laptop. ")
salary = float(input("Enter the employees salary : "))
years = int(input("Enter the number of years the employee has worked : "))
if years >= 10:
    bonus = 0.25
elif years >= 5 and years <= 9:
    bonus = 0.15
elif years >= 1 and years <= 4:
    bonus = 0.05
else: bonus = 0
bonus_amount = salary * bonus
print(f"The employees bonus amount is : {bonus_amount:,}")
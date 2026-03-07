bill_amount = float(input("Enter the bill amount: "))
num_people = int(input("Enter number of people: "))
tax = 0.10
total_after_tax = bill_amount * (1 + tax)
per_person = total_after_tax / num_people
print(f"total after tax : RP {total_after_tax:,.2f}")
print(f"each person pays : RP {per_person:,.2f}")
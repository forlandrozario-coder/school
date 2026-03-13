kwh_usage = float(input("Enter the amount of kwh used : "))
if kwh_usage <= 100:
    bill_amount = 0.10
elif kwh_usage <= 300:
    bill_amount = 0.15
else: 
    kwh_usage > 300
    bill_amount = 0.20
    
total_bill = kwh_usage * bill_amount
print(f"The total bill amount is : {total_bill:,}")
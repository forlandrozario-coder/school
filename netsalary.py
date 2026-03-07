base_salary = 5000000
allowance = 750000
bpjs_rate = 0.02
tax_rate = 0.05
total_salary = base_salary + allowance
bpjs_deduction = total_salary * bpjs_rate
tax_deduction = total_salary * tax_rate
net_salary = total_salary - bpjs_deduction - tax_deduction
print(f"net salary : (RP {net_salary:,})")
salary = int(input("The employees salary : "))
credit_score = int(input("The employees credit score : "))
duration = int(input("The number of years the employee has worked : "))
if salary >= 3000 and credit_score >= 650 and duration >= 2:
    print("The employee is eligibile for the loan.")
elif salary >= 3000 and credit_score >= 650 and duration < 2 or salary >= 3000 and credit_score < 650 and duration >= 2 or salary < 3000 and credit_score >= 650 and duration >= 2:
    print("The employee is eligibile for a loan with conditional approval.")
elif salary >= 3000 and credit_score < 650 and duration < 2 or salary < 3000 and credit_score >= 650 and duration < 2 or salary < 3000 and credit_score < 650 and duration >= 2:
    print("The employee is not eligibile for the loan.")
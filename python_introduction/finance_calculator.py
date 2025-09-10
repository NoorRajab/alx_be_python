monthly_income = int(input("Enter your monthly income:"))
total_monthly_expense = int(input("Enter your total monthly expenses:"))
monthly_savings = monthly_income - total_monthly_expense
yearly_savings_without_interest = monthly_savings * 12
yearly_interest = monthly_savings * 12 * 0.05
projected_savings_annual = int(yearly_savings_without_interest + yearly_interest)
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings_annual}")
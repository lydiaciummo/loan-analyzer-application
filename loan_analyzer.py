# coding: utf-8
import csv
from pathlib import Path

#here is a list of loans
loan_costs = [500, 600, 200, 1000, 450]

#calculate the number of loans in the loan_costs list and save that to the variable number_of_loans
number_of_loans = len(loan_costs)
print(f"The number of loans is: {number_of_loans}")

# calculate the total of the loans in the list and save that to the variable total_loan_amount
total_loan_amount = sum(loan_costs)
print(f"The total of all of the loans is: {total_loan_amount}")

#calculate the average loan amount from the list and save that to the variable average_loan_price
average_loan_price = total_loan_amount / number_of_loans
print(f"The average price of the loans is: {average_loan_price}")

#a dictionary containing information about a loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#extract information about the loan from the dictionary and assign those values to variables
future_value = loan.get("future_value")
print(f"The future value of the loan is: {future_value}")
remaining_months = loan.get("remaining_months")
print(f"There are {remaining_months} months remaining on the loan")
loan_price = loan.get("loan_price")
print(f"The current price of the loan is: {loan_price}")
annual_discount_rate = .20

#calculate the fair value of the loan using the Present Value formula and assign that to the variable fair_value
fair_value = future_value / (1 + annual_discount_rate / 12) ** remaining_months
print(f"The fair value of the loan is: {fair_value}")

#use a conditional statement to determine if the loan is worth the cost to buy it
if fair_value >= loan_price:
    print("The loan is at worth at least the cost to buy it")
else: 
    print("The loan is too expensive. It is not worth the price.")


# a dictionary containing information about a new loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#a function that can be used to calculate the present value of a loan
def calculate_present_value(future_value, annual_discount_rate, remaining_months):
    present_value = future_value / (1 + annual_discount_rate / 12) ** remaining_months
    return present_value

#calculating the present value of new_loan using the calculate_present_value function
annual_discount_rate = .20
present_value = calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate)
print(f"The present value of the new loan is: {present_value}")


loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

#this empty list is where loan data will be stored
inexpensive_loans = []

#a loop that will determine which loans are prices at under $500 and add those loans to the inexpensive_loans list
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

#now we can see which loans were added to the list
print(f"The inexpensive loans are: {inexpensive_loans}")


# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

#write the data from the inexpensive_loans list to a CSV file
with open(output_path, 'w', newline= '') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())

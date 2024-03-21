import math

# Display menu options for the user
print("Menu:")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# Prompt the user to make a choice between investment and bond calculations
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Check the user's choice and execute the corresponding calculation
if user_choice == "investment":
    # Get necessary inputs for investment calculation
    # User inputs the deposit amount, interest rate, number of years, and interest type
    deposit_amount = float(input("Enter the amount of money that you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    years = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    # Calculate the total amount based on the type of interest
    if interest_type == "simple":
        total_amount = deposit_amount * (1 + interest_rate * years)
    elif interest_type == "compound":
        total_amount = deposit_amount * math.pow((1 + interest_rate), years)
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        exit()

    # Display the result of the investment calculation
    print(f"Total amount after {years} years: {total_amount:.2f}")

elif user_choice == "bond":
    # Get necessary inputs for bond repayment calculation
    # User inputs the present value of the house, annual interest rate, and repayment period in months
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the annual interest rate: ")) / 100
    months = int(input("Enter the number of months to repay the bond: "))

    # Convert annual interest rate to monthly and calculate monthly bond repayment
    monthly_interest_rate = interest_rate / 12
    bond_repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))

    # Display the monthly bond repayment amount
    print(f"Monthly bond repayment: {bond_repayment:.2f}")

else:
    # Inform the user if they made an invalid choice
    print("Invalid choice. Please enter 'investment' or 'bond'.")


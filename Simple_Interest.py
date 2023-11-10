# Input principal amount and number of years from the user
principal = int(input("Enter the Principal Amount: "))
years = int(input("Enter the Number of Years: "))

# Check the number of years to determine the interest rate
if years > 12:
    interest_rate = 10
    si = (principal * interest_rate * years) / 100
    print("The Interest Rate is:", interest_rate)
    print("The Simple Interest is:", si)
else:
    interest_rate = 15
    si = (principal * interest_rate * years) / 100
    print("The Interest Rate is:", interest_rate)
    print("The Simple Interest is:", si)

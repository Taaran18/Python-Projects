# Get user input for the principal amount, interest rate, and number of years
P = int(input("Enter the Principal Amount: "))
R = float(input("Enter the Interest rate: "))
n = int(input("Enter the no. of Years: "))

# Continue the loop as long as the principal is greater than or equal to 1000 and the number of years is less than or equal to 15
while P >= 1000 and n <= 15:
    # Calculate compound interest using the formula
    ci = P * (1 + (R / 100)) ** n

    # Print the calculated compound interest
    print("The Compound Interest is:", ci)

    # Print the additional money earned (compound interest minus the principal)
    print("Additional Money:", ci - P)

    # Get user input for the next iteration of principal, interest rate, and years
    P = int(input("Enter the Principal Amount: "))
    R = float(input("Enter the Interest rate: "))
    n = int(input("Enter the no. of Years: "))

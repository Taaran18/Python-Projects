while True:
    # Input principal amount, interest rate, and number of years from the user
    p = int(input("Enter the Principal Amount: "))
    r = float(input("Enter the Interest Rate: "))
    t = float(input("Enter the Number of Years: "))

    # Check the conditions to continue the loop
    if p >= 5000 and t <= 20:
        # Print the input values
        print("Your Principal Amount, Interest rate, and Number of years are:", p, r, t)

        # Calculate and print simple interest
        si = (p * r * t) / 100
        print("Simple Interest is:", si)

        # Calculate and print compound interest
        ci = p * (1 + r / 100) ** t
        print("Compound Interest is:", ci)

        print()
    else:
        # Break the loop if conditions are not met
        break

principal = int(input("Enter the Principal Amount :"))
years = int(input("Enter the no. of Years :"))

if years > 12:
    interest_rate = 10
    si1 = (principal * interest_rate * years) / 100

    print("The Interest Rate is :", interest_rate)
    print("The Simple Interest is :", si1)

else:
    interest_rate = 15
    si2 = (principal * interest_rate * years) / 100

    print("The Interest Rate is :", interest_rate)
    print("The Simple Interest is :", si2)

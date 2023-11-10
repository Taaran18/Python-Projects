P = int(input("Enter the Principal Amount :"))
R = float(input("Enter the Interest rate :"))
n = int(input("Enter the no. of Years :"))
while P >= 1000 and n <= 15:
    ci = P * (1 + (R / 100)) ** n

    print("The Compound Interest is :", ci)
    print("Additional Money :", ci - P)

    P = int(input("Enter the Principal Amount :"))
    R = int(input("Enter the Interest rate :"))
    n = int(input("Enter the no. of Years :"))

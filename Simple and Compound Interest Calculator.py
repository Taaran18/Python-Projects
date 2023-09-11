p = int(input("Enter the Principal Amount -"))
r = float(input("Ente rthe Interest rate -"))
t = float(input("Enter the Number of years -"))

while p >= 5000 and t <= 20:
    print("Your Principal Amount, Interest rate and Number of years are -", p, r, t)

    si = (p * r * t) / 100
    print("Simple Interest is -", si)

    ci = p * (1 + r / 100) ** t
    print("Compound Interest is -", ci)

    print()
    p = int(input("Enter the Principal Amount -"))
    r = float(input("Ente the Interest rate -"))
    t = float(input("Enter the Number of years -"))

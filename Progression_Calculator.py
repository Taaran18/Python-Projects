print("1. A.P. of nth Terms.")
print("2. Sum of A.P. of nth Terms.")
print("3. G.P. of nth Terms.")
print("4. Sum of G.P. of nth Terms.")
print("5. Exit")
choice = int(input("Enter the choice :"))

while 0 < choice < 5:
    if choice == 1:
        a = int(input("Enter the First Term :"))
        d = int(input("Enter the Common Difference :"))
        n = int(input("Enter the nth Term :"))
        an = a + (n - 1) * d
        print("First Term =", a, "Common Difference =", d, "Nth Term", n)
        print("nth Terms of an A.P.s are", an)

    if choice == 2:
        a = int(input("Enter the First Term :"))
        d = int(input("Enter the Common Difference :"))
        n = int(input("Enter the nth Term :"))
        sn = n / 2 * (2 * a + (n - 1) * d)
        print("First Term =", a, "Common Difference =", d, "Nth Term", n, end="")
        print("Sum of nth Terms of an A.P.s are", sn)

    if choice == 3:
        a = int(input("Enter the First Term :"))
        r = int(input("Enter the Common Ratio :"))
        n = int(input("Enter the nth Term :"))
        an = a * r ** (n - 1)
        print("First Term =", a, "Common Ratio =", d, "Nth Term", n)
        print("nth Terms of an G.P.s are", an)

    if choice == 4:
        a = int(input("Enter the First Term :"))
        r = int(input("Enter the Common Ratio :"))
        n = int(input("Enter the nth Term :"))
        sn = (a * (r ** n - 1) / (r - 1))
        print("First Term =", a, "Common Ratio =", d, "Nth Term", n)
        print("Sum of nth Terms of an G.P.s are", sn)

    else:
        print()
        print("1. A.P. of nth Terms.")
        print("2. Sum of A.P. of nth Terms.")
        print("3. G.P. of nth Terms.")
        print("4. Sum of G.P. of nth Terms.")
        print("5. Exit")
        choice = int(input("Enter the choice :"))

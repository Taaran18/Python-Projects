# Display menu options
print("1. A.P. of nth Terms.")
print("2. Sum of A.P. of nth Terms.")
print("3. G.P. of nth Terms.")
print("4. Sum of G.P. of nth Terms.")
print("5. Exit")

# Get user choice
choice = int(input("Enter the choice: "))

# Menu loop
while 1 <= choice <= 4:
    # Get user input for common parameters
    a = int(input("Enter the First Term: "))
    n = int(input("Enter the nth Term: "))

    # Check the user's choice
    if choice == 1:
        d = int(input("Enter the Common Difference: "))
        an = a + (n - 1) * d
        print(f"nth Term of an A.P. is {an}")

    elif choice == 2:
        d = int(input("Enter the Common Difference: "))
        sn = n / 2 * (2 * a + (n - 1) * d)
        print(f"Sum of nth Terms of an A.P. is {sn}")

    elif choice == 3:
        r = int(input("Enter the Common Ratio: "))
        an = a * r ** (n - 1)
        print(f"nth Term of a G.P. is {an}")

    elif choice == 4:
        r = int(input("Enter the Common Ratio: "))
        sn = (a * (r ** n - 1) / (r - 1))
        print(f"Sum of nth Terms of a G.P. is {sn}")

    # Display menu options again
    print("\n1. A.P. of nth Terms.")
    print("2. Sum of A.P. of nth Terms.")
    print("3. G.P. of nth Terms.")
    print("4. Sum of G.P. of nth Terms.")
    print("5. Exit")

    # Get user choice for the next iteration
    choice = int(input("Enter the choice: "))

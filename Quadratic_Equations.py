import math

# Display a message for the quadratic equation
print("For Quadratic equation, ax**2 + bx + c = 0, enter the coefficients below")

# Get user input for coefficients a, b, and c
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Check if a is zero
if a == 0:
    print("Value of 'a' should not be zero")
    print("Aborting!!!!!!!!")
else:
    # Calculate the discriminant (delta) for the quadratic equation
    delta = b**2 - 4 * a * c

    # Check the value of delta to determine the nature of roots
    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Roots are REAL and UNEQUAL")
        print("Root1 =", root1, "Root2 =", root2)

    elif delta == 0:
        root1 = -b / (2 * a)
        print("Roots are REAL and EQUAL")
        print("Root 1 =", root1, "Root 2 =", root1)

    else:
        print("Roots are COMPLEX and IMAGINARY")

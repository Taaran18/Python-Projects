import math

# Display menu options
print("Enter the Choice below:")
print("1. Area of Rectangle.")
print("2. Area of Square.")
print("3. Area of Triangle.")
print("4. Area of Circle.")
print("5. Exit")

# Get user choice
choice = int(input("Enter the choice:"))

# Continue the loop until the user chooses to exit (option 5)
while choice != 5 or choice > 0:
    if choice == 1:
        # Calculate area of rectangle
        length = int(input("Enter the length of Rectangle:"))
        width = int(input("Enter the width of Rectangle:"))

        area1 = length * width

        print("The area of Rectangle is:", area1)

    elif choice == 2:
        # Calculate area of square
        side = int(input("Enter the side of Square:"))

        area2 = side**2

        print("The area of Square is:", area2)

    elif choice == 3:
        # Calculate area of triangle
        base = int(input("Enter the length of Triangle:"))
        height = int(input("Enter the width of Triangle:"))

        area3 = 1 / 2 * base * height

        print("The area of Triangle is:", area3)

    elif choice == 4:
        # Calculate area of circle
        radius = int(input("Enter the radius of Circle:"))

        area4 = math.pi * radius**2

        print("The area of Circle is:", area4)

    elif choice == 5:
        # Exit the loop if the user chooses option 5
        break

    else:
        # Invalid input, prompt the user again
        print("Invalid input")

    # Display menu options again
    print()
    print("Enter the Choice below:")
    print("1. Area of Rectangle.")
    print("2. Area of Square.")
    print("3. Area of Triangle.")
    print("4. Area of Circle.")
    print("5. Exit")

    # Get user choice for the next iteration
    choice = int(input("Enter the choice:"))
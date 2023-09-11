import math

print("Enter the Choice below :")
print("1. Area of Rectangle.")
print("2. Area of Square.")
print("3. Area of Triangle.")
print("4. Area of Circle..")
print("5. Exit")

choice = int(input("Enter the choice :"))

while choice != 5 or choice > 0:

    if choice == 1:
        lenght = int(input("Enter the lenght of Rectangle :"))
        width = int(input("Enter the width of Rectangle :"))

        area1 = lenght * width

        print("The area of Rectangle is :", area1)

    elif choice == 2:
        side = int(input("Enter the side of Square :"))

        area2 = side ** 2

        print("The area of Aquare is :", area2)

    elif choice == 3:
        base = int(input("Enter the lenght of Triangle :"))
        height = int(input("Enter the width of Triangle :"))

        area3 = 1 / 2 * base * height

        print("The area of Triangle is :", area3)

    elif choice == 4:
        radius = int(input("Enter the radius of Circle :"))

        area4 = math.pi * radius ** 2

        print("The area of Circle is :", area4)

    elif choice == 5:
        break

    else:
        print("invalid input")

        print()
        print("Enter the Choice below :")
        print("1. Area of Rectangle.")
        print("2. Area of Square.")
        print("3. Area of Triangle.")
        print("4. Area of Circle..")
        print("5. Exit")
        choice = int(input("Enter the choice :"))

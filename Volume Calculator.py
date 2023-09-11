import math

print("Enter the choice below :")

print("1. Caluculate Volume of Cube.")
print("2. Caluculate Volume of Cuboid.")
print("3. Caluculate Volume of Cylinder.")
print("4. Caluculate Volume of Cone.")
print("5. Caluculate Volume of Sphere.")
print("6. Caluculate Volume of Hemisphere.")
print("7. Caluculate Volume of Frustum.")
print("8. Exit.")
choice = int(input("Enter your choice :"))

while choice != 8 or choice > 0:
    if choice == 1:
        length = float(input("Enter the lenght of the Cuboid :"))
        width = float(input("Enter the width of the Cuboid :"))
        height = float(input("Enter the height of the Cuboid :"))

        volume1 = length * width * height

        print("The length, width and height are :", length, width, height)
        print("The Volume of the Cuboid is :", volume1)
    elif choice == 2:
        side = float(input("Enter the side of the Cube :"))

        volume2 = side ** 3

        print("The side is :", side)
        print("The volume is :", volume2)

    elif choice == 3:
        radius = float(input("Enter the raduis of the Cylinder :"))
        height = float(input("Enter the height of the Cylinder :"))

        volume3 = math.pi * radius ** 2 * height

        print("The radius and height are :", radius, height)
        print("The Volume of Cylinder is :", volume3)
    elif choice == 4:
        radius = float(input("Enter the raduis of the Cone :"))
        height = float(input("Enter the height of the Cone :"))

        volume4 = (math.pi * radius ** 2 * height) / 3

        print("The radius and height are :", radius, height)
        print("The Volume of Cone is :", volume4)

    elif choice == 5:
        radius = float(input("Enter the raduis of the Sphere :"))

        volume5 = 4 / 3 * (math.pi * radius ** 3)

        print("The radius is :", radius)
        print("The Volume of Sphere is :", volume5)

    elif choice == 6:
        radius = float(input("Enter the raduis of the hemisphere :"))

        volume6 = 2 / 3 * (math.pi * radius ** 3)

        print("The radius is :", radius)
        print("The Volume of Hemisphere is :", volume6)

    elif choice == 7:
        radius1 = float(input("Enter the 1st raduis of the Frustum :"))
        radius2 = float(input("Enter the 2nd raduis of the Frustum :"))
        height = float(input("Enter the height of the Frustum :"))

        volume7 = (math.pi / 3) * height * (radius1 ** 2 * radius2 ** 2 * radius1 * radius2)

        print("The 1st raduis, 2nd raduis and Height are : ", radius1, radius2, height)
        print("The volume of Frustum is :", volume7)

    elif choice == 8:
        break

    else:
        print("invalid input")
    print()
    print("Enter the choice below :")
    print("1. Caluculate Volume of Cube.")
    print("2. Caluculate Volume of Cuboid.")
    print("3. Caluculate Volume of Cylinder.")
    print("4. Caluculate Volume of Cone.")
    print("5. Caluculate Volume of Sphere.")
    print("6. Caluculate Volume of Hemisphere.")
    print("7. Caluculate Volume of Frustum.")
    print("8. Exit.")
    choice = int(input("Enter your choice :"))

import math


# Function to calculate the volume of a cube
def calculate_cube_volume():
    side = float(input("Enter the side of the Cube: "))
    volume = side**3
    print("The side is:", side)
    print("The volume is:", volume)


# Function to calculate the volume of a cuboid
def calculate_cuboid_volume():
    length = float(input("Enter the length of the Cuboid: "))
    width = float(input("Enter the width of the Cuboid: "))
    height = float(input("Enter the height of the Cuboid: "))
    volume = length * width * height
    print("The length, width, and height are:", length, width, height)
    print("The volume of the Cuboid is:", volume)


# Function to calculate the volume of a cylinder
def calculate_cylinder_volume():
    radius = float(input("Enter the radius of the Cylinder: "))
    height = float(input("Enter the height of the Cylinder: "))
    volume = math.pi * radius**2 * height
    print("The radius and height are:", radius, height)
    print("The volume of the Cylinder is:", volume)


# Function to calculate the volume of a cone
def calculate_cone_volume():
    radius = float(input("Enter the radius of the Cone: "))
    height = float(input("Enter the height of the Cone: "))
    volume = (math.pi * radius**2 * height) / 3
    print("The radius and height are:", radius, height)
    print("The volume of the Cone is:", volume)


# Function to calculate the volume of a sphere
def calculate_sphere_volume():
    radius = float(input("Enter the radius of the Sphere: "))
    volume = 4 / 3 * (math.pi * radius**3)
    print("The radius is:", radius)
    print("The volume of the Sphere is:", volume)


# Function to calculate the volume of a hemisphere
def calculate_hemisphere_volume():
    radius = float(input("Enter the radius of the Hemisphere: "))
    volume = 2 / 3 * (math.pi * radius**3)
    print("The radius is:", radius)
    print("The volume of the Hemisphere is:", volume)


# Function to calculate the volume of a frustum
def calculate_frustum_volume():
    radius1 = float(input("Enter the 1st radius of the Frustum: "))
    radius2 = float(input("Enter the 2nd radius of the Frustum: "))
    height = float(input("Enter the height of the Frustum: "))
    volume = (math.pi / 3) * height * (radius1**2 + radius2**2 + radius1 * radius2)
    print("The 1st radius, 2nd radius, and height are:", radius1, radius2, height)
    print("The volume of the Frustum is:", volume)


# Main program
while True:
    print("\nEnter the choice below:")
    print("1. Calculate Volume of Cube.")
    print("2. Calculate Volume of Cuboid.")
    print("3. Calculate Volume of Cylinder.")
    print("4. Calculate Volume of Cone.")
    print("5. Calculate Volume of Sphere.")
    print("6. Calculate Volume of Hemisphere.")
    print("7. Calculate Volume of Frustum.")
    print("8. Exit.")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        calculate_cube_volume()
    elif choice == 2:
        calculate_cuboid_volume()
    elif choice == 3:
        calculate_cylinder_volume()
    elif choice == 4:
        calculate_cone_volume()
    elif choice == 5:
        calculate_sphere_volume()
    elif choice == 6:
        calculate_hemisphere_volume()
    elif choice == 7:
        calculate_frustum_volume()
    elif choice == 8:
        break
    else:
        print("Invalid input. Please enter a number between 1 and 8.")

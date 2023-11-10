# Get user input for the number of the month
month = int(input("Enter the number of month: "))

# Define a list of month names
month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# Check if the entered month number is valid
if 1 <= month <= 12:
    print(
        "It's", month_names[month - 1]
    )  # Subtract 1 to access the correct index in the list
else:
    print("Invalid month number")

# Input days from the user and convert it to seconds
days = int(input("Input days:")) * 3600 * 24

# Input hours from the user and convert it to seconds
hours = int(input("Input hours:")) * 3600

# Input minutes from the user and convert it to seconds
minutes = int(input("Input minutes:")) * 60

# Input seconds from the user
seconds = int(input("Input seconds:"))

# Calculate the total time in seconds
time = days + hours + minutes + seconds

# Print the total time in seconds
print("The amount of seconds:", time)

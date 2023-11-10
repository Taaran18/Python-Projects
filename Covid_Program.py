# Import necessary libraries
import covid
import matplotlib.pyplot as plt

# Create a Covid object
cov = covid.Covid()

# Get user input for the country name
name = input("Enter the country name =")

# Get COVID-19 data for the specified country
virusdata = cov.get_status_by_country_name(name)

# Extract the number of active cases, recovered cases, and deaths
active = virusdata["active"]
recover = virusdata["recovered"]
deaths = virusdata["deaths"]

# Plot a pie chart
plt.pie(
    [active, recover, deaths],
    labels=["Active", "Recovered", "Deaths"],
    colors=["blue", "green", "red"],
    explode=(0, 0, 0.2),
    startangle=180,
    autopct="%1.1f%%",
    shadow=True,
)

# Set the title of the pie chart to the country name
plt.title(name)

# Add a legend to the pie chart
plt.legend()

# Display the pie chart
plt.show()

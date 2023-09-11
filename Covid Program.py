import covid
import matplotlib.pyplot as plt

cov = covid.Covid()
name = input("Enter the country name =")
virusdata = cov.get_status_by_country_name(name)
active = virusdata['active']
recover = virusdata['recovered']
deaths = virusdata['deaths']
plt.pie([active, recover, deaths], labels=['active', 'recovered', 'deaths'], colors=['b', 'g', 'r'],
        explode=(0, 0, 0.2), startangle=180, autopct='%1.1f%%', shadow=True)
plt.title(name)
plt.legend()
plt.show()

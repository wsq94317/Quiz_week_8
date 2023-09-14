import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./climate.csv')

years = [y for y in df["Year"]]
co2 = [c for c in df["CO2"]]
temp = [t for t in df["Temperature"]]

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 


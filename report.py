import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

df.plot(kind='line')
plt.title("Health & Hygiene Trends")
plt.xlabel("Days")
plt.ylabel("Values")
plt.show()

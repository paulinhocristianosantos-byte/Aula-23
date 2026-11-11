import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

df = pd.read_csv(r"C:\Users\paulo.cristiano\Downloads\funcionarios.csv")

df_lucro = df[df["lucro"] > 0]

xpoints = df_lucro["nome"]
ypoints = df_lucro["lucro"]

bars = plt.barh(xpoints, ypoints)
plt.bar_label(bars, fmt="%.2f", padding=3)


plt.barh(xpoints, ypoints)

plt.title("Grafico")
plt.xlabel("Plano X")
plt.xlabel("Plano Y")

plt.show()

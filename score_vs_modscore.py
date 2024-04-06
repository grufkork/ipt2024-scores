from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

repscore = []
oppscore = []




d = pd.read_csv("scores.csv")

for c in d["country"].unique():
    repscore.append(d.loc[(d['country'] == c) & (d["role"] == "Rep"), "score"].mean())
    oppscore.append(d.loc[(d['country'] == c) & (d["role"] == "Opp"), "score"].mean())




fig1, ax = plt.subplots()
ax.grid()
plt.title("Oppscore vs Repscore (per team)")
ax.scatter(repscore, oppscore)
ax.set_xlabel("Average reporter score")
ax.set_ylabel("Average opponent score")
ax.set_xlim(0, 10)

ax.set_ylim(0, 10)
ax.set_box_aspect(1)
plt.show()

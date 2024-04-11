import numpy as np
import pandas as pd

df = pd.read_csv("data/2024.csv", index_col=0)
print(df)


a = []

for i,row in df.iterrows():
    n = int(row.loc["fightName"][0])
    a.append(n)

df.insert(3, "fight", a, True)
df = df[["juror", "country", "fight", "role", "score", "participant", "problem", "round", "fightName", "fightID"]]
df.to_csv("data/2024.csv")

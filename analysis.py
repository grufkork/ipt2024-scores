# Participant Name, Country, PF, Jury, Grade, Type of Grade


# For each PF
# calculate average and stdev


# See if average grade increases with time




import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import datetime

data = pd.read_csv('scores.csv')#, index_col='AsOfDate', parse_dates=['AsOfDate'])
print(data)
dfs=[]
df = data
for i in df["fightName"].unique():
    print(i)
    df_i = df.loc[df["fightName"]==i]
    #print(df_i)
    dfs.append(df_i.copy())

print("Analysis starts now ...")

# juror	country	fight	role	score	participant	problem	round	fightName

round_1_score = 0
round_2_score = 0
round_3_score = 0

def calc_grade_for_fight(fight, col, val_array):
    for index, i in fight.iterrows():
        for i in val_array:

        fight[]


for fight in dfs:
    #print(fight)

    # Does later fights perform better?
    for index, i in fight.iterrows():#fight.loc[df["round"]==1]:
        
        if i["round"] == 1:
                 
        elif i["round"] == 2:
        
        print(i["round"])

        #df_i = df.loc[df["fightName"]==i]




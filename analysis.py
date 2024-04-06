# Participant Name, Country, PF, Jury, Grade, Type of Grade


# For each PF
# calculate average and stdev


# See if average grade increases with time




import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import datetime

#data = pd.read_csv('reduced_scores.csv')#, index_col='AsOfDate', parse_dates=['AsOfDate'])
data = pd.read_csv('scores.csv')#, index_col='AsOfDate', parse_dates=['AsOfDate'])


dfs=[]
df = data
for i in df["fightName"].unique():
    df_i = df.loc[df["fightName"]==i]
    dfs.append(df_i.copy())

print("Analysis starts now ...")

# juror	country	fight	role	score	participant	problem	round	fightName

round_scores = np.array([0,0,0])

def calc_stats_for_fight(fight, col, val_array,average):
    ret_arr = [0 for x in val_array]
    num_entries =  [0 for x in val_array]

    for index, f in fight.iterrows():
        for i in range(len(val_array)):
            val = val_array[i]
            if f[col] == val:
                ret_arr[i] += f["score"]
                num_entries[i] += 1

    if average:
        for i in range(len(val_array)):
            ret_arr[i] = ret_arr[i] / num_entries[i]
    
    return ret_arr

for fight in dfs:
    round_scores = round_scores + np.array(calc_stats_for_fight(fight, "round", [1,2,3], average=True))/len(dfs)

print(round_scores)
    
'''
    # Does later fights perform better?
    #for index, i in fight.iterrows():#fight.loc[df["round"]==1]:
        
        
        if i["round"] == 1:
                 
        elif i["round"] == 2:
        
        print(i["round"])
        
        #df_i = df.loc[df["fightName"]==i]


'''

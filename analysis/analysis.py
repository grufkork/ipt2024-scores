# Participant Name, Country, PF, Jury, Grade, Type of Grade


# For each PF
# calculate average and stdev


# See if average grade increases with time




import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import datetime

plt.rcParams.update({"font.size": 36})
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["font.family"] = "STIXGeneral"
plt.rcParams["figure.figsize"] = (3.2, 2.4)
plt.rcParams["savefig.bbox"] = "tight"
plt.interactive(True)



#data = pd.read_csv('reduced_scores.csv')#, index_col='AsOfDate', parse_dates=['AsOfDate'])
data = pd.read_csv('scores.csv')#, index_col='AsOfDate', parse_dates=['AsOfDate'])


dfs=[]
df = data
for i in df["fightName"].unique():
    df_i = df.loc[df["fightName"]==i]
    dfs.append(df_i.copy())

print("Analysis starts now ...")

# juror	country	fight	role	score	participant	problem	round	fightName

def get_non_zero(data_arr, column):
    temp = data_arr[:,column]
    return temp[temp != 0]

def calc_stats_for_fight(fight, col, val_array,average):
    ret_arr = np.empty(shape = [0,3])
    num_entries =  [0 for x in val_array]

    for index, f in fight.iterrows():
        for i in range(len(val_array)):
            val = val_array[i]
            if f[col] == val:
                temp_val = [0,0,0]
                temp_val[i] = f["score"]
                num_entries[i] += 1
                ret_arr = np.vstack((ret_arr,np.array(temp_val)))

    if average:
        for i in range(len(val_array)):
            ret_arr[i] = ret_arr[i] / num_entries[i]

    #print(ret_arr)
    return ret_arr

round_headers = [1,2,3]
round_scores = np.empty(shape =[0,len(round_headers)])#len(round_headers)))



round_headers = [1,2,3]
round_scores = np.empty(shape =[0,len(round_headers)])#len(round_headers)))


for fight in dfs:
    temp_vals = (np.array((calc_stats_for_fight(fight, "round", round_headers, average=False))))
    round_scores = np.vstack((round_scores,temp_vals))
    #round_scores = round_scores + np.array(calc_stats_for_fight(fight, "round", [1,2,3], average=False))/len(dfs)
    temp_vals = (np.array((calc_stats_for_fight(fight, "round", round_headers, average=False))))
    round_scores = np.vstack((round_scores,temp_vals))
 
averageRounds = []
stdevRounds = []

for i in range(len( round_headers )):
    vals = get_non_zero(round_scores,i)
    averageRounds += [np.average(vals)]
    stdevRounds += [np.std(vals)]

fig = plt.figure(figsize=(16,9))
ax = plt.axes()
ax.grid(True)
ax.set_title("title")
ax.set_xlabel('Round within PF')
ax.set_ylabel('Average Score (points $\pm \sigma$)')

ax.bar(round_headers, averageRounds,yerr = stdevRounds, align='center', alpha=0.5)
#plt.show()


averageRounds = []
stdevRounds = []

for i in range(len( round_headers )):
    vals = get_non_zero(round_scores,i)
    averageRounds += [np.average(vals)]
    stdevRounds += [np.std(vals)]

fig = plt.figure(figsize=(16,9))
ax = plt.axes()
ax.grid(True)
ax.set_title("title")
ax.set_xlabel('Round within PF')
ax.set_ylabel('Average Score (points $\pm \sigma$)')

ax.bar(round_headers, averageRounds,yerr = stdevRounds, align='center', alpha=0.5)
plt.show()




'''
    # Does later fights perform better?
    #for index, i in fight.iterrows():#fight.loc[df["round"]==1]:
        
        
        if i["round"] == 1:
                 
        elif i["round"] == 2:
        
        print(i["round"])
        
        #df_i = df.loc[df["fightName"]==i]


'''

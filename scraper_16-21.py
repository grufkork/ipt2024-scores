from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import pandas as pd

frame = []


# Juror, country, fight#, role, score, participant, problem, round#, fightname

def clean(s):
    return s.strip().replace("\t", "").replace("\n", "")

def filter_nums(s):
    return ''.join(filter(lambda x: x.isdigit(), s))


def parse_round(sec):
    tables = sec.find_all("table")
    people = tables[0]
    scores = tables[1]


    rows = people.find_all("tr")
    tds = rows[1].find_all("td")

    roles = {}
    r = ["Rep", "Opp", "Mod"]
    if len(tds) == 3:
        del r[2]
    for (i, role) in enumerate(r):
        split = tds[i+1].text.split("--")
        roles[role] = {
            "country": split[0],
            "name": split[1],
        }

    
    fightName = sec.find("div", {"class": "section"}).find("h1").text
    split = fightName.split("|")

    fight = split[0]
    fightnum = int(filter_nums(split[0]))
    roundnum = 0

    if "Semifinal" in fight:
        fightnum = 5
        roundnum = int(filter_nums(split[1]))
    elif "Final" in fight:
        fightnum = 6
        roundnum = int(filter_nums(split[1]))
    else:
        roundnum = int(filter_nums(split[2]))


    

    problem = sec.find(lambda tag: tag.name=="h2" and "presented" in tag.text).find("a").text
    


    rows = scores.find_all("tr")
    del rows[0]
    del rows[len(rows)-1]
    for row in rows:
        data = row.find_all("td")

        name = data[0].text

        for (i, role) in enumerate(r):
            frame.append([name, roles[role]["country"], fightnum, role, float(data[i+1].text), roles[role]["name"], problem, roundnum, fightName, -1])

for i in range(100):
    scorepage = requests.get("https://archive.ipt.ee/ipt_connect-2016-2022/IPT2022/rounds/" + str(i + 1) + "/index.html")
    print(i)


    page = bs(scorepage.text, features="html.parser")

    try:
        parse_round(page)
    except:
        print("Failed to parse " + str(i+1))

nextID = 0
fightIDs = {}

for i in range(len(frame)):
    for j in range(len(frame[i])):
        if isinstance(frame[i][j], str):
            frame[i][j] = clean(frame[i][j])

    split = frame[i][8].split("|")
    del split[len(split)-1]
    name = "".join(split)
    if not name in fightIDs:
        fightIDs[name] = nextID
        nextID += 1

    frame[i][9] = fightIDs[name]


pdframe = pd.DataFrame(frame, columns = ["juror", "country", "fight", "role", "score", "participant", "problem", "round", "fightName", "fightID"])
# print(pdframe)

pdframe.to_csv("scores.csv")

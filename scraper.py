from bs4 import BeautifulSoup as bs
import requests
import numpy as np
import pandas as pd

frame = []


# Juror, country, fight#, role, score, 

def parse_round(sec, fightN, page):
    scores = sec.find("table", {"class": "score-table"})
    rows = scores.find_all("tr")
    del rows[0]

    roles = {}

    for row in rows:
        data = row.find_all("td")

        role = data[0].text
        team = data[1].text
        name = data[2].text
        grade = data[3].text

        roles[role] = {
            "country": team,
            "name": name,
            "grade": grade
        }
    jury_marks = sec.find("div", {"class": "jury-marks"})


    fightName = page.find("h1", {"class", "title"}).text
    roundTitle = sec.find("h3").text.split("-")

    round = roundTitle[0]
    round = ''.join(filter(lambda x: x.isdigit(), round))
    round = int(round.strip())
    problem = roundTitle[1]




    rows = jury_marks.find("table").find_all("tr")
    del rows[0]
    for mark in rows:
        data = mark.find_all("td")
        name = data[0].text

        grades = {
            "Rep": data[1].text,
            "Opp": data[2].text,
            "Mod": data[3].text
        }


        for role in ["Rep", "Opp", "Mod"]:
            frame.append([name, roles[role]["country"], fightN, role, float(grades[role]), roles[role]["name"], problem, round, fightName])


    

for i in range(32):
    scorepage = requests.get("https://score.ipt.ee/fight/" + str(i + 1))
    print(i)


    page = bs(scorepage.text)

    rounds = page.find_all("section", {"class": "round"})
    for round in rounds:
        parse_round(round, i+1, page)

for i in range(len(frame)):
    for j in range(len(frame[i])):
        if isinstance(frame[i][j], str):
            frame[i][j] = frame[i][j].strip()


pdframe = pd.DataFrame(frame, columns = ["juror", "country", "fight", "role", "score", "participant", "problem", "round", "fightName"])
print(pdframe)

pdframe.to_csv("scores.csv")

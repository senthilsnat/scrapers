from bs4 import BeautifulSoup
import requests
import pandas as pd

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

p_list = []
for alph in alphabet:
    print alph
    url1 = "https://www.pro-football-reference.com/players/"+alph+"/"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
    r1 = requests.get(url1, headers=header)
    data1 = r1.text
    soup1 = BeautifulSoup(data1, "lxml")

    play = soup1.findChildren('div')
    players = play[17].findChildren('a')

    for p in players:
        p_list.append(str(p.contents[0]))

out = pd.DataFrame(p_list, columns=["names"])
out.to_csv("nflnames.csv")

import requests
from bs4 import BeautifulSoup
import pandas as pd

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

all_names = []
links = []

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']

for alph in alphabet:
    base_url = "https://www.basketball-reference.com/players/"+alph+"/"
    base_r = requests.get(base_url, headers=header)
    base_data = base_r.text
    base_soup = BeautifulSoup(base_data, "lxml")
    table = base_soup.findChildren('table')[0].findChildren('tbody')

    for p in table[0].findChildren('a'):
        if "players" in str(p):
            links.append(str(p['href']))

for linker in links:
    print linker
    url1 = "https://www.basketball-reference.com"+linker
    r1 = requests.get(url1, headers=header)
    data1 = r1.text
    soup1 = BeautifulSoup(data1, "lxml")
    heighter = soup1.findChildren('div')

    datas = list(heighter[10].findChildren('p'))[0:4]

    for nn in datas:
        if ("(" in str(nn)) and ("-" not in str(nn)):
            ind = list(heighter[10].findChildren('p')).index(nn)
            extract = str((heighter[10].findChildren('p')[ind].contents[0].strip('\n').strip('(').strip(')')).encode('utf-8'))

            if "," in extract:
                temp = extract.split(', ')
                for t in temp:
                    all_names.append(t)
            else:
                all_names.append(extract)

for n in all_names:
    if n == '':
        all_names.remove(n)

print all_names

out = pd.DataFrame(all_names, columns=["names"])
out.to_csv("nbanicknames.csv")

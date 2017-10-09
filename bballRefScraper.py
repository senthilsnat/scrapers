import requests
from bs4 import BeautifulSoup


def adv_scraper(firstname, lastname, id):

    output_arr = [firstname+" "+lastname]
    print firstname+" "+lastname

    url1 = "http://www.sports-reference.com/cbb/players/"+firstname+"-"+lastname+"-"+id+".html"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

    r1 = requests.get(url1, headers=header)
    data1 = r1.text
    soup1 = BeautifulSoup(data1, "lxml")

    # get player position
    positioner = soup1.findChildren('div')
    p_temp = str(list(positioner[12].findChildren('p')[0].children)[-1])
    if p_temp == '\n  Guard\n\n\n\n  ':
        position = "Guard"
    if p_temp == '\n  Forward\n\n\n\n  ':
        position = "Forward"
    if p_temp == '\n  Center\n\n\n\n  ':
        position = "Center"
    output_arr.append(position)

    # get player height
    heighter = soup1.findChildren('div')
    h_temp = list(heighter[12].findChildren('p')[1].findChildren('span')[0].children)[0]
    h_split = str(h_temp).split("-")
    height = (12*int(h_split[0])) + int(h_split[1])
    output_arr.append(height)

    # get player weight
    weighter = soup1.findChildren('div')
    w_temp = list(weighter[12].findChildren('p')[1].findChildren('span')[1].children)[0]
    weight = int(str(w_temp)[:-2])
    output_arr.append(weight)

    # get amount of player awards
    awarder = soup1.findChildren('ul')
    if "bling" in str(awarder[3]):
        a_temp = awarder[3].findChildren('a')
        awardsnum = len(a_temp)
    else:
        awardsnum = 0
    output_arr.append(awardsnum)

    # extract widget page for advanced data table to get player's final season advanced stats
    url2 = "http://widgets.sports-reference.com/wg.fcgi?css=1&site=cbb&url=%2Fcbb%2Fplayers%2F"+firstname+"-"+lastname+"-"+id+".html&div=div_players_advanced"
    r2 = requests.get(url2, headers=header)
    data2 = r2.text
    soup2 = BeautifulSoup(data2, "lxml")

    tables = soup2.findChildren('table')
    my_table = tables[0]
    rows = my_table.findChildren('tbody')

    years = rows[0].findChildren('tr')
    output_arr.append(len(years))
    data = years[-1].findChildren('td')

    for n in data[5:-3]:
        if list(n.children):
            output_arr.append(list(n.children)[0])

    # add interaction variables - REBxAST
    output_arr.append(float(list(data[12].children)[0])*float(list(data[13].children)[0]))
    # add interaction variables - 3PAxFTA
    output_arr.append(float(list(data[7].children)[0])*float(list(data[8].children)[0]))
    # add interaction variables - EFGxUSG
    output_arr.append(float(list(data[6].children)[0])*float(list(data[17].children)[0]))
    # add interaction variables - STLxBLK
    output_arr.append(float(list(data[14].children)[0])*float(list(data[15].children)[0]))

    # extract widget page for per-40 data table to get player's 3P%, FT%, pts per 40
    url3 = "http://widgets.sports-reference.com/wg.fcgi?css=1&site=cbb&url=%2Fcbb%2Fplayers%2F"+firstname+"-"+lastname+"-"+id+".html&div=div_players_per_min"
    r3 = requests.get(url3, headers=header)
    data3 = r3.text
    soup3 = BeautifulSoup(data3, "lxml")

    tables = soup3.findChildren('table')
    my_table = tables[0]
    rows = my_table.findChildren('tbody')

    years = rows[0].findChildren('tr')
    data = years[-1].findChildren('td')
    if list(data[12].children):
        threep = list(data[12].children)[0]
    else:
        threep = 0
    output_arr.append(threep)
    freep = list(data[15].children)[0]
    output_arr.append(freep)
    pts = list(data[-1].children)[0]
    output_arr.append(pts)

    # print output_arr

    return output_arr


def per40_scraper(firstname, lastname, id):

    output_arr = [firstname+" "+lastname]
    print firstname+" "+lastname

    url1 = "http://www.sports-reference.com/cbb/players/"+firstname+"-"+lastname+"-"+id+".html"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

    r1 = requests.get(url1, headers=header)
    data1 = r1.text
    soup1 = BeautifulSoup(data1, "lxml")

    # get player position
    positioner = soup1.findChildren('div')
    p_temp = str(list(positioner[12].findChildren('p')[0].children)[-1])
    if p_temp == '\n  Guard\n\n\n\n  ':
        position = "Guard"
    if p_temp == '\n  Forward\n\n\n\n  ':
        position = "Forward"
    if p_temp == '\n  Center\n\n\n\n  ':
        position = "Center"
    output_arr.append(position)

    # get player height
    heighter = soup1.findChildren('div')
    h_temp = list(heighter[12].findChildren('p')[1].findChildren('span')[0].children)[0]
    h_split = str(h_temp).split("-")
    height = (12*int(h_split[0])) + int(h_split[1])
    output_arr.append(height)

    # extract widget page for per-40 data table
    url3 = "http://widgets.sports-reference.com/wg.fcgi?css=1&site=cbb&url=%2Fcbb%2Fplayers%2F"+firstname+"-"+lastname+"-"+id+".html&div=div_players_per_min"
    r3 = requests.get(url3, headers=header)
    data3 = r3.text
    soup3 = BeautifulSoup(data3, "lxml")

    tables = soup3.findChildren('table')
    my_table = tables[0]
    rows = my_table.findChildren('tbody')

    years = rows[0].findChildren('tr')
    output_arr.append(len(years))
    data = years[-1].findChildren('td')

    for n in data[3:]:
        if list(n.children):
            output_arr.append(list(n.children)[0])

    # add interaction variables - REBxAST
    output_arr.append(float(list(data[-7].children)[0])*float(list(data[-6].children)[0]))
    # add interaction variables - STLxBLK
    output_arr.append(float(list(data[-5].children)[0])*float(list(data[-4].children)[0]))
    # add interaction variables - FTAx3PA
    output_arr.append(float(list(data[-12].children)[0])*float(list(data[-9].children)[0]))

    return output_arr

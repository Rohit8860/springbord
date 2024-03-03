import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
import time

cookies = {
    'PHPSESSID': '61519867453d3a9b76308274df79c02e',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://bsis.bsmou.org',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://bsis.bsmou.org/public/?button=Agree',
    # 'Cookie': 'PHPSESSID=61519867453d3a9b76308274df79c02e',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}


def list_page():
    params = {
        'action': 'getinspections',
    }

    data = {
        'imo': '',
        'callsign': '',
        'name': '',
        'From': '18.12.2023',
        'Till': '17.01.2024',
        'authority': '0',
        'flag': '0',
        'class': '0',
        'ro': '0',
        'type': '0',
        'result': '0',
        'insptype': '-1',
        'sort1': '0',
        'sort2': 'DESC',
        'sort3': '0',
        'sort4': 'DESC',
    }

    response = requests.post('https://bsis.bsmou.org/public/', params=params, cookies=cookies, headers=headers, data=data)
    print('response------->',response)
    soup = BS(response.text,'html.parser')
    data = soup.find_all('tr',onclick="onclick_shipinsp(this)")
    count = 1
    for i in data:
        input_url = i.find('input').get('value')    
        print(input_url)
        details_page(input_url)
        if count == 10:
            break
        count +=1

def details_page(input_url):
    params = {
    'action': 'getshipinsp',
    }

    data = {
        'UID': input_url,
    }

    response = requests.post('https://bsis.bsmou.org/public/', params=params, cookies=cookies, headers=headers, data=data)
    soup = BS(response.text,'html.parser')


    # soup.find_all("h2")[4].find_next_sibling()

    tabs = soup.find_all("h2")
    for i in tabs:
        tab_name = i.text
        table = i.find_next_sibling()
        x = pd.read_html(str(table).replace('$','').replace('rowspan','row'))[0]
        if tab_name in xlsx.keys():
            xlsx[tab_name] = pd.concat([xlsx[tab_name],x])
        else:
            xlsx[tab_name] = x

    # for index, i in enumerate(x):
    #     i.to_excel(writer,sheet_name=str(index+1),index=False)
    #     print(i)
    #     time.sleep(3)
    
xlsx = {}

writer = pd.ExcelWriter('data.xlsx')

list_page()

for sheet_name, dataframe in xlsx.items():
    dataframe.to_excel(writer,sheet_name=sheet_name,index=False)
    print(dataframe)
    time.sleep(3)

writer.close()
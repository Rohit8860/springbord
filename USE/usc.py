import requests
from requests import Session
session = Session()
from bs4 import BeautifulSoup as BS
import re
import json
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'segment_anonymous_id=88fc63df-20de-4cdf-9755-4726d129fdab; X-SD-URep=f2a2462d-4ec4-4093-b048-86a711ce1aa7; usc_AuthenticationCookie=88fc63df-20de-4cdf-9755-4726d129fdab; TS01f2aabf=01e4dc9a7631b5614ee43c602e9e350005ac466db7f7301f60c0f09a3d3cf0fe191c53b6ca81d88922df44b807499e6d7b48cb3c4cee41db2f3f634c1ada2746581c53e901e0ffa9d0755dcfb78abb7aa0e2e8447113f5bc9ff85890d9e332227f2e0b2bd234b0914a313a032f46c8fc01e7b580b98a8d375b3185122e4e1040864d2f34a224b21db9ef57c8c0b55b41ed20d2db5b66432a725b1b3621c5f25617fe34f1b5; _abck=5E7ABD5E391CC3F97FDE1100E64BC6AD~0~YAAQZxwgFwm6De+NAQAATn8P/gsfpqFzGVMi3Ovz8FO7as59h+PhxikGVq73dbwIh4IJKeYiIix6kiHAe97PzEn3uyJWwDFwA+17zwvUWpRhjcgnCqibxihSeYNRYkEFEbWmdRo5hLJkDUfbpbWKWQOtjPcfvCnvkK8iLJXJv3oY8he5hR8/mEKNcQQIF4p4DiLG5pfsZTxC18v6TGgWF+t1tbTTP7dR1pBzLEHcSFQFJfZzdZ7WnJuxH6Ju/+hVMkzd06SjT7JdQGiwNVJ/Kr3pg/FrwqypxFd3V58Xsg11NVekmhp8+Ym8PVoj5hP7vnuKwttNZnd8Z+YL3fZOyveTWDBH1CtxqZ2cA6IFm9Z8OyPNQK2xirG4nYyIFzbaO8j353NfB3EcUewQvxx57fc4qJDJQZ6P~-1~-1~1709368045; ak_bmsc=68323CC75EA149B95B905D349C08B200~000000000000000000000000000000~YAAQZxwgF8a9De+NAQAAr8MP/hYXnE9AXCRTY2VSBwUI3wHzoUENi316MnMbaHGmGeGmcs4eFu2mz9DLtW7DkSItL6ACESkucNP3P4ZtUeWk+czoPOQK1UsU7O/dlmf6+pHyQEeAS8jV8AhZkkgdq7PEB7B5mEYQWO+saiP9P1qrNeWju7aX30bx9E2ku5MJSPUD9IE46lUk6liWHB81InwZhRuz8kSTrvPj+64sgTVO5RrKmd2vIuwCqRfsDSziBxSRYAYZj9dtE+pJa6WG/eGBVlk2SUwJ/3WB9Z0QtbOcmCF2R1uOBnOvxlDvDeTEW0Ow6fth/t+kdUpkS9omvDmV8hhMJ6qhjYwnxXvQWGowGCCIL8N+zt0rjkvMCk47L4mBmbs08BRIggzW4QU+8PT2vtVqiES0wQ2Q34bNCJBIaEjWGcS97DO2n2KPoeFK6vmb+/ZMZa8kMR1auo9agSZR1D6L6rOOeeCDwNjte4rvxzSGfd9zm576VKghIDfD; bm_sz=E5CC58397C6F79894CAC4E1D2092BAB0~YAAQZxwgF7SzDe+NAQAAuhIP/habCUzdTfGbVmNbeU05q1U+maRKb6j4puYdEhP31r0z9C+iRo3pw0EfBeXBJOxOoQnkh5nKzE/Tl+HX+li3Gi84MxsXV5DAgn8EJi4LN1Cy8K3/4Lipzq78oQ2xX+bwnwT4DHl4WNJw465N4ee+izChci7r4exJTeu0mJ6NumIVzT3RHMWb4QIYDdYy11UCCUnpcXllPlXcs8HDx4g93iK6aJa+qokxm/nOkWEj9inafgxQQjObo/m5sotEEkGwLb7tJFcrh4Os6zpeac7l7kyERpxwZdhDw7ZIP84at0ewWDYdzbUcBnBLL85Ny+DXIRTpZ5viS6pk7rOSZDIG5wLSgbiH~4404792~4473652; _dyjsession=jg7qgemkusc4v8vtmfrxc9fc5fumv3un; dy_fs_page=www.usc.co.uk%2Fstores%2Fall; _dy_csc_ses=jg7qgemkusc4v8vtmfrxc9fc5fumv3un; _dy_c_exps=; _dy_soct=1033311.1066955.1709364418.jg7qgemkusc4v8vtmfrxc9fc5fumv3un*1033311.1066956.1709364444.jg7qgemkusc4v8vtmfrxc9fc5fumv3un*1235492.1838889.1709364673*1020024.1035687.1709364673*1106460.1317906.1709364673; selectedLevel2MenuTabId=0; _dycnst=dg; _dyid=-6498693307103521598; _dycst=dk.m.f.ms.; _dy_geo=IN.AS.IN_DL.IN_DL_Delhi; _dy_df_geo=India..Delhi; bm_sv=50D02148E12B49B5D50CE0F9363DE2FA~YAAQZxwgFznwDe+NAQAAnQQT/hYVrsGVJ7IeD3LVBir4CmOOl5prYicevG+WKNJbKk8Vp9lb7EOFjtH5Q0ddJGgaeJLSpcVecc6+FD4ZK1NdPOHJfMxN5MvC3cijAa1rJnDgeRhxusNwe/Ctr2PON6KiP4uxM2lSLpykAiPVgCucBlwVzXDoKiu9P4ySsV0770xvsFZJKY+ayokAapf3lsG+YaL+lMDcy5bGFSA5LDA/pULOms0NY4Hvl25Z7D5m~1; _dy_toffset=-212; dtCookie=v_4_srv_6_sn_702NV8NCDURHFJ020LUN8B42B9J4Q0RN_app-3Ab9702d2cec8810b9_1_ol_0_perc_100000_mul_1; rxVisitor=17093644191048B7HT6FC2EA0EG4QARG7VISJ70G91PAK; dtPC=6$564676775_806h-vWPFUTEHRBCPIGWUEECGLKKCOMEOCUKBA-0e0; rxvt=1709366479532|1709364419105; dtSa=-; _cq_duid=1.1709364419.iMoiX9CQrPEHgtZi; _cq_suid=1.1709364419.LJsLhnLPD7ASRR4L; _ALGOLIA=anonymous-f41ad517-6b7a-498e-8bd2-7f339a3515b0; _cs_c=0; _cs_id=a8220764-b087-a714-d9e3-ea53a0b5ce9f.1709364420.1.1709364678.1709364420.1.1743528420886.1; _cs_s=11.0.0.1709366478661; scarab.visitor=%2253D83B63706FBA72%22; _tt_enable_cookie=1; _ttp=2HzM4tY_Wmeo-rnAjGyyOWQRNkf; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Mar+02+2024+13%3A01%3A16+GMT%2B0530+(India+Standard+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=b31a6d64-cd87-4c96-8974-1b1da21ec76a&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=IN%3BDL&AwaitingReconsent=false; ajs_anonymous_id=88fc63df-20de-4cdf-9755-4726d129fdab; OptanonAlertBoxClosed=2024-03-02T07:27:06.565Z; _gcl_au=1.1.1881087997.1709364427; _ga=GA1.3.2049699578.1709364421; _gid=GA1.3.920965239.1709364427; AMP_TOKEN=%24NOT_FOUND; _ga_VXFM372VJS=GS1.1.1709364419.1.1.1709364677.49.0.0; _ga_E9W6WKDZGY=GS1.3.1709364427.1.1.1709364691.19.0.0; _fbp=fb.2.1709364428097.302135559; _dyid_server=-6498693307103521598; bm_mi=C433BCF0C93E95B85985A5C1F32BB5DF~YAAQZxwgF+q5De+NAQAAnHwP/haAdEPKVrb2rWGBDuicKGPZKvvCiDCIAztJoB7cBtQz5GvI3y0T/8InrUu6WiW+jK9PxwLlxumwCYs4PxDWCaBQsS/SLkEZ6hBrvtF8Vaz9RFv7ZyQ1SeZ1RWaorjatKe6pRggH3d0gETvlPPgmpeB+oKctJ7I+qWB7AObzdQbJD3ZL78KDiIf5i0ho1bA/LFJMrju4ihw906zXi95sb3C0ifIGq3oHYdY3QXssfdCxpa4Y+CxEs62lYuav9U5ylSiWvDxZ0ohCPxr2zks8uIZhBmTfM52yCfz+Cb4CegZ8CUaf8yvV5VUTS6pKZKfTUs9BdcGHhg==~1; _dy_c_att_exps=; segment_anonymous_id=88fc63df-20de-4cdf-9755-4726d129fdab',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

product = []

def main_funtion():
    response = requests.get('https://www.usc.co.uk/stores/all', headers=headers)
    soup = BS(response.text,'html.parser')
    count = 1
    for i in soup.find_all('div','letItems'):
        main_url ='https://www.usc.co.uk'+ i.find('a').get('href').replace('..','')
        title = i.find('a').text.strip().replace("\r","").replace("\n","").replace(" ","").strip()
        print(title)
        print(main_url)
        details_page(main_url,title)
        # if count ==5:   
        #     break
        # count += 1

def details_page(main_url,title):
    response = requests.get(main_url, headers=headers)
    soup = BS(response.text,'html.parser')
    website = "https://www.usc.co.uk/stores/all"
    # store_name = soup.find('div','StoreDetailsContainerInner').find('h1').find('span').text
    # print('title------',title)
    print(response)
    try:
        data =re.search('var store =  (.*?)\n',response.text).group(1).replace("\r","")
        json_objects = data.strip().split(';')
        for obj in json_objects:
            try:
                data_obj = json.loads(obj.strip())
                # name = data_obj.get('name')
                code = data_obj.get('code')
                storeType = data_obj.get('storeType')
                address = data_obj.get('address')
                try:
                    unit = re.search('Unit(.*?),',address).group(0)
                except:
                    unit = ""
                town = data_obj.get('town')
                postCode = data_obj.get('postCode')
                countryCode = data_obj.get('countryCode')
                country = data_obj.get('country')
                addressType = data_obj.get('addressType')
                brandCode = data_obj.get('brandCode')
                telephone = data_obj.get('telephone')
                description = data_obj.get('description')
                storeUrl = 'https://www.usc.co.uk/'+data_obj.get('storeUrl')
                formattedStoreName = data_obj.get('formattedStoreName')
                parentDescription = data_obj.get('parentDescription')
                openingTimes = data_obj.get('openingTimes')
                for j in openingTimes:
                    day = j['dayOfWeek']
                    if day == 0:
                        monday_opening = j['openingTime']
                        monday_closing_time = j['closingTime']
                    elif day ==1:
                        tuesday_opening = j['openingTime']
                        tuesday_closing_time = j['closingTime']     
                    elif day ==2:
                        wed_opening = j['openingTime']
                        wed_closing_time = j['closingTime']   
                    elif day ==3:
                        thurs_opening = j['openingTime']
                        thurs_closing_time = j['closingTime']   
                    elif day ==4:
                        fri_opening = j['openingTime']
                        fri_closing_time = j['closingTime']
                    elif day ==5:
                        satur_opening = j['openingTime']
                        satur_closing_time = j['closingTime']   
                    elif day ==6:
                        sun_opening = j['openingTime']
                        sun_closing_time = j['closingTime']   

                item = dict()
                item['code'] = code
                item['title'] = title 
                item['storeType'] = storeType 
                item['address'] = address 
                item['town'] = town 
                item['postCode'] = postCode 
                item['countryCode'] = countryCode 
                item['country'] = country
                item['Unit No'] = unit 
                item['brandCode'] = brandCode 
                item['telephone'] = telephone 
                item['description'] = description 
                item['storeUrl'] = storeUrl 
                item['formattedStoreName'] = formattedStoreName 
                item['parentDescription'] = parentDescription 
                item['Monday Opening'] = monday_opening
                item['Monday Closing'] = monday_closing_time 
                item['Tuesday Opening'] = tuesday_opening 
                item['Tuesday Closing'] = tuesday_closing_time 
                item['Wednesday Opening'] = wed_opening 
                item['Wednesday Closing'] = wed_closing_time 
                item['Thursday Opening'] = thurs_opening 
                item['Thursday Closing'] = thurs_closing_time 
                item['Friday Opening'] = fri_opening
                item['Friday Closing'] = fri_closing_time
                item['Saturday Opening'] = satur_opening
                item['Saturday Closing'] = satur_closing_time
                item['Sunday Opening'] = sun_opening
                item['Sunday Closing'] = sun_closing_time
                print(item)
                
                product.append(item)
                
            except:
                pass
    except:
        pass

    df = pd.DataFrame(product)
    df.to_excel('USE_OUTPUT.xlsx')

main_funtion()


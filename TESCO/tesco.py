import requests
from bs4 import BeautifulSoup as BS
import pandas as pd


cookies = {
    'atrc': '350ef028-c42b-40c6-93d4-5416763f4fba',
    '_abck': 'BF7E2233009EC7C8AECBEB92D4FD3177~0~YAAQPAVaaBDaHvCNAQAAVHYtBAspI2IQgjYp2K8PB+sFnPR36hg/q8sQR7Wkc8RNyV/mGeY0oMVzHH2zV9aLKeu/9MP/xZxCQTapejodR7l+Vnypa38pmkjT5LmBPkUOb7SR6Ze+foHPUckxzImHCQL7oFpdzVEQOTEOTkmyU31nUE/8WL4ZWlCGXrxGkiXi7eKk22MBrC2W5WN3mqiCLPAZAHRXhngxHx7gAuBZT5a7adOfJb1riaRSBkCaRRMBxOYvfYJ7eGz0wW7U+K0LaxiNvjxzsRdUKsISX4WdwE/WUzz/xO++riM9hih9ZPiJl854RZit+cPJH5w4Cr5zTgJc8Mg1OmohL84HPuNNG9m/R2Zeh/2CwWPK+obvI9WH5pyc6RBtDz0aR/Ds/6s4jKGyJIgBeTtp~-1~-1~1709470672',
    'bm_sz': 'B74C47AE23949BD9F783328F0C09F4E7~YAAQPAVaaFO4HPCNAQAAvZ6dAxYqnn4dr/oVJQDn62MLNkv28rHh4Dno3zRe/125yDiUT4iyVFv7lHTEPi96qpoeHrfH5XDQrA1ur4DkBln7CWQhHrnjXQTuejZ5m5zq9SjaMfs5YWEIIeaCUfwZ4j7aWEj5O7eZoeHjS7xxc/GB+qDCurWfrhf7fhq0x8VWSHJQaOl2b0p9Mw44qgh7siiyi4vpn8X001MW7LPn/WeYwp9NwSY5YGs49Qb63MRrQjqbU2oApfpCWfRq5xktf94Bx2N6vp4wWwzikyoO4v6gww0ygIEhL7WpuAnuesjoVHS3lH8ydhMF5suBFFQYrP8l6Me5Kt/AUMEyGY//Knz3xC/svAdiOQ==~3617605~3356227',
    'cookiePreferences': '%7B%22experience%22%3Atrue%2C%22advertising%22%3Atrue%7D',
    'AMCV_E4860C0F53CE56C40A490D45%40AdobeOrg': '1585540135%7CMCIDTS%7C19786%7CMCMID%7C32967199366741734350094917496202921394%7CMCAID%7CNONE%7CMCOPTOUT-1709474272s%7CNONE%7CvVersion%7C4.4.0',
    's_ecid': 'MCMID%7C32967199366741734350094917496202921394',
    'AMCVS_E4860C0F53CE56C40A490D45%40AdobeOrg': '1',
    's_cc': 'true',
    'AKA_A2': 'A',
    'ak_bmsc': 'CA22A120FC549F4B16A3201BE492210A~000000000000000000000000000000~YAAQPAVaaAvaHvCNAQAAYnQtBBaRb/fl+5db1/2OvvF1cJ4t5DrpDEERzvu8nep6FL3zvg0oudZQrxVBk1dlDrbH8UtsbEuYDZRkrNeaW6snZNd3wO56jze2RBu10CaLPltHG4Rveb9pK1Qo5T2nfGqvWR0rWGzu1fsaHPECVwyCv4y9Err2J57HS7d6ueu2vISkcKK/8pn8LkyuarEo/1HdApk+bP/by1QLL4qAMrR1RnKetCPCuYeVd8p2i3jGW53mmo3sWeGpqAoXdBNIrDh2re76ujiuydXc6Hc9wBtY3MbyH0ZC39jg4ydv5tJK9dWv+LMVDWaZ2ajckLF8CWao3z8qP6jjKsWmCtWuV3VzJW0lkoT5zWcmksdXtbPpK6+c41laAX/aPTvbSvEiaKhUcNg2JJSBIVxdkAAU4drv7tCrKyZQuAlVHP3Fa/tenNKd98wkyf+n1YmDgQ==',
    'bm_sv': '22BA672B550F6328C32ABD56B57BE27D~YAAQPAVaaAfaHvCNAQAAbXItBBalE4BhcNkGi6d8BS+/AU9ikETkPL9fG1nE3Cl6KCctw6OLHJal2wFETnRj4X79IOUW+CyZIZ3x0ox+TM0Va/7kDys8J+gcArn7rHjOCZ7OaQ+Od730Je7zjruvGzxoi5Wk9osvbNG9h0/R0k5ImUse/utfi2C18TTDoEirqCpECFV5VTL2q5/fQSS87Q6WUTbNEwjhf2nC7LQvbKqquX7s2Kq41jLGBE6mh4Y=~1',
    's_gpv_pn': 'store%20results',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.tesco.com/store-locator/?q=london&qp=london&l=en',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    # 'Cookie': 'atrc=350ef028-c42b-40c6-93d4-5416763f4fba; _abck=BF7E2233009EC7C8AECBEB92D4FD3177~0~YAAQPAVaaBDaHvCNAQAAVHYtBAspI2IQgjYp2K8PB+sFnPR36hg/q8sQR7Wkc8RNyV/mGeY0oMVzHH2zV9aLKeu/9MP/xZxCQTapejodR7l+Vnypa38pmkjT5LmBPkUOb7SR6Ze+foHPUckxzImHCQL7oFpdzVEQOTEOTkmyU31nUE/8WL4ZWlCGXrxGkiXi7eKk22MBrC2W5WN3mqiCLPAZAHRXhngxHx7gAuBZT5a7adOfJb1riaRSBkCaRRMBxOYvfYJ7eGz0wW7U+K0LaxiNvjxzsRdUKsISX4WdwE/WUzz/xO++riM9hih9ZPiJl854RZit+cPJH5w4Cr5zTgJc8Mg1OmohL84HPuNNG9m/R2Zeh/2CwWPK+obvI9WH5pyc6RBtDz0aR/Ds/6s4jKGyJIgBeTtp~-1~-1~1709470672; bm_sz=B74C47AE23949BD9F783328F0C09F4E7~YAAQPAVaaFO4HPCNAQAAvZ6dAxYqnn4dr/oVJQDn62MLNkv28rHh4Dno3zRe/125yDiUT4iyVFv7lHTEPi96qpoeHrfH5XDQrA1ur4DkBln7CWQhHrnjXQTuejZ5m5zq9SjaMfs5YWEIIeaCUfwZ4j7aWEj5O7eZoeHjS7xxc/GB+qDCurWfrhf7fhq0x8VWSHJQaOl2b0p9Mw44qgh7siiyi4vpn8X001MW7LPn/WeYwp9NwSY5YGs49Qb63MRrQjqbU2oApfpCWfRq5xktf94Bx2N6vp4wWwzikyoO4v6gww0ygIEhL7WpuAnuesjoVHS3lH8ydhMF5suBFFQYrP8l6Me5Kt/AUMEyGY//Knz3xC/svAdiOQ==~3617605~3356227; cookiePreferences=%7B%22experience%22%3Atrue%2C%22advertising%22%3Atrue%7D; AMCV_E4860C0F53CE56C40A490D45%40AdobeOrg=1585540135%7CMCIDTS%7C19786%7CMCMID%7C32967199366741734350094917496202921394%7CMCAID%7CNONE%7CMCOPTOUT-1709474272s%7CNONE%7CvVersion%7C4.4.0; s_ecid=MCMID%7C32967199366741734350094917496202921394; AMCVS_E4860C0F53CE56C40A490D45%40AdobeOrg=1; s_cc=true; AKA_A2=A; ak_bmsc=CA22A120FC549F4B16A3201BE492210A~000000000000000000000000000000~YAAQPAVaaAvaHvCNAQAAYnQtBBaRb/fl+5db1/2OvvF1cJ4t5DrpDEERzvu8nep6FL3zvg0oudZQrxVBk1dlDrbH8UtsbEuYDZRkrNeaW6snZNd3wO56jze2RBu10CaLPltHG4Rveb9pK1Qo5T2nfGqvWR0rWGzu1fsaHPECVwyCv4y9Err2J57HS7d6ueu2vISkcKK/8pn8LkyuarEo/1HdApk+bP/by1QLL4qAMrR1RnKetCPCuYeVd8p2i3jGW53mmo3sWeGpqAoXdBNIrDh2re76ujiuydXc6Hc9wBtY3MbyH0ZC39jg4ydv5tJK9dWv+LMVDWaZ2ajckLF8CWao3z8qP6jjKsWmCtWuV3VzJW0lkoT5zWcmksdXtbPpK6+c41laAX/aPTvbSvEiaKhUcNg2JJSBIVxdkAAU4drv7tCrKyZQuAlVHP3Fa/tenNKd98wkyf+n1YmDgQ==; bm_sv=22BA672B550F6328C32ABD56B57BE27D~YAAQPAVaaAfaHvCNAQAAbXItBBalE4BhcNkGi6d8BS+/AU9ikETkPL9fG1nE3Cl6KCctw6OLHJal2wFETnRj4X79IOUW+CyZIZ3x0ox+TM0Va/7kDys8J+gcArn7rHjOCZ7OaQ+Od730Je7zjruvGzxoi5Wk9osvbNG9h0/R0k5ImUse/utfi2C18TTDoEirqCpECFV5VTL2q5/fQSS87Q6WUTbNEwjhf2nC7LQvbKqquX7s2Kq41jLGBE6mh4Y=~1; s_gpv_pn=store%20results',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

params = {
    'q': 'london',
    'qp': 'london',
    'l': 'en',
}



class Tesco():
    def __init__(self) -> None:
        self.product = []
        pass

    def main(self):
        response = requests.get('https://www.tesco.com/store-locator/searchapi', params=params, cookies=cookies, headers=headers)
        print(response)
        # print("resonse.text------",response.text)
        self.website_url = "https://www.tesco.com"

        for i in response.json()['response']['entities']:
            self.title = i['profile']['c_bRANCH_NAME']
            self.branch = i['profile']['c_bRANCH_NO2']
            self.store_type = i['profile']['name']
            self.des = i['profile']['description']
            self.num = i['profile']['mainPhone']['number']
            self.web_url = i['profile']['websiteUrl']
            self.city = i['profile']['address']['city']
            self.line1 = i['profile']['address']['line1']
            self.line2 = i['profile']['address']['line2']
            self.line3 = i['profile']['address']['line3']
            self.postalcode = i['profile']['address']['postalCode']

            self.Facilities = ""
            self.details = i['profile']['c_additionalServiceLists']
            for j in self.details:
                service = j['serviceListURLs']
                for k in service:
                    ser = k['serviceName']
                    self.Facilities += ser+"|"


            self.Accessibility = ""
            try:
                self.access= i['profile']['c_locatorFiltersAccessibility']
                for n in self.access:
                    self.Accessibility += "|"+n
            except:
                pass
            
            self.add_des = ""
            for des in i['profile']['address'].values():
                if des != None:
                    self.add_des += "|"+des
                else:
                    pass



            # print('facility----->',Facilities)
            # print('branch',branch)
            # print('Accessibility--',Accessibility)
            # print('des',des)
            # print('num',num)
            # print('store------>',store_type)
            # print('url--------->',web_url)
            # print('city------>',city)
            # print('Street1----->',line1)
            # print('Street2------>',line2)
            # print('Street3------>',line3)
            # print("postalcode",postalcode)
            self.details_page()


    def details_page(self):
        response = requests.get(self.web_url, cookies=cookies, headers=headers)
        print(response)
        soup = BS(response.text,'html.parser')
        row = {}
        data = soup.find('table','c-hours-details').find_all('tr','c-hours-details-row js-day-of-week-row')
        for i in data:
            day_name = i.find('td','c-hours-details-row-day').text
            if day_name =="Monday":
                self.Monday_open = i.find('span','c-hours-details-row-intervals-instance-open').text
                self.Monday_close_ = i.find('span','c-hours-details-row-intervals-instance-close').text

            elif day_name == "Tuesday":
                self.Tuesday_open = i.find('span','c-hours-details-row-intervals-instance-open').text
                self.Tuesday_close_ = i.find('span','c-hours-details-row-intervals-instance-close').text
            elif day_name == "Wednesday":
                self.Wednesday_open = i.find('span','c-hours-details-row-intervals-instance-open').text
                self.Wednesday_close_ = i.find('span','c-hours-details-row-intervals-instance-close').text

            elif day_name == "Thursday":
                self.Thursday_open = i.find('span','c-hours-details-row-intervals-instance-open').text
                self.Thursday_close_ = i.find('span','c-hours-details-row-intervals-instance-close').text

            elif day_name == "Friday":
                self.Friday_open = i.find('span','c-hours-details-row-intervals-instance-open').text
                self.Friday_close_ = i.find('span','c-hours-details-row-intervals-instance-close').text
            elif day_name == "Saturday":
                self.Saturday_open = i.find('span','c-hours-details-row-intervals-instance-open').text
                self.Saturday_close_ = i.find('span','c-hours-details-row-intervals-instance-close').text

            elif day_name == "Sunday":
                self.Sunday_open = i.find('span','c-hours-details-row-intervals-instance-open').text
                self.Sunday_close_ = i.find('span','c-hours-details-row-intervals-instance-close').text



        item = dict()
        item['Title'] = self.title
        item['website_url'] = self.website_url
        item['Branch NO'] = self.branch
        item['Store_type'] = self.store_type
        item['Descriptions'] = self.des
        item['Mobile No'] = self.num
        item['Sourch_url'] = self.web_url
        item['City'] = self.city
        item['Street'] = self.line1
        item['Street1'] = self.line2
        item['Street2'] = self.line3
        item['Postalcode'] = self.postalcode
        item['Facilities'] = self.Facilities
        item['Accessibility'] = self.Accessibility
        item['Address_Description'] = self.add_des
        # item['Title'] = self.title
        # item['Title'] = self.title
        # item['Title'] = self.title
        
        item['Store_type'] = self.store_type
        item['Monday Opening'] = self.Monday_open
        item['Monday Closing'] = self.Monday_close_ 
        item['Tuesday Opening'] = self.Tuesday_open 
        item['Tuesday Closing'] = self.Tuesday_close_ 
        item['Wednesday Opening'] = self.Wednesday_open 
        item['Wednesday Closing'] = self.Wednesday_close_ 
        item['Thursday Opening'] = self.Thursday_open 
        item['Thursday Closing'] = self.Thursday_close_ 
        item['Friday Opening'] = self.Friday_open
        item['Friday Closing'] = self.Friday_close_
        item['Saturday Opening'] = self.Saturday_open
        item['Saturday Closing'] = self.Saturday_close_
        item['Sunday Opening'] = self.Sunday_open
        item['Sunday Closing'] = self.Sunday_close_

        print(item)
        self.product.append(item)

        self.excel_file()

    def excel_file(self):
        df = pd.DataFrame(self.product)
        df.to_excel('TESCO_OUTPUT.xlsx')        


bot = Tesco()
bot.main()

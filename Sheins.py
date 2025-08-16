# from PyPDF2 import PdfReader

# reader = PdfReader('aemr101.pdf')
# for page in reader.pages:
#     print(page.extract_text())


# import fitz  # PyMuPDF

# pdf_document = 'table.pdf'
# doc = fitz.open(pdf_document)
# list1 = []
# for page_num in range(len(doc)):
#     page = doc.load_page(page_num)
#     text = page.get_text()
#     list1.append(text)
# print(list1)

# import tabula
# import pandas as pd


# def pdf_to_excel(pdf_file_path, excel_file_path):
#     # Read PDF file
#     tables = tabula.read_pdf(pdf_file_path, pages='all')

#     # Write each table to a separate sheet in the Excel file
#     with pd.ExcelWriter(excel_file_path) as writer:
#         for i, table in enumerate(tables):
#             table.to_excel(writer, sheet_name=f'Sheet{i+1}')


# pdf_to_excel('table.pdf', 'test.xlsx')


# import pdfrw

# reader = pdfrw.PdfReader('aemr101.pdf')
# for page in reader.pages:
#     print(page.extract_text())


# list1 = [1,3,4,5,6,7,8,9,5,3,2,4,99]


# list2 = []
# for i in list1:
#     list2.insert(0,i)
# print(list2)


# a = '12345'
# x = [i for i in a]
# print(x)



# import camelot

# # Extract tables from the PDF file
# tables = camelot.read_pdf("table.pdf")

# # Print out the first table
# print(tables[0].df)

# # Optionally, save the table to a CSV file
# tables[0].to_csv("table.csv")

# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas

# # Create a PDF file
# c = canvas.Canvas("example.pdf", pagesize=letter)
# c.drawString(100, 100, "Hello, I'm Rohit Prajapati!")
# c.save()


# import requests
# import json
# import time

# # 官方文档地址
# # https://doc2.bitbrowser.cn/jiekou/ben-di-fu-wu-zhi-nan.html

# # 此demo仅作为参考使用，以下使用的指纹参数仅是部分参数，完整参数请参考文档

# url = "http://127.0.0.1:54345"
# headers = {'Content-Type': 'application/json'}


# def createBrowser():  # 创建或者更新窗口，指纹参数 browserFingerPrint 如没有特定需求，只需要指定下内核即可，如果需要更详细的参数，请参考文档
#     json_data = {
#         'name': 'Rohit',  # 窗口名称
#         'remark': '',  # 备注
#         'proxyMethod': 2,  # 代理方式 2自定义 3 提取IP
#         # 代理类型  ['noproxy', 'http', 'https', 'socks5', 'ssh']
#         'proxyType': 'http',
#         'host': '64.137.48.60',  # 代理主机
#         'port': '6267',  # 代理端口
#         'proxyUserName': 'yjytexjyes',  # 代理账号
#         'proxyPassword':'x6kytcvmsibp',
#         "browserFingerPrint": {  # 指纹对象
#             'coreVersion': '124'  # 内核版本 112 | 104，建议使用112，注意，win7/win8/winserver 2012 已经不支持112内核了，无法打开
#         }
#     }

#     res = requests.post(f"{url}/browser/update",
#                         data=json.dumps(json_data), headers=headers).json()
#     browserId = res['data']['id']
#     print('browser_id ----------->',browserId)
#     return browserId


# def updateBrowser():
#     json_data = {'ids': ['93672cf112a044f08b653cab691216f0'],
#                  'remark': '我是一个备注', 'browserFingerPrint': {}}
#     res = requests.post(f"{url}/browser/update/partial",
#                         data=json.dumps(json_data), headers=headers).json()
#     print("DATA : ----------->",res)


# def openBrowser(id):  # 直接指定ID打开窗口，也可以使用 createBrowser 方法返回的ID
#     json_data = {"id": f'{id}'}
#     res = requests.post(f"{url}/browser/open",
#                         data=json.dumps(json_data), headers=headers).json()
#     print('----------------------------',res)
#     print('<<<<<<<<<<<<<<<<<<<<<<<',res['data']['http'])

#     return res


# # def closeBrowser(id):  # 关闭窗口
# #     json_data = {'id': f'{id}'}
# #     requests.post(f"{url}/browser/close",
# #                   data=json.dumps(json_data), headers=headers).json()


# # def deleteBrowser(id):  # 删除窗口
# #     json_data = {'id': f'{id}'}
# #     print(requests.post(f"{url}/browser/delete",
# #           data=json.dumps(json_data), headers=headers).json())


# if __name__ == '__main__':
#     browser_id = createBrowser()
#     openBrowser(browser_id)

#     time.sleep(20)  # 等待10秒自动关闭窗口

#     # closeBrowser(browser_id)

#     # time.sleep(10)  # 等待10秒自动删掉窗口

#     # deleteBrowser(browser_id)



# def gen(x):
#     def hell():
#         print('Hi')
#         x()
#         print('hello')
#     return hell
# @gen
# def say():
#     print('world')
# say()

# 89.35.80.244:6899:yjytexjyes:x6kytcvmsibp

# proxies = {
#     "http":f"http://yjytexjyes:x6kytcvmsibp@89.35.80.244:6899",
#     "https":f"http://yjytexjyes:x6kytcvmsibp@89.35.80.244:6899"
# }
# import requests

# def bypass_ticketmaster_presale(url: str):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
#     }

#     try:
#         # Sending a GET request to the Ticketmaster presale URL
#         response = requests.get(url, headers=headers,proxies=proxies)

#         # Checking if the request was successful
#         if response.status_code == 200:
#             return "Successfully bypassed the queue and now first in line at Ticketmaster presale waiting room."
#         else:
#             return f"Failed to bypass the queue. Status code: {response.status_code}"

#     except requests.exceptions.RequestException as e:
#         return f"An error occurred: {e}"

# # Example of using the bypass_ticketmaster_presale function:

# # URL of the Ticketmaster presale waiting room
# presale_url = "https://www.ticketmaster.co.uk/artist/766720?int_cmp_name=OASIS-2025&int_cmp_id=UK-Home-601&int_cmp_creative=Home-main-1&tm_link=tm_ccp_Home_main_OASIS-2025"

# # Attempting to bypass the queue
# result = bypass_ticketmaster_presale(presale_url)
# print(result)




import threading
import requests
import math
import pandas as pd
from urllib.parse import unquote
import time
import random
import seleniumwire.undetected_chromedriver as uc
from pymongo import MongoClient
import mysql.connector
# self.proxy_list = open('ProxyNew.txt','r').readlines()
# proxy_user = 'rmwbtfpg-rotate'  
# proxy_password = "ficpgvcb0raw"
# endpoint = "p.webshare.io:80"
import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='techmagnate'
)
cursor = conn.cursor()


class Main:
    def __init__(self):
        self.cookies = {}
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': 'https://us.shein.com/Women-Tops,-Blouses-Tee-c-1766.html?adp=&categoryJump=true&ici=us_tab00navbar03menu02dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DTops%60oc%3DView%20All%60ps%3Dtab00navbar03menu02dir01%60jc%3Dreal_1766&src_module=topcat&src_tab_page_id=page_select_class1725539102521',
            'armorToken': 'T0_2.9.2_0LE2BS71N1FRZsgBdevues4xuun5XJiuL-LnzxAv3jyxekxROOmKiu5Ga0RoDHDtVDtL31gVrDckJHtgSZni3pRyohSmWzAsyKnbnbprKfQJCQ-_RRuqEJEjOiAz4DzRy6A7-RbGrbT4o9mP-PUV5Z-iZhbKORZAqz3n_OVKKyR1pgIXyyGlr3mdXTMBNe7o_1725539102687',
            'x-csrf-token': '34rW1dWy-p00_VJWofrS1lG8U8Cn7wVJ_u74',
            'x-requested-with': 'XMLHttpRequest',
            'Anti-In': '0_1.4.1_a161da_Pao9urnUFWHBq_mHePpOqMhpTL-xxyALaOjtM24Ql_cVZfUssFA4-6xcPwbQYf3Y7NdX3FIn9EhX1Atuvs3HXBPMw4evr2-oUTuF5qxK0hErGM8Gr4NTYFptfxrAEvObnf-iynLKziFrkC-2FFByHi3ynJtITKoJqlGlyhivh4N_Ur2NoKQG4e4ehTs1CqfU7dqlphIS05M4wdgAt8Hk8FCdBeqCO2HPhuB_i0EDAMwO1LtMpTBTFh62L1SYhLkMmM4e3oskfT4tTt4nJon4VFT8Tn_L4sIhE-OJuflIu-ncJsE4O17LyRsfm11pPJcAv7v5ulbkEy43G15bo_Gcd1ddwNDrrRAfjCvSxdVJGF8UfOHbL3_xuM6iNfE0jXAhT',
            'uber-trace-id': 'ff1659681fcea438:ff1659681fcea438:0:0',
            'x-gw-auth': 'a=xjqHR52UWJdjKJ0x6QrCsus66rNXR9@2.0.13&b=1725539315403&d=06942fbc37be6a98b8dee877d03ae8f6&e=WN1EwOGVmY2JhNGY4ZGY0OGFiNTgxYTBjZTNkYWFhMjUyZDU0MDliNjZjMjMyNjdjNGRhZmZiOWRlYjMyNmI4YTE2Ng%3D%3D',
            'Connection': 'keep-alive',
            # 'Cookie': 'armorUuid=20240905174834e7e8d4ac73f8278aa1b5d1c6e729d14800e4023fbb116cd600; cookieId=48BA5C9E_2AA0_C8D4_7504_5C7C4EC64DFA; sessionID_shein=s%3AMEaLJLnBdLA9Xn5Eg40Z4SUEe3KFKdoi.P4A%2BNx78tRcitkVMXEuB3nD2ts7CJx2Akv9lWK%2BR%2FpE; _cfuvid=FdA_BobDx8bC3Jg2tHPHRrMa4fBVSObllbkIx4ggCM0-1725539098250-0.0.1.1-604800000; RESOURCE_ADAPT_WEBP=1; cf_clearance=i7N1jGIQ.j9FQ80J2IvoErhWhEQDtpdYEZGSHse.8zU-1725539100-1.2.1.1-0Koap_1SFpU77td9hjI3qlB2s0Yetosf2AYDhjJy5rzcCA_z6yfd5KRoX5_zqHJDJaQBgvxv6phXUnegmbPYvbfUDRM8to.QB5w.YY7d9XHpSnuig_bhUSxi0eXTw0st7Dx.vZKMj__PHxsKyHw_itLHAc4xb5UJovQvczftJpjK9UjsVntvBEdSupbPSQCHYsi0JRfMR7BZ64jPzgB4D7LfKmvIIml4wXptEBF6DuOgBycTq.cn.Cjb1BwKa47k0Kc0YMud6.86NrcxdvLxrLYf8SDDZBgB.ZwvZerTuIUdV19b8nueTowKw24w4LY_D2t6o4edmBL1R_9yYdhUqs0wxMee188gobNVad5hYqFIYMipjC_1KeWhZCTuhA19RbcZ.B670gSueg8m.ok26A; _csrf=7Zh7lCNIXqFD8znKhZk-h739; forterToken=8012cb28284b47b98194686f80b942e2_1725539145032_478_UAS9_17ck',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }
        # self.proxy_list = open('ProxyNew.txt','r').readlines()
        # self.proxy = random.choice(self.proxy_list)
        # self.proxies = self.proxy.replace('\n', '')
        self.host = "proxy.soax.com"   ##6vpSj7JQOCEs6ukN:mobile;;;;@proxy.soax.com:9000
        self.port = "9000"
        self.proxy_user = "qKNGqjNvARGI4gMW"
        self.proxy_password = "mobile;gb;;;"

        self.URI = "mongodb://localhost:27017"
        self.client = MongoClient(self.URI)
        self.mydb = self.client['crawling'] ## database
        self.mycol = self.mydb['Jiomart_spider'] ## collection


        self.product = []
        self.lock = threading.Lock()
        

    def url_check(self, url):
        self.url = url
        self.ici = self.url.split("ici=")[1].split("&")[0]
        print("ICI : ", self.ici)
        self.src_identifier = self.url.split("src_identifier=")[1].split("&")[0]
        print("SCR_IDENTIFIER : ", self.src_identifier)
        self.src_tab_page_id = self.url.split("src_tab_page_id=")[1]
        print("src_tab_page_id  : ", self.src_tab_page_id)
        self.src_identifiers = unquote(self.url.split("src_identifier=")[1].split("&")[0])
        print('src_identifiers :', self.src_identifiers)
        self.route_id = self.src_identifiers.split("_")[-1]
        print("route_id : ", self.route_id)

        try:
            self.adp_id = self.url.split("adp=")[1].split("&")[0]
        except:
            self.adp_id = ''

        print("ADP_ID : ", self.adp_id)


        seleniumwire_options ={
        "proxy" :{
        "http": f"http://{self.proxy_user}:{self.proxy_password}@{self.host}:{self.port}",
        "https": f"http://{self.proxy_user}:{self.proxy_password}@{self.host}:{self.port}",
        }
        }

        try:
            self.driver = uc.Chrome(seleniumwire_options=seleniumwire_options)
        except:
            self.driver = uc.Chrome(seleniumwire_options=seleniumwire_options)
        self.driver.set_window_size(500,700)
        self.driver.get(self.url)
        time.sleep(10)
        
        for request in self.driver.requests:
            if request.url.startswith('https://us.shein.com/api/productList/info/get'):
                my_headers = request.headers
                print("API Headers:", my_headers)  # Print headers
                anti_in = my_headers.get('anti-in')
                print('anti_in',anti_in)
                uber_trace_id = my_headers.get('uber-trace-id')
                print('uber_trace_id',uber_trace_id)
                x_gw_auth = my_headers.get('x-gw-auth')
                print('x_gw_auth',x_gw_auth)
                referer = my_headers.get('referer')
                print('referer',referer)
                self.headers.update({'anti-in':anti_in,'uber-trace-id':uber_trace_id,'x-gw-auth':x_gw_auth,'referer':referer})


        print("cheeeeeeeeeecking")
        cookie = self.driver.get_cookies()
        for i in cookie:
            key = i.get('name')
            value = i.get('value')
            self.cookies.update({key: value})


        if self.driver.session_id:
            self.driver.quit() 
        print("GOING LIST FUNTION")
        self.list_page()


    def list_page(self):
        
        proxies = {
            "http":f"http://{self.proxy_user}:{self.proxy_password}@{self.host}:{self.port}",
            "https":f"http://{self.proxy_user}:{self.proxy_password}@{self.host}:{self.port}"
        }

        product = []
        done = False
        page = 1

        while done == False:

            params = {
                '_ver': '1.1.8',
                '_lang': 'en',
                'type': 'entity',
                'routeId': str(self.route_id),
                'page': str(page),
                'prePureGoods': '1',
                'adp': str(self.adp_id),
                'categoryJump': 'true',
                'ici': self.ici,
                'src_identifier': self.src_identifiers,
                'src_module': 'topcat',
                'src_tab_page_id': self.src_tab_page_id,
                'requestType': 'firstLoad',
                'reqSheinClub': 'true',
                'isPaid': '0',

            }
            if 'real_' in self.src_identifiers:
                params.update({'type': 'entity'})
            else:
                params.update({'type': 'selection'})

            response = requests.get('https://us.shein.com/api/productList/info/get', params=params, cookies=self.cookies, headers=self.headers,proxies=proxies)
            
            if response.status_code == 200:
                print('RESPONSE GOOD : ', response)
                print("PAGE NO : -------------------------------------------------->", page)
                goods = response.json()['goods']
                if len(goods) > 0:
                    page_no = math.ceil(response.json()['sumForPage'] / 120)
                    for i in goods:
                        try:
                            goods_id = i['goods_id']
                        except:
                            goods_id = ''
                        try:
                            title = i['goods_url_name']
                        except:
                            title = ''
                        try:
                            product_name = i['goods_url_name'].replace(" ", "-")
                        except:
                            product_name = ''

                        try:
                            product_url = f"https://us.shein.com/{product_name}-p-{goods_id}.html?src_identifier={self.src_identifier}&src_module=topcat&src_tab_page_id={self.src_tab_page_id}&mallCode=1"
                        except:
                            product_url = ''

                        row = {}
                        row.update({'Title': title, 'Product Url': product_url})
                        print("ROW : ", row)
                        product.append(row)
                        sql = "INSERT INTO seo (title, product_url) VALUES (%s, %s)"
                        values = (title,product_url)  # Replace with actual values
                        cursor.execute(sql, values)
                        conn.commit()

                else:
                    break

                if page == page_no:
                    done = True
                    try:
                        self.driver.close()
                    except:
                        self.driver.quit()

                    break

                page += 1
            else:
                print("BAD RESPONSE PLEASE CHANGE HEADERS AND COOKIES")
                break

        with self.lock:
            self.product.extend(product)


    def save_to_excel(self):
        df = pd.DataFrame(self.product)
        df.to_excel('data.xlsx', index=False)



def worker(url, main):
    main.url_check(url)



if __name__ == "__main__":
    main = Main()
    # list_url = ['https://us.shein.com/new/NEW-IN-WOMEN-CLOTHING-sc-002157082.html?adp=&categoryJump=true&ici=us_tab00navbar01menu01dir01&src_identifier=fc%3DAll%60sc%3DNew%20In%60tc%3DNEW%20IN%20WOMEN%27S%20CLOTHING%60oc%3DView%20All%60ps%3Dtab00navbar01menu01dir01%60jc%3DitemPicking_002157082&src_module=topcat&src_tab_page_id=page_select_class1725535274346','https://us.shein.com/new/Plus-Size-New-In-15-Days-sc-00210832.html?adp=&categoryJump=true&ici=us_tab01navbar01menu02dir01&src_identifier=fc%3DNew%20In%60sc%3DNew%20In%60tc%3DNew%20In%20Curve%20Clothing%60oc%3DView%20All%60ps%3Dtab01navbar01menu02dir01%60jc%3DitemPicking_00210832&src_module=topcat&src_tab_page_id=page_select_class1725535733240','https://us.shein.com/trends/Total-sc-00641093.html?adp=&categoryJump=true&ici=us_tab01navbar01menu04dir01&src_identifier=fc%3DNew%20In%60sc%3DNew%20In%60tc%3D%23SHEIN%20X%60oc%3DView%20All%60ps%3Dtab01navbar01menu04dir01%60jc%3DitemPicking_00641093&src_module=topcat&src_tab_page_id=page_store1725535765624','https://us.shein.com/hotsale/Custom-Gifts-sc-003411529.html?adp=&categoryJump=true&ici=us_tab01navbar01menu06dir01&src_identifier=fc%3DNew%20In%60sc%3DNew%20In%60tc%3DNEW%20IN%20CUSTOMIZED%20GIFTS%60oc%3DView%20All%60ps%3Dtab01navbar01menu06dir01%60jc%3DitemPicking_003411529&src_module=topcat&src_tab_page_id=page_select_class1725535785367','https://us.shein.com/Women-Tops,-Blouses-Tee-c-1766.html?adp=&categoryJump=true&ici=us_tab01navbar03menu02dir01&src_identifier=fc%3DNew%20In%60sc%3DWomen%20Clothing%60tc%3DTops%60oc%3DView%20All%60ps%3Dtab01navbar03menu02dir01%60jc%3Dreal_1766&src_module=topcat&src_tab_page_id=page_store1725536571379','https://us.shein.com/Women-Dresses-c-12472.html?adp=&categoryJump=true&ici=us_tab03navbar03menu03dir01&src_identifier=fc%3DWomen%20Clothing%60sc%3DWomen%20Clothing%60tc%3DDresses%60oc%3DView%20All%60ps%3Dtab03navbar03menu03dir01%60jc%3Dreal_12472&src_module=topcat&src_tab_page_id=page_real_class1725536662105','https://us.shein.com/Women-Bottoms-c-1767.html?adp=&categoryJump=true&ici=us_tab02navbar03menu04dir01&src_identifier=fc%3DSale%60sc%3DWomen%20Clothing%60tc%3DBottoms%60oc%3DView%20All%60ps%3Dtab02navbar03menu04dir01%60jc%3Dreal_1767&src_module=topcat&src_tab_page_id=page_real_class1725536682603','https://us.shein.com/Women-Denim-c-1930.html?adp=&categoryJump=true&ici=us_tab00navbar03menu06dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DDenim%60oc%3DView%20All%60ps%3Dtab00navbar03menu06dir01%60jc%3Dreal_1930&src_module=topcat&src_tab_page_id=page_real_class1725536713828,https://us.shein.com/Women-Clothing-c-2030.html?adp=&categoryJump=true&ici=us_tab00navbar03menu01dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DShop%20by%20category%60oc%3DView%20All%60ps%3Dtab00navbar03menu01dir01%60jc%3Dreal_2030&src_module=topcat&src_tab_page_id=page_real_class1725536775991','https://us.shein.com/Women-Outerwear-c-2037.html?adp=&categoryJump=true&ici=us_tab00navbar03menu07dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DJackets%20%26%20Coats%60oc%3DView%20All%60ps%3Dtab00navbar03menu07dir01%60jc%3Dreal_2037&src_module=topcat&src_tab_page_id=page_real_class1725536785596','https://us.shein.com/Women-Beachwear-c-2039.html?adp=&categoryJump=true&ici=us_tab02navbar03menu12dir01&src_identifier=fc%3DSale%60sc%3DWomen%20Clothing%60tc%3DBeachwear%60oc%3DView%20All%60ps%3Dtab02navbar03menu12dir01%60jc%3Dreal_2039&src_module=topcat&src_tab_page_id=page_real_class1725536803887','https://us.shein.com/Women-Wedding-c-3090.html?adp=&categoryJump=true&ici=us_tab00navbar03menu13dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DWedding%60oc%3DView%20All%60ps%3Dtab00navbar03menu13dir01%60jc%3Dreal_3090&src_module=topcat&src_tab_page_id=page_real_class1725536820617','https://us.shein.com/Women-Party-Wear-c-5360.html?adp=&categoryJump=true&ici=us_tab01navbar03menu14dir01&src_identifier=fc%3D%60sc%3DWomen%20Clothing%60tc%3DParty%20Wear%60oc%3DView%20All%60ps%3Dtab01navbar03menu14dir01%60jc%3Dreal_5360&src_module=topcat&src_tab_page_id=page_real_class1725536836311','https://us.shein.com/Maternity-Clothing-c-4437.html?adp=&categoryJump=true&ici=us_tab00navbar03menu15dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DMaternity%20Clothing%60oc%3DView%20All%60ps%3Dtab00navbar03menu15dir01%60jc%3Dreal_4437&src_module=topcat&src_tab_page_id=page_real_class1725536855983','https://us.shein.com/World-Apparel-c-3618.html?adp=&categoryJump=true&ici=us_tab00navbar03menu16dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DWorld%20Apparel%60oc%3DView%20All%60ps%3Dtab00navbar03menu16dir01%60jc%3Dreal_3618&src_module=topcat&src_tab_page_id=page_real_class1725536872175','https://us.shein.com/Series-recommend/SHEIN-Collection-New-Hot-sc-66798444.html?adp=&categoryJump=true&ici=us_tab00navbar03menu18dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DSHEIN%20collection%60oc%3DView%20All%60ps%3Dtab00navbar03menu18dir01%60jc%3DitemPicking_66798444&src_module=topcat&src_tab_page_id=page_real_class1725536888983']
    list_url = ['https://us.shein.com/Women-Wedding-c-3090.html?adp=&categoryJump=true&ici=us_tab00navbar03menu13dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DWedding%60oc%3DView%20All%60ps%3Dtab00navbar03menu13dir01%60jc%3Dreal_3090&src_module=topcat&src_tab_page_id=page_real_class1725536820617','https://us.shein.com/Women-Party-Wear-c-5360.html?adp=&categoryJump=true&ici=us_tab01navbar03menu14dir01&src_identifier=fc%3D%60sc%3DWomen%20Clothing%60tc%3DParty%20Wear%60oc%3DView%20All%60ps%3Dtab01navbar03menu14dir01%60jc%3Dreal_5360&src_module=topcat&src_tab_page_id=page_real_class1725536836311','https://us.shein.com/Maternity-Clothing-c-4437.html?adp=&categoryJump=true&ici=us_tab00navbar03menu15dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DMaternity%20Clothing%60oc%3DView%20All%60ps%3Dtab00navbar03menu15dir01%60jc%3Dreal_4437&src_module=topcat&src_tab_page_id=page_real_class1725536855983','https://us.shein.com/World-Apparel-c-3618.html?adp=&categoryJump=true&ici=us_tab00navbar03menu16dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DWorld%20Apparel%60oc%3DView%20All%60ps%3Dtab00navbar03menu16dir01%60jc%3Dreal_3618&src_module=topcat&src_tab_page_id=page_real_class1725536872175','https://us.shein.com/Series-recommend/SHEIN-Collection-New-Hot-sc-66798444.html?adp=&categoryJump=true&ici=us_tab00navbar03menu18dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DSHEIN%20collection%60oc%3DView%20All%60ps%3Dtab00navbar03menu18dir01%60jc%3DitemPicking_66798444&src_module=topcat&src_tab_page_id=page_real_class1725536888983']
    threads = []
    for url in list_url:
        t = threading.Thread(target=worker, args=(url, main))
        threads.append(t)
        t.start()
        time.sleep(5)
    # for t in threads:
    #     t.join()



# import requests
# import urllib.parse
# import math
# from urllib.parse import unquote
# import pandas as pd
# import seleniumwire.undetected_chromedriver as uc
# import time

# proxy_user = 'rmwbtfpg'  
# proxy_password = "ficpgvcb0raw"
# endpoint = "102.212.90.190:5884"
# # :rmwbtfpg:ficpgvcb0raw
# def get_chromedriver(self):
#         seleniumwire_options ={
#         "proxy" :{
#         "http": f"http://{proxy_user}:{proxy_password}@{endpoint}",
#         "https": f"http://{proxy_user}:{proxy_password}@{endpoint}",
#         }
#         }

#         try:
#             self.driver = uc.Chrome(seleniumwire_options=seleniumwire_options)
#         except:
#             self.driver = uc.Chrome(seleniumwire_options=seleniumwire_options)
#         self.driver.set_window_size(500,700)
#         self.driver.get('https://us.shein.com/Women-Tops,-Blouses-Tee-c-1766.html?adp=&categoryJump=true&ici=us_tab00navbar03menu02dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DTops%60oc%3DView%20All%60ps%3Dtab00navbar03menu02dir01%60jc%3Dreal_1766&src_module=topcat&src_tab_page_id=page_select_class1725539102521')
#         time.sleep(10)
        
#         for request in self.driver.requests:
#             if request.url.startswith('https://us.shein.com/api/productList/info/get'):
#                 my_headers = request.headers
#                 print("API Headers:", my_headers)  # Print headers
#                 anti_in = my_headers.get('anti-in')
#                 print('anti_in',anti_in)
#                 uber_trace_id = my_headers.get('uber-trace-id')
#                 print('uber_trace_id',uber_trace_id)
#                 x_gw_auth = my_headers.get('x-gw-auth')
#                 print('x_gw_auth',x_gw_auth)
#                 referer = my_headers.get('referer')
#                 print('referer',referer)



#         print("cheeeeeeeeeecking")
#         cookie = self.driver.get_cookies()
#         for i in cookie:
#             key = i.get('name')
#             value = i.get('value')
#             # cookies.update({key: value})


#         time.sleep(100)
#         time.sleep(100)




# get_chromedriver()




# class main():
#     def __init__(self) -> None:
#         cookies = {
#             'cookieId': '42EECF71_D734_65D4_6D2A_45F65E06AAC5',
#             'sessionID_shein': 's%3AAAp1tOBxjt8V9aHgBG3qwfEQQoxeKI_o.0NG7eqh9cKHsrMTLtMqoD%2BOMgf61Wgtvo8dGq9LOKco',
#             '_cfuvid': 'mjWbKPvdnl1xaVEyw2yrYv2WQTk0H844X.g3Lv6igGM-1725537967193-0.0.1.1-604800000',
#             'RESOURCE_ADAPT_WEBP': '1',
#             'cf_clearance': 'DPU5S8XkhPTGHv8iOzc.QxR1kpyAcihSBZUzJDFfVxM-1725537975-1.2.1.1-lQeVaOXlKditb3zCfN7ebxjbRO10wqSZlT4cGLR9Ix6Pyq03XtaA9Ow9_5Q4tPLqbzhyZQ3FUBVX0SM9wP5x7iKHri_0nCwpBdPoFTc.OZds2MlZt_sdIOmuyCODbabRcsLub.CcE.NCXeRhx7G_zI8IIYQUsJeayWcZW2tSlDAvbeREAnUX_72.Hw5PxC0Qn4OwFDxwHvUDhF6dZe_ZCdiNtrrMMCgOzvxK7eyJmFAYbFndMs7aDEbdKyHNlRNZ53_bjk7ouKkWrT1gUlEHkzwaEa.gNJ__23IhnIavrPpwZzhGfsMTxGSjteah4gCx.6iySR5P0rWsp1YJYUDGa6ebfZIyQiHFeglApQEbdHSpNLM3xekMlhmT7kirPXqVP1oqwAllwoCsRe1fMSTs.nh5OT0uwpYlF_Y_rY_PTaeFiLfrndHwESHJAc9ESM5p9ckv7LfMgwOreF8C8KpmyQ',
#         }


#         self.headers = {
#             'accept': 'application/json, text/plain, */*',
#             'accept-language': 'en-US,en;q=0.9',
#             'anti-in': '0_1.4.1_4e9351_Ay7yenHDCP3QbkMsnvkqZXHEOT6xluuhsYK2_XhQvAvABk1cC81x0DACVqTD0fXqXJebTkLEUWNkSQNck8H7gW0L5JO76RH4XaTLG-uH6_rDSvYhv2JH3JYHEqgpEe_nicxarpOXZ7AtkSk4ruNz54Tv_AgWb61LmLOxtl02box44Mk0v8tdWJA-B_8QgNyT1f3rM31g6MEOGvZs9U80iJysr0GIsasw84jPvhjNNqz01icTU-zJIylmYBhYGqvxgzuEcjb40_135iXYhE-0phuT5vXdiivAlcW5dXzVk--c4uH5lzzk6ujMf_jR3gkMZEfQie__VgPzBhoNTe7kTrjiirRF2k5YFk_3L6iHUHDsDxOJG_HHJU6NBJ9EiPUVYYfKbcyif1pVkPL5B0G5LSbu15mj48zMoMvxoLQLnBioVnElsywy_BWOvS-fUu0kra0YY1TtJrdITdwaR0bMT9lErxRX9065YwpzCw-WtE9NJXg89UG4T-ydO5i2Idc36Z1cwfTNRX4aIu8tml6y0SeMy7gh7YlM3OZRRDLcoH-8OkHkwUv_ytfZvw5nATNFu-8GOkmMkpqwA6eDbh23Z2Ovruet8zV7lBt59aEBPekH',
#             'armortoken': '',
#             # 'cookie': 'cookieId=42EECF71_D734_65D4_6D2A_45F65E06AAC5; sessionID_shein=s%3AAAp1tOBxjt8V9aHgBG3qwfEQQoxeKI_o.0NG7eqh9cKHsrMTLtMqoD%2BOMgf61Wgtvo8dGq9LOKco; _cfuvid=mjWbKPvdnl1xaVEyw2yrYv2WQTk0H844X.g3Lv6igGM-1725537967193-0.0.1.1-604800000; RESOURCE_ADAPT_WEBP=1; cf_clearance=DPU5S8XkhPTGHv8iOzc.QxR1kpyAcihSBZUzJDFfVxM-1725537975-1.2.1.1-lQeVaOXlKditb3zCfN7ebxjbRO10wqSZlT4cGLR9Ix6Pyq03XtaA9Ow9_5Q4tPLqbzhyZQ3FUBVX0SM9wP5x7iKHri_0nCwpBdPoFTc.OZds2MlZt_sdIOmuyCODbabRcsLub.CcE.NCXeRhx7G_zI8IIYQUsJeayWcZW2tSlDAvbeREAnUX_72.Hw5PxC0Qn4OwFDxwHvUDhF6dZe_ZCdiNtrrMMCgOzvxK7eyJmFAYbFndMs7aDEbdKyHNlRNZ53_bjk7ouKkWrT1gUlEHkzwaEa.gNJ__23IhnIavrPpwZzhGfsMTxGSjteah4gCx.6iySR5P0rWsp1YJYUDGa6ebfZIyQiHFeglApQEbdHSpNLM3xekMlhmT7kirPXqVP1oqwAllwoCsRe1fMSTs.nh5OT0uwpYlF_Y_rY_PTaeFiLfrndHwESHJAc9ESM5p9ckv7LfMgwOreF8C8KpmyQ',
#             'priority': 'u=1, i',
#             'referer': 'https://us.shein.com/new/Plus-Size-New-In-15-Days-sc-00210832.html?adp=&categoryJump=true&ici=us_tab01navbar01menu02dir01&src_identifier=fc%3D%60sc%3DNew%20In%60tc%3DNew%20In%20Curve%20Clothing%60oc%3DView%20All%60ps%3Dtab01navbar01menu02dir01%60jc%3DitemPicking_00210832&src_module=topcat&src_tab_page_id=page_select_class1725537772034',
#             'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
#             'sec-ch-ua-arch': '"x86"',
#             'sec-ch-ua-bitness': '"64"',
#             'sec-ch-ua-full-version': '"128.0.2739.54"',
#             'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.114", "Not;A=Brand";v="24.0.0.0", "Microsoft Edge";v="128.0.2739.54"',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-model': '""',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-ch-ua-platform-version': '"15.0.0"',
#             'sec-fetch-dest': 'empty',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-site': 'same-origin',
#             'smdeviceid': '',
#             'uber-trace-id': 'ffbe4d89b4bedd4f:ffbe4d89b4bedd4f:0:0',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
#             'x-csrf-token': 'sBQEQgfR-XlwMyZAe47sF1RY3zyMwvDarpHA',
#             'x-gw-auth': 'a=xjqHR52UWJdjKJ0x6QrCsus66rNXR9@2.0.13&b=1725537977070&d=06942fbc37be6a98b8dee877d03ae8f6&e=KvAmtYmI5YWEzODc1MTZjNGE1ODdjYjU1NDFiY2JhMjU5MzlmYzcwYzNkOGMxYmQ2NDQyNGYxODI4MjBhNmUxMzYxNA%3D%3D',
#             'x-requested-with': 'XMLHttpRequest',
#         }
#         # self.product = []
#         # self.row = {}
#         self.url_check('')


#     def get_chromedriver(self):
#         seleniumwire_options ={
#         "proxy" :{
#         "http": f"http://{proxy_user}:{proxy_password}@{endpoint}",
#         "https": f"http://{proxy_user}:{proxy_password}@{endpoint}",
#         }
#         }

#         try:
#             self.driver = uc.Chrome(seleniumwire_options=seleniumwire_options)
#         except:
#             self.driver = uc.Chrome(seleniumwire_options=seleniumwire_options)
#         self.driver.set_window_size(500,700)
#         self.driver.get('https://us.shein.com/Women-Tops,-Blouses-Tee-c-1766.html?adp=&categoryJump=true&ici=us_tab00navbar03menu02dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DTops%60oc%3DView%20All%60ps%3Dtab00navbar03menu02dir01%60jc%3Dreal_1766&src_module=topcat&src_tab_page_id=page_select_class1725539102521')
#         time.sleep(10)
        
#         for request in self.driver.requests:
#             if request.url.startswith('https://us.shein.com/api/productList/info/get'):
#                 my_headers = request.headers
#                 print("API Headers:", my_headers)  # Print headers
#                 anti_in = my_headers.get('anti-in')
#                 print('anti_in',anti_in)
#                 uber_trace_id = my_headers.get('uber-trace-id')
#                 print('uber_trace_id',uber_trace_id)
#                 x_gw_auth = my_headers.get('x-gw-auth')
#                 print('x_gw_auth',x_gw_auth)
#                 referer = my_headers.get('referer')
#                 print('referer',referer)
                


#         print("cheeeeeeeeeecking")
#         cookie = self.driver.get_cookies()
#         for i in cookie:
#             key = i.get('name')
#             value = i.get('value')
#             self.cookies.update({key: value})


#         time.sleep(100)
#         time.sleep(100)


#     def url_check(self):
#         # url = 'https://us.shein.com/Women-Leggings-c-1871.html?adp=36095942&categoryJump=true&ici=us_tab00navbar03menu04dir06&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DBottoms%60oc%3DLeggings%60ps%3Dtab00navbar03menu04dir06%60jc%3Dreal_1871&src_module=topcat&src_tab_page_id=page_real_class1725530553446'
#         list_url = ['https://us.shein.com/new/NEW-IN-WOMEN-CLOTHING-sc-002157082.html?adp=&categoryJump=true&ici=us_tab00navbar01menu01dir01&src_identifier=fc%3DAll%60sc%3DNew%20In%60tc%3DNEW%20IN%20WOMEN%27S%20CLOTHING%60oc%3DView%20All%60ps%3Dtab00navbar01menu01dir01%60jc%3DitemPicking_002157082&src_module=topcat&src_tab_page_id=page_select_class1725535274346','https://us.shein.com/new/Plus-Size-New-In-15-Days-sc-00210832.html?adp=&categoryJump=true&ici=us_tab01navbar01menu02dir01&src_identifier=fc%3DNew%20In%60sc%3DNew%20In%60tc%3DNew%20In%20Curve%20Clothing%60oc%3DView%20All%60ps%3Dtab01navbar01menu02dir01%60jc%3DitemPicking_00210832&src_module=topcat&src_tab_page_id=page_select_class1725535733240','https://us.shein.com/trends/Total-sc-00641093.html?adp=&categoryJump=true&ici=us_tab01navbar01menu04dir01&src_identifier=fc%3DNew%20In%60sc%3DNew%20In%60tc%3D%23SHEIN%20X%60oc%3DView%20All%60ps%3Dtab01navbar01menu04dir01%60jc%3DitemPicking_00641093&src_module=topcat&src_tab_page_id=page_store1725535765624','https://us.shein.com/hotsale/Custom-Gifts-sc-003411529.html?adp=&categoryJump=true&ici=us_tab01navbar01menu06dir01&src_identifier=fc%3DNew%20In%60sc%3DNew%20In%60tc%3DNEW%20IN%20CUSTOMIZED%20GIFTS%60oc%3DView%20All%60ps%3Dtab01navbar01menu06dir01%60jc%3DitemPicking_003411529&src_module=topcat&src_tab_page_id=page_select_class1725535785367','https://us.shein.com/Women-Tops,-Blouses-Tee-c-1766.html?adp=&categoryJump=true&ici=us_tab01navbar03menu02dir01&src_identifier=fc%3DNew%20In%60sc%3DWomen%20Clothing%60tc%3DTops%60oc%3DView%20All%60ps%3Dtab01navbar03menu02dir01%60jc%3Dreal_1766&src_module=topcat&src_tab_page_id=page_store1725536571379','https://us.shein.com/Women-Dresses-c-12472.html?adp=&categoryJump=true&ici=us_tab03navbar03menu03dir01&src_identifier=fc%3DWomen%20Clothing%60sc%3DWomen%20Clothing%60tc%3DDresses%60oc%3DView%20All%60ps%3Dtab03navbar03menu03dir01%60jc%3Dreal_12472&src_module=topcat&src_tab_page_id=page_real_class1725536662105','https://us.shein.com/Women-Bottoms-c-1767.html?adp=&categoryJump=true&ici=us_tab02navbar03menu04dir01&src_identifier=fc%3DSale%60sc%3DWomen%20Clothing%60tc%3DBottoms%60oc%3DView%20All%60ps%3Dtab02navbar03menu04dir01%60jc%3Dreal_1767&src_module=topcat&src_tab_page_id=page_real_class1725536682603','https://us.shein.com/Women-Denim-c-1930.html?adp=&categoryJump=true&ici=us_tab00navbar03menu06dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DDenim%60oc%3DView%20All%60ps%3Dtab00navbar03menu06dir01%60jc%3Dreal_1930&src_module=topcat&src_tab_page_id=page_real_class1725536713828,https://us.shein.com/Women-Clothing-c-2030.html?adp=&categoryJump=true&ici=us_tab00navbar03menu01dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DShop%20by%20category%60oc%3DView%20All%60ps%3Dtab00navbar03menu01dir01%60jc%3Dreal_2030&src_module=topcat&src_tab_page_id=page_real_class1725536775991','https://us.shein.com/Women-Outerwear-c-2037.html?adp=&categoryJump=true&ici=us_tab00navbar03menu07dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DJackets%20%26%20Coats%60oc%3DView%20All%60ps%3Dtab00navbar03menu07dir01%60jc%3Dreal_2037&src_module=topcat&src_tab_page_id=page_real_class1725536785596','https://us.shein.com/Women-Beachwear-c-2039.html?adp=&categoryJump=true&ici=us_tab02navbar03menu12dir01&src_identifier=fc%3DSale%60sc%3DWomen%20Clothing%60tc%3DBeachwear%60oc%3DView%20All%60ps%3Dtab02navbar03menu12dir01%60jc%3Dreal_2039&src_module=topcat&src_tab_page_id=page_real_class1725536803887','https://us.shein.com/Women-Wedding-c-3090.html?adp=&categoryJump=true&ici=us_tab00navbar03menu13dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DWedding%60oc%3DView%20All%60ps%3Dtab00navbar03menu13dir01%60jc%3Dreal_3090&src_module=topcat&src_tab_page_id=page_real_class1725536820617','https://us.shein.com/Women-Party-Wear-c-5360.html?adp=&categoryJump=true&ici=us_tab01navbar03menu14dir01&src_identifier=fc%3D%60sc%3DWomen%20Clothing%60tc%3DParty%20Wear%60oc%3DView%20All%60ps%3Dtab01navbar03menu14dir01%60jc%3Dreal_5360&src_module=topcat&src_tab_page_id=page_real_class1725536836311','https://us.shein.com/Maternity-Clothing-c-4437.html?adp=&categoryJump=true&ici=us_tab00navbar03menu15dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DMaternity%20Clothing%60oc%3DView%20All%60ps%3Dtab00navbar03menu15dir01%60jc%3Dreal_4437&src_module=topcat&src_tab_page_id=page_real_class1725536855983','https://us.shein.com/World-Apparel-c-3618.html?adp=&categoryJump=true&ici=us_tab00navbar03menu16dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DWorld%20Apparel%60oc%3DView%20All%60ps%3Dtab00navbar03menu16dir01%60jc%3Dreal_3618&src_module=topcat&src_tab_page_id=page_real_class1725536872175','https://us.shein.com/Series-recommend/SHEIN-Collection-New-Hot-sc-66798444.html?adp=&categoryJump=true&ici=us_tab00navbar03menu18dir01&src_identifier=fc%3DAll%60sc%3DWomen%20Clothing%60tc%3DSHEIN%20collection%60oc%3DView%20All%60ps%3Dtab00navbar03menu18dir01%60jc%3DitemPicking_66798444&src_module=topcat&src_tab_page_id=page_real_class1725536888983']
#         for i in list_url:
#             self.url = i
#             self.ici = self.url.split("ici=")[1].split("&")[0]
#             print("ICI : ",self.ici)
#             self.src_identifier = self.url.split("src_identifier=")[1].split("&")[0]
#             print("SCR_IDENTIFIER : ", self.src_identifier)
#             self.src_tab_page_id = self.url.split("src_tab_page_id=")[1]
#             print("src_tab_page_id  : ",self.src_tab_page_id)
#             self.src_identifiers = unquote(self.url.split("src_identifier=")[1].split("&")[0])
#             print('src_identifiers :',self.src_identifiers)
#             self.route_id = self.src_identifiers.split("_")[-1]
#             print("route_id : ",self.route_id)
#             try:
#                 self.adp_id = self.url.split("adp=")[1].split("&")[0]
#             except:
#                 self.adp_id = ''
#             print("ADP_ID : ",self.adp_id)
#             self.list_page()



#     def list_page(self):
        
#         self.product = []
#         done = False
#         page = 1
#         while done == False:
#             params = {
#                 '_ver': '1.1.8',
#                 '_lang': 'en',
#                 'type': 'entity',
#                 'routeId': str(self.route_id),
#                 'page': str(page),
#                 'prePureGoods': '1',
#                 'adp': str(self.adp_id),
#                 'categoryJump': 'true',
#                 'ici': self.ici,
#                 'src_identifier': self.src_identifiers,
#                 'src_module': 'topcat',
#                 'src_tab_page_id': self.src_tab_page_id,
#                 'requestType': 'firstLoad',
#                 'reqSheinClub': 'true',
#                 'isPaid': '0',
#             }
#             if 'real_' in self.src_identifiers:
#                 params.update({'type':'entity'})
#             else:
#                 params.update({'type':'selection'})

#             response = requests.get('https://us.shein.com/api/productList/info/get', params=params, cookies=self.cookies, headers=self.headers)
            

#             if response.status_code == 200:
#                 print('RESPONSE GOOD : ',response)

#                 print("PAGE NO : -------------------------------------------------->",page)
#                 self.goods = response.json()['goods']
#                 if len(self.goods) > 0 :
#                     page_no = math.ceil(response.json()['sumForPage']/120)
#                     for i in self.goods:
#                         try:
#                             self.goods_id = i['goods_id']
#                         except:
#                             self.goods_id = ''
#                         try:
#                             self.title = i['goods_url_name']
#                         except:
#                             self.title = ''
#                         try:
#                             self.product_name = i['goods_url_name'].replace(" ","-")
#                         except:
#                             self.product_name = ''
#                         try:
#                             self.product_url = f"https://us.shein.com/{self.product_name}-p-{self.goods_id}.html?src_identifier={self.src_identifier}&src_module=topcat&src_tab_page_id={self.src_tab_page_id}&mallCode=1"
#                         except:
#                             self.product_url
#                         # print("self.Title : ",self.title)
#                         # print("PRODUCT URL : ",self.product_url)
#                         self.row = {}
#                         self.row.update({'Title':self.title,'Product Url':self.product_url})
#                         print("ROW : ",self.row)
                    
#                         self.product.append(self.row)
#                 else:
#                     break

#                 if page == page_no:
#                     done = True
#                     break

#                 page += 1

#             else:
#                 print("BAD RESPONSE PLEASE CHANGE HEADERS AND COOKIES")

    
#     def save_to_excel(self):
#         df = pd.DataFrame(self.product)
#         df.to_excel('data.xlsx', index=False)



# # bot = main()
# # bot.save_to_excel()
# # df = pd.DataFrame(product)
# # df.to_excel('CHECK.xlsx',index=False)

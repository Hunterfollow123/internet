import json
import requests
import time
import random

with open("familyNames.json", "r", encoding="utf-8") as file:
    data = json.load(file)
familyNames = data["familyNames"]

with open("firstNames.json", "r", encoding="utf-8") as file:
    data2 = json.load(file)
firstNames = data2["firstNames"]

with open("wilayas.json", "r", encoding="utf-8") as file:
    data3 = json.load(file)
wilayas = data3["wilayas"]

with open("baladiya.json", "r", encoding="utf-8") as file:
    data4 = json.load(file)
baladiyat = data4["municipalities"]



def getName():
    return random.choice(firstNames) + ' ' + random.choice(familyNames)

def getPhone():
    provider = random.choice(['05', '07', '06'])
    return provider + ''.join(map(str, random.choices(list(range(10)), k=8)))

def getPlace():
    return random.randint(0, 48)

def getWilaya(n):
    return wilayas[n]

def getBaladiya(n):
    return baladiyat[n]

def getNumber():
    return ' ' + str(random.randint(1, 10)) + ' '

def getProduct():
    return random.choice(['500DA - 80GB', '900DA - 160GB', '1000DA - 250GB', '1200DA - 320GB', '1550DA - 500GB', '2900DA - 1TB'])

def getSize():
    return random.choice(['HDD 2.5', 'HDD 3.5'])


url = 'https://api.telegram.org/bot6631368167:AAGFINjpsf5Mc4FkIVhWY0lElQwkrO8VWrY/sendMessage'
url2 = 'https://disque-dur.vercel.app'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Lenovo-A6020l36 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36'
}
n=0
while 1:
    num = getPlace()
     data = {
         "chat_id":"-1001850388716",
         "text":f"\n        طلب جديد من {getName()}\n\n        رقم الهاتف: {getPhone()}\n\n        الولاية: {getWilaya(num)}\n\n        البلدية: {getBaladiya(num)}\n\n        الاختيار المحدد: \n\n        الكمية: {getNumber()}\n\n        المنتج المحدد: {getProduct()}\n\n        حجم ديسك دير: {getSize()}\n\n    "
         }
    ##data = {
     #   "chat_id":"-1001850388716",
     #   "text":f"\n        طلب جديد من جاك عزرائيل\n\n        رقم الهاتف: {getPhone()}\n\n        الولاية: قالولي نتا سراق ولد قحبة\n\n        البلدية: يدك في زبي\n\n        الاختيار المحدد: \n\n        الكمية: شفت كفاه جبت تطيح ليماك\n\n        المنتج المحدد: رجع للسيد لي سرقتو دراهمو ولا ننيكك هذا مجرد تحذير ما شفت والو اسمو Mohamed Oukil\n\n        حجم ديسك دير: حجم بزازل مك\n\n    "
      #  }
    resp = requests.post(url, data=data, headers=headers)
    if resp.status_code == 200:
        n+=1
        print(f'Requests sent: {n}               ', end='\r')
    else:
        print('Rate limited, sleeping..', end='\r')
        time.sleep(10)

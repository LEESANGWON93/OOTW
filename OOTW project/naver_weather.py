import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://search.naver.com/search.naver?query=날씨',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

data1 = soup.find('div', {'class': 'weather_box'})

find_address = data1.find('span', {'class':'btn_select'}).text
print('현재 위치: '+find_address)

find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
print('현재 온도: '+find_currenttemp+'℃')

find_cast = soup.find('p', {'class' : 'cast_txt'}).text
print('날씨 상태: '+find_cast)

find_minnum = soup.find('span', {'class' : 'min'}).text 
find_maxnum = soup.find('span', {'class' : 'max'}).text 
print('최저/최고 온도: '+find_minnum+ "/" +find_maxnum)

find_sensible = soup.find('span', {'class' : 'sensible'}).text[5:]
print('체감 온도: '+find_sensible)


# DB에 데이터 넣기
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

item = {
        "address": find_address,
        "currenttemp": find_currenttemp,
        "min": find_minnum,
        "max": find_maxnum,
        "sensible": find_sensible
    }

db.weather.insert_one(item)
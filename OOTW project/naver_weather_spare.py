import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://search.naver.com/search.naver?query=날씨',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

ErrorCheck = soup.find('span', {'class' : 'btn_select'})
if 'None' in str(ErrorCheck): print("Error! 지역 검색 오류!")
else:
    # 지역 정보
    for i in soup.select('span[class=btn_select]'): LocationInfo = i.text

    # 현재 온도
    NowTemp = soup.find('span', {'class': 'todaytemp'}).text + soup.find('span', {'class' : 'tempmark'}).text[2:]

    # 날씨 캐스트
    WeatherCast = soup.find('p', {'class' : 'cast_txt'}).text

    # 오늘 오전온도, 오후온도, 체감온도
    TodayMorningTemp = soup.find('span', {'class' : 'min'}).text 
    TodayAfternoonTemp = soup.find('span', {'class' : 'max'}).text 
    TodayFeelTemp = soup.find('span', {'class' : 'sensible'}).text[5:]
    
    # 내일 오전, 오후 온도 및 상태 체크 
    tomorrowArea = soup.find('div', {'class': 'tomorrow_area'})
    tomorrowCheck = tomorrowArea.find_all('div', {'class': 'main_info morning_box'})

    # 내일 오전온도
    tomorrowMoring1 = tomorrowCheck[0].find('span', {'class': 'todaytemp'}).text 
    tomorrowMoring2 = tomorrowCheck[0].find('span', {'class' : 'tempmark'}).text[2:] 
    tomorrowMoring = tomorrowMoring1 + tomorrowMoring2

    # 내일 오전상태
    tomorrowMState1 = tomorrowCheck[0].find('div', {'class' : 'info_data'}) 
    tomorrowMState2 = tomorrowMState1.find('ul', {'class' : 'info_list'}) 
    tomorrowMState3 = tomorrowMState2.find('p', {'class' : 'cast_txt'}).text 
    tomorrowMState4 = tomorrowMState2.find('div', {'class' : 'detail_box'}) 
    tomorrowMState = tomorrowMState3 

    # 내일 오후온도 
    tomorrowAfter1 = tomorrowCheck[1].find('p', {'class' : 'info_temperature'}) 
    tomorrowAfter2 = tomorrowAfter1.find('span', {'class' : 'todaytemp'}).text 
    tomorrowAfter3 = tomorrowAfter1.find('span', {'class' : 'tempmark'}).text[2:] 
    tomorrowAfter = tomorrowAfter2 + tomorrowAfter3

    # 내일 오후상태 
    tomorrowAState1 = tomorrowCheck[1].find('div', {'class' : 'info_data'}) 
    tomorrowAState2 = tomorrowAState1.find('ul', {'class' : 'info_list'}) 
    tomorrowAState3 = tomorrowAState2.find('p', {'class' : 'cast_txt'}).text 
    tomorrowAState4 = tomorrowAState2.find('div', {'class' : 'detail_box'})  
    tomorrowAState = tomorrowAState3

print("=========================================") 
print(LocationInfo + " 날씨 정보입니다.") 
print("=========================================") 
print("현재온도: " + NowTemp) 
print("체감온도: " + TodayFeelTemp) 
print("오전/오후 온도: " + TodayMorningTemp + "/" + TodayAfternoonTemp)
print("현재 상태: " + WeatherCast) 
print("=========================================") 
print(LocationInfo + " 내일 날씨 정보입니다.") 
print("=========================================") 
print("내일 오전 온도: " + tomorrowMoring) 
print("내일 오전 상태: " + tomorrowMState) 
print("내일 오후 온도: " + tomorrowAfter) 
print("내일 오후 상태: " + tomorrowAState)

import requests
import time
from datetime import datetime, timedelta

def get_weather(api_key, city):
    """
    OpenWeatherMap API를 사용하여 지정된 도시의 날씨 정보를 가져옵니다.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    # url에 요청을 보낸 결과를 response로 받음.
    response = requests.get(url)
    # print(response)
    try:
        if response.status_code == 200: # 정상적으로 API 호출이 완료됨.
            data = response.json() # json으로 변경
            # print(data)
            temperature = data
        return temperature
    except:
        print("Cannot GET Response")
        return None, None

def main():
    api_key = 'bd6bd166489c86d8429a616f5b6e6cf9'
    city1 = input("날씨를 확인하고 싶은 도시 이름을 입력하세요: ")
    city2 = input("날씨를 확인하고 싶은 도시 이름을 입력하세요: ")
    a = time.localtime()
    b = []
    a = list(a[:-3])
    seoul = []
    london = []
    while True:
        t = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        if len(b) == 2:
                break
        temperature1 = get_weather(api_key, city1)
        temperature2 = get_weather(api_key, city2)
        temperature1['time'] = t
        temperature2['time'] = t
        seoul.append(temperature1)
        london.append(temperature2)
        time.sleep(10)
        b.append("1")
            
    with open("weather_seoul.csv", "w") as f:
        for i in seoul:
            f.write(f"{i}\n")
            print(datetime.utcfromtimestamp(i["dt"])+timedelta(hours=9))

    with open("weather_london.csv", "w") as f:
        for i in london:
            f.write(f"{i}\n")
            print(datetime.utcfromtimestamp(i["dt"])+timedelta(hours=9))



    # if temperature:
    #     print(f"{city}의 현재 기온은 {temperature}°C이며, 날씨는 {weather_description}입니다.")
    # else:
    #     print("날씨 정보를 가져오는 데 실패했습니다. 도시 이름을 확인하거나 나중에 다시 시도해주세요.")

if __name__ == "__main__":
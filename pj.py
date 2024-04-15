import requests

def get_weather(api_key, city):
    """
    OpenWeatherMap API를 사용하여 지정된 도시의 날씨 정보를 가져옵니다.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    try:
		    response.status_code == 200  # 정상적으로 API 호출이 완료됨.
	      data = response.json()
	      
        ############################# TODO #############################
        ## 받아온 data 변수의 내용을 보고, 기온과 날씨 상태를 추출하여 return 하세요 ##
        ################################################################
        
        return temperature, weather_description
    except:
		    print("Cannot GET Response")
		    return None, None

def main():
    api_key = '여기에_당신의_API_키를_입력하세요'
    city = input("날씨를 확인하고 싶은 도시 이름을 입력하세요: ")
    temperature, weather_description = get_weather(api_key, city)
    if temperature:
        print(f"{city}의 현재 기온은 {temperature}°C이며, 날씨는 {weather_description}입니다.")
    else:
        print("날씨 정보를 가져오는 데 실패했습니다. 도시 이름을 확인하거나 나중에 다시 시도해주세요.")

if __name__ == "__main__":
    main()
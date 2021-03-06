import requests

API_KEY = "29c17a3fbc8c9e4e65477eed31e02f2c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 237.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "celius")
else:
    print("An error occurred.")
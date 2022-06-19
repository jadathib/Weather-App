import requests 

API_KEY = "07d9ae8c85a71d37d50a513743b09234"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200: 
  data = response.json()
  weather = data['weather'][0]['description']
  print('Looks like it is', weather, 'today, fren' )
  temperature = round((((data["main"]["temp"]-273.15) * 1.8) + 32), 1)
  print(temperature, 'degrees Fahrenheit')
  humidity = data["main"]["humidity"] 
  print('The humidity is', str(humidity)+'%, bud')


else: 
  print("An error occurred.")

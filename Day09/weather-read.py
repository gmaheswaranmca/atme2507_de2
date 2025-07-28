#https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}
import requests 
city = input('City Name:')
key = '39be8355f4c2b070862ba7ea33d969fa'
url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
response = requests.get(url)
#print(response)
if response.status_code == 200:
    data = response.json()
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}K")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print(f"Error: {response.status_code} - {response.reason}")
    print("Please check the city name and try again.")
import requests
from bs4 import BeautifulSoup

def get_weather(city):
    url = f'https://www.timeanddate.com/weather/{city}'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        weather_container = soup.find('div', class_='h2').text
        temperature = soup.find('div', class_='h1').text.strip()
        
        print(f"Weather in {city}: {weather_container}")
        print(f"Temperature: {temperature}")
    else:
        print("Failed to fetch weather data.")

get_weather('Vietnam/Hanoi')

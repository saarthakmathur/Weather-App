import requests
import os
from dotenv import load_dotenv

API_KEY = "d10c23ca7f40596d86d3caf435f4974e"
# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
params = {"q": city, "appid": API_KEY, "units": "metric"}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    print(f"Weather in {data['name']}, {data['sys']['country']}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Condition: {data['weather'][0]['description'].capitalize()}")
else:
    print("❌ City not found. Please check the name and try again.")

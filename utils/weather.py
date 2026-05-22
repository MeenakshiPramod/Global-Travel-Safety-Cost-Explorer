import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env properly
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

print("Loaded API KEY:", API_KEY)


def get_weather(city):

    try:

        if not API_KEY:
            print("API KEY NOT FOUND")
            return None

        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        response = requests.get(url, timeout=10)

        print("Weather Status:", response.status_code)
        print("Weather Response:", response.text)

        if response.status_code != 200:
            return None

        data = response.json()

        return {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }

    except Exception as e:
        print("Weather Exception:", e)
        return None
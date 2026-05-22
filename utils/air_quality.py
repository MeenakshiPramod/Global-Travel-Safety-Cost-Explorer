import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env properly
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

print("Loaded AQI API KEY:", API_KEY)


def get_air_quality(city):

    try:

        if not API_KEY:
            print("API KEY NOT FOUND")
            return None

        # Get coordinates
        geo_url = (
            f"http://api.openweathermap.org/geo/1.0/direct"
            f"?q={city}&limit=1&appid={API_KEY}"
        )

        geo_response = requests.get(geo_url, timeout=10)

        print("Geo Status:", geo_response.status_code)

        if geo_response.status_code != 200:
            return None

        geo_data = geo_response.json()

        if not geo_data:
            return None

        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]

        # Air Quality
        air_url = (
            f"http://api.openweathermap.org/data/2.5/air_pollution"
            f"?lat={lat}&lon={lon}&appid={API_KEY}"
        )

        air_response = requests.get(air_url, timeout=10)

        print("Air Status:", air_response.status_code)

        if air_response.status_code != 200:
            return None

        air_data = air_response.json()

        aqi = air_data["list"][0]["main"]["aqi"]

        status_map = {
            1: "Good",
            2: "Fair",
            3: "Moderate",
            4: "Poor",
            5: "Very Poor"
        }

        return {
            "aqi": aqi,
            "status": status_map.get(aqi, "Unknown")
        }

    except Exception as e:
        print("AQI Exception:", e)
        return None
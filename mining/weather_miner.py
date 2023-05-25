import requests
import datetime
import random
import json

import airportsdata

class WeatherMiner:
    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key
        self.units = "metric"
        
    def get_weather_event(self, airport_coord_lat, airport_coord_lon, timestamp):
        response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={airport_coord_lat}&lon={airport_coord_lon}&dt={timestamp}&appid={self.api_key}&units={self.units}")
        if response.status_code == 200:
            weather_event_raw = response.json()

            weather_event = {
                "temp": weather_event_raw["data"][0].get("temp"),
                "pressure": weather_event_raw["data"][0].get("pressure"),
                "humidity": weather_event_raw["data"][0].get("humidity"),
                "dew_point": weather_event_raw["data"][0].get("dew_point"),
                "clouds": weather_event_raw["data"][0].get("clouds"),
                "visibility": weather_event_raw["data"][0].get("visibility"),
                "wind_speed": weather_event_raw["data"][0].get("wind_speed"),
                "rainfall_1hr": weather_event_raw["data"][0].get("rain", {}).get("1h"),
                "rainfall_3hr": weather_event_raw["data"][0].get("rain", {}).get("3h"),
                "snowfall_1hr": weather_event_raw["data"][0].get("snow", {}).get("1h"),  
                "snowfall_3hr": weather_event_raw["data"][0].get("snow", {}).get("3h"),  
            }
            return weather_event
        else:
            print("Error: Could not retrieve weather data")
            return {}
    


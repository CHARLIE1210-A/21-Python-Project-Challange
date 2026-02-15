import requests
import logging
import os
from dotenv import load_dotenv

# ================= LOADS .env FILE =================
load_dotenv()

# ================= LOGGING =================
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ================= API KEY =================
API_KEY = os.getenv("WEATHER_API_KEY")
if not API_KEY:
    logger.error("API key for weather service is not set. Please set the WEATHER_API_KEY environment variable.")
    exit(1)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# ================= GET WEATHER  =================
def get_weather(city: str)-> dict:
    """
    Docstring for get_weather
    
    :param city: Description
    :type city: str
    :return: Description
    :rtype: dict
    """
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    response = requests.get(BASE_URL, params=params, timeout=10)
    
    if response.status_code != 200:
        return {"error": f"Failed to get weather data: {response.status_code}"}

    return response.json()

# ================= SHOW WEATHER =================
def show_weather(data: dict) -> None:
    """
    Docstring for show_weather
    
    :param data: Description
    :type data: dict
    """
    if "error" in data:
        logger.error(data["error"])
        
    city = data["name"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    
    logger.info(f"Weather in {city}")
    logger.info(f"Temperature: {temp}°C (Feels like: {feels_like}°C)")
    logger.info(f"Humidity: {humidity}")
    logger.info(f"Condition: {weather}\n")
    
# ================= MAIN =================
def main():
    city = input("Enter city name: ")
    print("\n")
    
    data = get_weather(city)
    show_weather(data)


if __name__ == "__main__":
    main()

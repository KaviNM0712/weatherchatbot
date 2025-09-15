import requests

# Replace with your Tomorrow.io API key
API_KEY = "tlhZDKRmL6aSY7w5YFvmgm95eyBrXYnG"
BASE_URL = "https://api.tomorrow.io/v4/weather/realtime"

# Mapping Tomorrow.io weather codes to human-friendly descriptions
WEATHER_CODES = {
    1000: "Clear, Sunny",
    1100: "Mostly Clear",
    1101: "Partly Cloudy",
    1102: "Mostly Cloudy",
    1001: "Cloudy",
    2000: "Fog",
    2100: "Light Fog",
    4000: "Drizzle",
    4001: "Rain",
    4200: "Light Rain",
    4201: "Heavy Rain",
    5000: "Snow",
    5001: "Flurries",
    5100: "Light Snow",
    5101: "Heavy Snow",
    6000: "Freezing Drizzle",
    6001: "Freezing Rain",
    6200: "Light Freezing Rain",
    6201: "Heavy Freezing Rain",
    7000: "Ice Pellets",
    7101: "Heavy Ice Pellets",
    7102: "Light Ice Pellets",
    8000: "Thunderstorm"
}

def get_weather(city):
    params = {
        'location': city,
        'apikey': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        values = data.get("data", {}).get("values", {})
        temp = values.get("temperature")
        code = values.get("weatherCode")
        weather = WEATHER_CODES.get(code, f"Unknown (code {code})")
        return f"The weather in {city} is {weather} with a temperature of {temp}°C."
    else:
        return "Sorry, I couldn't fetch the weather right now. Please check the city name."

if __name__ == "__main__":
    print("Type 'exit' to quit.")
    while True:
        user_message = input("You: ")
        if user_message.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break
        if "weather" in user_message.lower():
            # Very basic extraction: last word assumed as city
            words = user_message.split()
            city = words[-1]
            reply = get_weather(city)
        else:
            reply = "I can help you with weather info. Ask me about the weather in a city."
        print("Bot:", reply)

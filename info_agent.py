import os
import requests
from openai import OpenAI

client = OpenAI()

def get_weather(location):
    # This function would call an external API to get weather data
    # For the purpose of this example, we'll return a mock response
    return {
        "location": location,
        "temperature": "22°C",
        "description": "Partly cloudy"
    }

def search_web(query):
    api_key = os.getenv("BRAVE_API_KEY")
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": api_key
    }
    params = {
        "q": query
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def fetch_data():
    location = "San Francisco"
    weather_info = get_weather(location)
    print(f"Weather in {location}: {weather_info['temperature']}, {weather_info['description']}")

    query = "latest news in technology"
    search_results = search_web(query)
    print(f"Search results for '{query}':")
    for result in search_results.get("web", {}).get("results", []):
        print(f"- {result['title']}: {result['url']}")

if __name__ == "__main__":
    fetch_data()
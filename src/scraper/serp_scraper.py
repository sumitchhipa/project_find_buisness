import os
import requests

from dotenv import load_dotenv

load_dotenv()

SERP_API_KEY = os.getenv("SERPAPI_KEY")
from src.scraper.serp_scraper import search_businesses

results = search_businesses(
    category="dentist",
    postcode="302001"
)

print(results.keys())




def search_businesses(category, postcode):

    query = f"{category} in {postcode}"

    params = {
        "engine": "google_maps",
        "q": query,
        "api_key": SERP_API_KEY
    }

    response = requests.get(
        "https://serpapi.com/search",
        params=params,
        timeout=60
    )

    response.raise_for_status()

    return response.json()
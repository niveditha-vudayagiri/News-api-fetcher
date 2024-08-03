import os
import requests
from dotenv import find_dotenv, load_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

class APIInteg():
    def fetch_articles(query, start=1):
        api_key = os.getenv('GOOGLE_API_KEY')
        cx = os.getenv('GOOGLE_CX')
        url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}&start={start}'
        response = requests.get(url)
        return response.json()
    
    def fetch_news(query, start=1):
        api_key = os.getenv('NEWS_API_KEY')
        url = f'https://newsapi.org/v2/everything?q=ArtificialIntelligence&from=2024-07-10&sortBy=popularity&apiKey={api_key}'
        response = requests.get(url)
        return response.json()
    
    def headlines(query, start=1):
        api_key = os.getenv('NEWS_API_KEY')
        url=f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={api_key}"
        response = requests.get(url)
        return response.json()
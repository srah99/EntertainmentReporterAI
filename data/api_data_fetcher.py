import requests
import json

def fetch_musicbrainz_data():
    url = "https://musicbrainz.org/ws/2/artist?query=rock&fmt=json"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def fetch_wikipedia_data():
    url = "https://en.wikipedia.org/w/api.php?action=query&titles=Rock_music&prop=extracts&exintro=1&explaintext=1&format=json"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def fetch_news_data():
    url = "https://newsapi.org/v2/everything?q=rock music&apiKey=YOUR_API_KEY"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

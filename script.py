import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit=100&sort=ticker&apiKey={API_KEY}"

if __name__=="__main__": 
    response = requests.get(url)
    if response.status_code != 200:
        raise TimeoutError(f"unable to make the request, status: {response.status_code}")
    
    print(response.json())
    
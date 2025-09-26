import csv
import os
import requests
import time
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
LIMIT = 100

url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={API_KEY}"

def stock_job():
    response = requests.get(url)
    if response.status_code != 200:
        raise TimeoutError(f"unable to make the request, status: {response.status_code}")
    
    tickers: list[dict] = []
    data = response.json()
    
    total_tickers = 0
        
    while "next_url" in data:
        response = requests.get(data["next_url"] + f"&apiKey={API_KEY}")
        data: dict = response.json()
        if "results" in data:
            for ticker in data['results']: 
                tickers.append(ticker)
        
    example_ticker = {
                      'ticker': 'ACI', 
                      'name': 'Albertsons Companies, Inc.', 
                      'market': 'stocks', 
                      'locale': 'us', 
                      'primary_exchange': 'XNYS', 
                      'type': 'CS', 
                      'active': True, 
                      'currency_name': 'usd', 
                      'cik': '0001646972', 
                      'composite_figi': 'BBG009KG1750',
                      'share_class_figi': 'BBG009KG1741', 
                      'last_updated_utc': '2025-09-24T06:06:16.196092144Z'
                      }
    fieldnames = list(example_ticker.keys())
    csv_path = '/home/tiasz/stock_market_api/tickers.csv'
    with open (csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for ticker in tickers:
            row = {key: ticker.get(key, '') for key in fieldnames}
            writer.writerow(row)

    print(f"finished execution at {time.localtime()}")
    
if __name__ == "__main__":
    stock_job()
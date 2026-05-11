import requests
import pandas as pd
import os

from dotenv import load_dotenv

#get key
load_dotenv()
api_key = os.getenv("API_KEY")

url = "https://api.football-data.org/v4/competitions/PD/matches"

headers = {
    "X-Auth-Token": api_key
}

#make & check request
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
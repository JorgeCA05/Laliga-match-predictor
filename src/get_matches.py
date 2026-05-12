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
else:
    print(f"Error: {response.status_code}")


#build list of dictionaries with any relevant matches info
matches_data = []
#data ingestion
for match in data["matches"]:
    match_info = {
        "match_id":     match["id"],
        "date":         match["utcDate"],
        "season_start": match["season"]["startDate"],
        "season_end":   match["season"]["endDate"],
        "matchday":     match["matchday"],
        "home_team":    match["homeTeam"]["shortName"],
        "away_team":    match["awayTeam"]["shortName"],
        "home_goals":   match["score"]["fullTime"]["home"],
        "away_goals":   match["score"]["fullTime"]["away"],
        "winner":       match["score"]["winner"],
        "status":       match["status"]
    }
    matches_data.append(match_info)

#build dataframe
df_matches = pd.DataFrame(matches_data)

#dataframe transformation
df_matches["date"] = pd.to_datetime(df_matches["date"])

df_matches["season"] = (
    df_matches["season_start"].str[:4]
    + "-"
    + df_matches["season_end"].str[:4]
)

df_matches = df_matches.drop(columns=["season_start", "season_end"])

#print(df_matches.head())
#print(df_matches.info())

df_matches.to_csv("data/matches.csv", index=False)
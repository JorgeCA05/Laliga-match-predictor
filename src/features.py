import pandas as pd



#Last 5 matches form for a team, including points, winrate, avg goals scored and conceded
def get_global_form(history, team, window=5):

    matches = history.tail(window)

    points = 0
    goals_scored = 0
    goals_conceded = 0

    for _, m in matches.iterrows():

        if m["home_team"] == team:
            gf = m["home_goals"]
            ga = m["away_goals"]
            result = m["winner"]
            is_win = (result == "HOME_TEAM")

        else:
            gf = m["away_goals"]
            ga = m["home_goals"]
            result = m["winner"]
            is_win = (result == "AWAY_TEAM")

        goals_scored += gf
        goals_conceded += ga

        if result == "DRAW":
            points += 1
        elif is_win:
            points += 3

    n = len(matches)

    return {
        "points_last_5": points,
        "winrate_last_5": points / (n * 3) if n > 0 else 0,
        "avg_goals_scored_last_5": goals_scored / n if n > 0 else 0,
        "avg_goals_conceded_last_5": goals_conceded / n if n > 0 else 0
    }


#General home performance metrics for a team, including home winrate, avg goals scored and conceded at home
def get_home_form(history, team, window=5):

    matches = history[history["home_team"] == team].tail(window)

    points = 0
    goals_scored = 0
    goals_conceded = 0

    for _, m in matches.iterrows():

        gf = m["home_goals"]
        ga = m["away_goals"]

        goals_scored += gf
        goals_conceded += ga

        if m["winner"] == "DRAW":
            points += 1
        elif m["winner"] == "HOME_TEAM":
            points += 3

    n = len(matches)

    return {
        "home_winrate": points / (n * 3) if n > 0 else 0,
        "avg_home_goals": goals_scored / n if n > 0 else 0,
        "avg_home_goals_conceded": goals_conceded / n if n > 0 else 0
    }


#General away performance metrics for a team, including away winrate, avg goals scored and conceded away
def get_away_form(history, team, window=5):

    matches = history[history["away_team"] == team].tail(window)

    points = 0
    goals_scored = 0
    goals_conceded = 0

    for _, m in matches.iterrows():

        gf = m["away_goals"]
        ga = m["home_goals"]

        goals_scored += gf
        goals_conceded += ga

        if m["winner"] == "DRAW":
            points += 1
        elif m["winner"] == "AWAY_TEAM":
            points += 3

    n = len(matches)

    return {
        "away_winrate": points / (n * 3) if n > 0 else 0,
        "avg_away_goals": goals_scored / n if n > 0 else 0,
        "avg_away_goals_conceded": goals_conceded / n if n > 0 else 0
    }


#Dataset builder for ML, using the above functions
def build_dataset(df, window=5):

    df = df.sort_values("date").reset_index(drop=True)

    dataset = []

    for i in range(len(df)):

        match = df.iloc[i]
        history = df.iloc[:i]

        home = match["home_team"]
        away = match["away_team"]

        home_global = get_global_form(history, home, window)
        away_global = get_global_form(history, away, window)

        home_home = get_home_form(history, home, window)
        away_away = get_away_form(history, away, window)

        row = {
            "match_id": match["match_id"],
            "date": match["date"],
            "home_team": home,
            "away_team": away,
            "target": match["winner"]
        }

        for k, v in home_global.items():
            row["home_" + k] = v

        for k, v in away_global.items():
            row["away_" + k] = v

        row.update(home_home)
        row.update(away_away)

        dataset.append(row)

    return pd.DataFrame(dataset)
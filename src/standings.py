import pandas as pd

def build_standings(df):
    # Get unique teams
    teams = pd.unique(df[["home_team", "away_team"]].values.ravel())

    rows = []

    # Build standings row by row
    for team in teams:
        home_matches = df[df["home_team"] == team]
        away_matches = df[df["away_team"] == team]

        matches_played = len(home_matches) + len(away_matches)

        wins = (
            len(home_matches[home_matches["winner"] == "HOME_TEAM"]) +
            len(away_matches[away_matches["winner"] == "AWAY_TEAM"])
        )

        draws = (
            len(home_matches[home_matches["winner"] == "DRAW"]) +
            len(away_matches[away_matches["winner"] == "DRAW"])
        )

        losses = matches_played - wins - draws

        goals_for = (
            home_matches["home_goals"].sum() +
            away_matches["away_goals"].sum()
        )

        goals_against = (
            home_matches["away_goals"].sum() +
            away_matches["home_goals"].sum()
        )

        goal_difference = goals_for - goals_against
        points = wins * 3 + draws

        rows.append({
            "team": team,
            "matches_played": matches_played,
            "wins": wins,
            "draws": draws,
            "losses": losses,
            "goals_for": goals_for,
            "goals_against": goals_against,
            "goal_difference": goal_difference,
            "points": points
        })

    standings = pd.DataFrame(rows)

    # Sort standings
    standings = standings.sort_values(
        by=["points", "goal_difference", "goals_for"],
        ascending=False
    ).reset_index(drop=True)

    return standings
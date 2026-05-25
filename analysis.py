import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import leaguedashplayerstats
import time

# Fetch 2024-25 season player stats
print("Fetching NBA data...")
time.sleep(1)

stats = leaguedashplayerstats.LeagueDashPlayerStats(
    season='2024-25',
    per_mode_detailed='PerGame'
)

df = stats.get_data_frames()[0]

# Keep only useful columns
df = df[['PLAYER_NAME', 'TEAM_ABBREVIATION', 'GP', 'PTS', 'REB', 'AST', 'FG_PCT', 'FG3_PCT', 'MIN']]

# Filter to players with at least 20 games played
df = df[df['GP'] >= 20]

# Sort by points per game
df = df.sort_values('PTS', ascending=False)

# Print top 20 scorers
print("\nTop 20 Scorers (2024-25 Season)")
print(df.head(20).to_string(index=False))

# Plot top 20 scorers
top20 = df.head(20)

plt.figure(figsize=(12, 7))
plt.barh(top20['PLAYER_NAME'], top20['PTS'], color='royalblue')
plt.xlabel('Points Per Game')
plt.title('NBA Top 20 Scorers – 2024-25 Season')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('top_scorers.png')
plt.show()

print("\nChart saved as top_scorers.png")
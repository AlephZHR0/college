import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Load data from CSV files
lobby_stats_df = pd.read_csv("tb_lobby_stats_player.csv")
players_df = pd.read_csv("tb_players.csv")

# Set Pandas options to display all columns
pd.set_option('display.max_columns', None)

# Drop columns that won't be used
lobby_stats_df = lobby_stats_df.drop(["qtPlusKill", "qtTrade","idLobbyGame", "idRoom", "qtBombeDefuse", "qtBombePlant", "qtLastAlive", "qtClutchWon", "descMapName", "qtSurvived", "flWinner"], axis=1)
players_df = players_df.drop(["flFacebook", "flTwitter", "flTwitch"], axis=1)

# Remove rows with missing data
players_df = players_df.dropna(subset=["dtBirth"])
lobby_stats_df = lobby_stats_df.dropna(subset=["qtHitHeadshot"])

# Merge dataframes
merged_df = pd.merge(lobby_stats_df, players_df, on='idPlayer', how='inner')

# Understand the data:
merged_df[merged_df["qtHs"] > merged_df["qtKill"]][["qtKill", "qtHs"]] # the hs kills is separated from the kills
merged_df[merged_df["qtTk"] > merged_df["qtKill"]][["qtTk", "qtKill", "qtAssist", "vlDamage"]] # the tk is separated from the kills
merged_df[merged_df["qtTkAssist"] > merged_df["qtAssist"]][["qtTkAssist", "qtAssist"]] # the tk assist is separated from the assist
merged_df[merged_df["qtFlashAssist"] > merged_df["qtAssist"]][["qtFlashAssist", "qtAssist"]] # the flash assist is separated from the assist

# Create new columns
merged_df["dtCreatedAt"] = pd.to_datetime(merged_df["dtCreatedAt"])
merged_df["dtBirth"] = pd.to_datetime(merged_df["dtBirth"])
merged_df["age"] = (merged_df["dtCreatedAt"] - merged_df["dtBirth"]).dt.days // 365

merged_df["global_acuracy"] = merged_df["qtHits"] / merged_df["qtShots"]
merged_df["head_acuracy"] = merged_df["qtHitHeadshot"] / merged_df["qtShots"]
merged_df["mid_body_acuracy"] = (merged_df["qtHitChest"] + merged_df["qtHitStomach"] + merged_df["qtHitLeftAtm"] + merged_df["qtHitRightArm"]) / merged_df["qtShots"]
merged_df["lower_body_acuracy"] = (merged_df["qtHitLeftLeg"] + merged_df["qtHitRightLeg"]) / merged_df["qtShots"]
merged_df["kills"] = merged_df["qt1Kill"] + 2* merged_df["qt2Kill"] + 3* merged_df["qt3Kill"] + 4* merged_df["qt4Kill"] + 5* merged_df["qt5Kill"]
# Map state abbreviations to country names
uf_to_country = {
 "descCountry": ["br", "ar", "cl", "uy", "us", "py", "ca", "pe", "bo"],
 "Country": ["Brasil", "Argentina", "Chile", "Uruguai", "Estados Unidos", "Paraguai", "Canadá", "Peru", "Bolívia"]
}
countries = pd.DataFrame(uf_to_country)
merged_df = pd.merge(merged_df, countries, on='descCountry', how='inner')

# Create line plots for all accuracies
sns.lineplot(x="vlLevel", y="global_acuracy", data=merged_df, color='blue', label='Global')
sns.lineplot(x="vlLevel", y="head_acuracy", data=merged_df, color='orange', label='Head')
sns.lineplot(x="vlLevel", y="mid_body_acuracy", data=merged_df, color='green', label='Mid-Body')
sns.lineplot(x="vlLevel", y="lower_body_acuracy", data=merged_df, color='red', label='Lower-Body')

# Set the plot title and axis labels
plt.title('Level vs Precision by Body Part')
plt.xlabel('Level')
plt.ylabel('Precision')
plt.show()

# Create line plots for all strikes
sns.lineplot(x="vlLevel", y="qt1Kill", data=merged_df, color='blue', label='Single Kill')
sns.lineplot(x="vlLevel", y="qt2Kill", data=merged_df, color='orange', label='Double Kill')
sns.lineplot(x="vlLevel", y="qt3Kill", data=merged_df, color='green', label='Triple Kill')
sns.lineplot(x="vlLevel", y="qt4Kill", data=merged_df, color='red', label='Quadra Kill')
sns.lineplot(x="vlLevel", y="qt5Kill", data=merged_df, color='purple', label='Penta Kill')

# Set the plot title and axis labels
plt.title('Level impact on kill Streak')
plt.xlabel('Level')
plt.ylabel('Streak')
plt.show()

# Create a density heatmap of player performance by level
colors = mcolors.LinearSegmentedColormap.from_list("", ["#FFC300", "#FF5733", "#C70039", "#900C3F", "#581845"])
for i in range(merged_df["vlLevel"].max() + 1):
    sns.lineplot(x="qtDeath", y="kills", data=merged_df[merged_df["vlLevel"]  == i], color=colors(i/merged_df["vlLevel"].max()), label=f'lvl {i}')
    plt.xlim(0, 50)
plt.title('KD by Level')
plt.xlabel('Deaths')
plt.ylabel('Kills')
plt.show()

# Plot mean rounds played by level
mean_rounds_played = merged_df.groupby('vlLevel')['qtRoundsPlayed'].mean()
sns.lineplot(x=mean_rounds_played.index, y=mean_rounds_played.values, color='blue')

# Set the plot title and axis labels
plt.title('Mean Rounds Played by Level')
plt.xlabel('Level')
plt.ylabel('Mean Rounds Played')
plt.show()

# Create line plot of mean("age") x "vlLevel"
mean_age = merged_df.groupby('vlLevel')['age'].mean()
sns.lineplot(x=mean_age.index, y=mean_age.values, color='blue')

# Set the plot title and axis labels
plt.title('Mean Age by Level')
plt.xlabel('Level')
plt.ylabel('Mean Age')
plt.show()

# Calculate kill-death ratio
merged_df['kd_ratio'] = merged_df['qtKill'] / merged_df['qtDeath']

# Group ages into 10-year intervals
merged_df['age_group'] = pd.cut(merged_df['age'], bins=range(0, 101, 10), right=False)

# Create scatter plot of kd_ratio vs age, with different colors for each age group
sns.scatterplot(data=merged_df, x='age', y='kd_ratio', hue='age_group', palette='viridis')

# Set the plot title and axis labels
plt.title('Kill-Death Ratio vs Age')
plt.xlabel('Age')
plt.ylabel('Kill-Death Ratio')
plt.show()

# Create a density heatmap of player performance by country and level
sns.kdeplot(data=merged_df, x='vlLevel', y='qtKill', hue='Country', fill=True, cmap='coolwarm', alpha=.5, n_jobs=-1)

# Set the plot title and axis labels
plt.title('Player Performance by Country and Level')
plt.xlabel('Level')
plt.ylabel('Kills')
plt.show()
I obtained all the data for the analysis from the following site

[Brazilian CS:GO Platform Dataset by Gamers Club](https://www.kaggle.com/datasets/gamersclub/brazilian-csgo-plataform-dataset-by-gamers-club/discussion/308279)

# Notes about the data used in this analysis
I didn't use the "tb_medalha.csv" and the "tb_players_medalha.csv" files because during my conversations with some players to better understand the data, they told me that the medals are not important for the analysis. Therefore, I decided to exclude them from my analysis.

# Objectives of the analysis
The objective of this analysis is to understand the relationship between the player statistics and the player's age, country, and level. The analysis will help us understand the following questions:
1. How the level of the player affects the precision by body part?
2. How much the level of the player impact on kill streaks?
3. What happens with kills and deaths per level?
4. How much rounds it takes per level? (mean)
5. how is the age distribution per level? (mean)
6. How does the KD ratio change per age?
How the performance is distributed per country and level?

# Code description
This code is performing data cleaning, merging, and visualization on two dataframes: lobby_stats_df and players_df. It drops unnecessary columns, removes rows with missing data, creates new columns, and merges the dataframes. It then creates various line plots, scatter plots, and density heatmaps to visualize the data. The plots show the relationship between various player statistics as described earlier on the [Objectives of the analysis](#objectives-of-the-analysis) section.

# Results
The results of the analysis are available in the following images:

- [KD by Level](Results/KD_by_Level.png)

- [Kill-Death Ratio vs Age](Results/Kill-Death_Ratio_vs_Age.png)

- [Level impact on kill Streak](Results/Level_impact_on_kill_Streak.png)

- [Level vs Precision by Body Part](Results/Level_vs_Precision_by_Body_Part.png)

- [Mean Age by Level](Results/Mean_Age_by_Level.png)

- [Mean Rounds Played by Level](Results/Mean_Rounds_Played_by_Level.png)

- [Player Performance by Country and Level](Results/Player_Performance_by_Country_and_Level.png)
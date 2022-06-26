import pandas as pd

your_csv_website = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')

print(your_csv_website)

# Rename Columns --> from Div to Divisions

your_csv_website.rename(columns={'Div': 'Divisons'}, inplace=True)

print(your_csv_website)
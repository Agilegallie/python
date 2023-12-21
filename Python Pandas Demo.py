import pandas as pd

# File paths for the two CSV files
weather_data_path = r"C:\weather.csv"
thunderball_data_path = r"C:\thunderball-draw-history.csv"

# Read the data from the CSV files into separate DataFrames
df_weather = pd.read_csv(weather_data_path)
df_thunderball = pd.read_csv(thunderball_data_path)

# Perform an inner merge on the "Month" column to combine the weather data with thunderball data
combined_df = pd.merge(df_thunderball, df_weather, on='Month', how='inner')

# Export the combined DataFrame to a new CSV file in the same folder
output_path = r"C:\combined_data.csv"
combined_df.to_csv(output_path, index=False)

print("Data has been exported to:", output_path)

# Code written by Brett Gallie and ChatGPT
# Code run using Anaconda Jupyter Notebook
# Public data from UK Weather and lotto sources
# Created for entertainment and illustrative purposes only
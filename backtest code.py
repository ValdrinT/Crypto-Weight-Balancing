import pandas as pd

# List to store DataFrames for each month
monthly_data_dfs = []

# List of CSV file names
csv_files = [
    "bnb_updated.csv",
    "BTC_All_graph_coinmarketcap.csv",
    "CRO_All_graph_coinmarketcap.csv",
    "ETH_All_graph_coinmarketcap.csv",
    "ICP_All_graph_coinmarketcap.csv",
    "LDO_All_graph_coinmarketcap.csv",
    "MATIC_All_graph_coinmarketcap.csv",
    "RUNE_All_graph_coinmarketcap.csv",
    "SAND_All_graph_coinmarketcap.csv",
    "UNI_All_graph_coinmarketcap.csv"
]

# Iterate over each CSV file
for csv_file in csv_files:
    # Read CSV file
    df = pd.read_csv(fr"C:\Users\valdr\OneDrive\Desktop\backtest\{csv_file}", sep=";", parse_dates=["timestamp"])

    # Convert timestamp to date
    df["timestamp"] = pd.to_datetime(df["timestamp"]).dt.date

    # Set timestamp as index
    df.set_index('timestamp', inplace=True)
    df.index = pd.to_datetime(df.index)

    # Calculate moving average
    df["MA"] = df["close"].rolling(window=3).mean()

    # Resample to weekly
    df_weekly = df.resample("W").mean()

    # Forward fill missing values
    df_weekly['close'].fillna(df_weekly['close'].ffill(), inplace=True)
    df_weekly['marketCap'].fillna(df_weekly['marketCap'].ffill(), inplace=True)

    # Calculate 12-week moving average
    df_weekly["12_week_MA"] = df_weekly["close"].rolling(window=12).mean()

    # Set index to date and rename index
    df_weekly.index = pd.to_datetime(df_weekly.index)  # Ensure datetime index
    df_weekly.index.name = "timestamp"

    # Save weekly data to CSV with corresponding file name
    df_weekly.to_csv(fr"C:\Users\valdr\OneDrive\Desktop\backtest\{csv_file}_Weekly.csv", sep=';', date_format='%Y-%m-%d')

    # Extract 12_week_MA and marketCap for the first week of each month
    first_week_data = df_weekly.resample('MS').first()[['12_week_MA', 'marketCap']]

    # Filter data from 2021-08-01 onwards
    first_week_data = first_week_data[first_week_data.index >= pd.to_datetime("2021-08-01")]

    # Extract ticker symbol from file name
    ticker = csv_file.split('_')[0]

    # Add it as a column header
    first_week_data.columns = [f"{ticker}_12_week_MA", f"{ticker}_marketCap"]

    # Add it to the list
    monthly_data_dfs.append(first_week_data)

# Concatenate all DataFrames
result_df = pd.concat(monthly_data_dfs, axis=1)

# Save the result to a CSV file
result_df.to_csv(fr"C:\Users\valdr\OneDrive\Desktop\backtest\Monthly_Data.csv", sep=';', date_format='%Y-%m-%d')


# Read the CSV file containing the data
result_df = pd.read_csv(fr"C:\Users\valdr\OneDrive\Desktop\backtest\Monthly_Data.csv", sep=';', parse_dates=["timestamp"])

# Set timestamp as index
result_df.set_index('timestamp', inplace=True)
result_df.index = pd.to_datetime(result_df.index)

# Extract the columns containing the asset prices (ticker_12_week_MA)
price_columns = [col for col in result_df.columns if '_12_week_MA' in col]

# Replace 0 values with NaN
result_df[price_columns] = result_df[price_columns].replace(0, float('nan'))

# Drop rows with NaN values in the price columns
result_df.dropna(subset=price_columns, inplace=True)

# Create a new DataFrame to store the summed prices
weekly_sum_df = pd.DataFrame(columns=['Week', 'Total_Price'])

# Iterate over each month and extract the first week's data
for month, group in result_df.groupby(pd.Grouper(freq='MS')):
    # Extract data for the first week of the month
    first_week_data = group.head(1)
    # Sum all the prices for the first week of the month
    total_price = first_week_data[price_columns].sum().sum()
    # Append the total price to the DataFrame
    weekly_sum_df = weekly_sum_df.append({'Week': first_week_data.index[0], 'Total_Price': total_price}, ignore_index=True)

# Save the result to a CSV file
weekly_sum_df.to_csv(fr"C:\Users\valdr\OneDrive\Desktop\backtest\Weekly_Sum_Price.csv", sep=';', index=False)

import pandas as pd

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

    # Calculate 12-week moving average
    df_weekly["12_week_MA"] = df_weekly["close"].rolling(window=12).mean()

    # Set index to date and rename index
    df_weekly.index = df_weekly.index.date
    df_weekly.index.name = "timestamp"

    # Save weekly data to CSV with corresponding file name
    df_weekly.to_csv(fr"C:\Users\valdr\OneDrive\Desktop\backtest\{csv_file}_Weekly.csv", sep=';', date_format='%Y-%m-%d')

    # Save original data to CSV
    df.to_csv(fr"C:\Users\valdr\OneDrive\Desktop\backtest\{csv_file}", sep=";", date_format='%Y-%m-%d')

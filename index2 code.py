import csv

crypto_portfolio = {
    'Render (RNDR)': {'percentage': 20.96, 'market_cap': 1500},
    'Axie Infinity (AXS)': {'percentage': 14.95, 'market_cap': 1070},
    'The Sandbox (SAND)': {'percentage': 14.53, 'market_cap': 1040},
    'Decentraland (MANA)': {'percentage': 12.58, 'market_cap': 900},
    'Gala (GALA)': {'percentage': 10.86, 'market_cap': 777},
    'Illuvium (ILV)': {'percentage': 7.22, 'market_cap': 517},
    'Apecoin (APE)': {'percentage': 7.22, 'market_cap': 517},
    'Enjin Coin (ENJ)': {'percentage': 5.74, 'market_cap': 411},
    'Treasure (MAGIC)': {'percentage': 3.90, 'market_cap': 279},
    'Vulcan Forged (PYR)': {'percentage': 2.04, 'market_cap': 146},
}

# Clean the data
redistributed_crypto_list = []
for asset, data in crypto_portfolio.items():
    percentage = data.pop("percentage")
    market_cap = data.pop("market_cap")
    redistributed_crypto_list.append({'Asset': asset, 'Percentage': percentage, 'Market_Cap': market_cap})

# Make a copy of the original list for redistribution
original_cryptos = [crypto.copy() for crypto in redistributed_crypto_list]

# Calculate rebalancing
top_5_pct = sum(crypto['Percentage'] for crypto in redistributed_crypto_list[:5])
scaling_factor = 80 / top_5_pct

if top_5_pct > 80:
    for crypto in redistributed_crypto_list[:5]:
        crypto["Percentage"] *= scaling_factor

    excess_pct = top_5_pct - 80
    for crypto in redistributed_crypto_list[5:]:
        weight = crypto["Percentage"] / (100 - top_5_pct)
        crypto["Percentage"] -= (excess_pct / 5) * weight

# Check if the original and redistributed lists are the same
lists_are_same = original_cryptos == redistributed_crypto_list

# Print the original and redistributed crypto lists only if they are different
if not lists_are_same:
    print("Original Crypto List:")
    for crypto in original_cryptos:
        print(f"{crypto['Asset']}\t{crypto['Percentage']:.2f}%")

print("\nRedistributed Crypto List:")
for crypto in redistributed_crypto_list:
    print(f"{crypto['Asset']}\t{crypto['Percentage']:.2f}%")

# Write to CSV only if the lists are different
csv_file_path = r"C:\Users\valdr\Downloads\index2.csv"
with open(csv_file_path, 'w', newline='') as csv_file:
    fieldnames = ['Asset', 'Percentage', 'Market_Cap']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the original or redistributed data based on the condition
    if not lists_are_same:
        for crypto in original_cryptos:
            crypto['Percentage'] = "{:.2f}%".format(float(crypto['Percentage']))
            writer.writerow(crypto)
    else:
        for crypto in redistributed_crypto_list:
            crypto['Percentage'] = "{:.2f}%".format(float(crypto['Percentage']))
            writer.writerow(crypto)
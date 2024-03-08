import csv

cryptos = [
    {"Asset": "Bitcoin (BTC)", "Percentage": 68.47, "Market Capitalization in billions": 802.36},
    {"Asset": "Ethereum (ETH)", "Percentage": 25.37, "Market Capitalization in billions": 297.26},
    {"Asset": "Binance Coin (BNB)", "Percentage": 4.10, "Market Capitalization in billions": 48.09},
    {"Asset": "Uniswap (UNI)", "Percentage": 0.40, "Market Capitalization in billions": 4.74},
    {"Asset": "Cronos (CRO)", "Percentage": 0.18, "Market Capitalization in billions": 2.16},
    {"Asset": "Lido Dao (LDO)", "Percentage": 0.23, "Market Capitalization in billions": 2.68},
    {"Asset": "The Sandbox (SAND)", "Percentage": 0.09, "Market Capitalization in billions": 1},
    {"Asset": "Internet Computer (ICP)", "Percentage": 0.43, "Market Capitalization in billions": 5.02},
    {"Asset": "Polygon (MATIC)", "Percentage": 0.62, "Market Capitalization in billions": 7.25},
    {"Asset": "THORChain (RUNE)", "Percentage": 0.11, "Market Capitalization in billions": 1.24},
]
# Create a copy of the original cryptos list
original_cryptos = [crypto.copy() for crypto in cryptos]

# Total percentage of all cryptos minus ETH and BTC
total_percentage_minus_btc_eth = sum(asset["Percentage"] for asset in cryptos[2:])

# Calculate if BTC is over 65. If so, make it 65.
btc_percentage = cryptos[0]["Percentage"]
if btc_percentage > 65:
    excess_btc = btc_percentage - 65
    cryptos[0]["Percentage"] = 65

# Calculate if ETH is over 25. If so, make it 25
eth_percentage = cryptos[1]["Percentage"]
if eth_percentage > 25:
    excess_eth = eth_percentage - 25
    cryptos[1]["Percentage"] = 25

excess_percentage = excess_btc + excess_eth


# Calculate and add redistribution percentage
for crypto in cryptos[2:]:
    crypto_weight = crypto["Percentage"] / total_percentage_minus_btc_eth
    redistribution_amount = excess_percentage * crypto_weight
    crypto["Percentage"] += redistribution_amount

redistributed_crypto_list = []
for crypto in cryptos:
    redistributed_crypto_list.append({
        "Asset": crypto["Asset"],
        "Percentage": crypto["Percentage"],
        "Market Capitalization in billions": crypto["Market Capitalization in billions"]
    })

# Print both original and redistributed crypto lists
print("Original Crypto List:")
for crypto in original_cryptos:
    print(f"{crypto['Asset']}\t{crypto['Percentage']:.2f}%")

print("\nRedistributed Crypto List:")
for crypto in redistributed_crypto_list:
    print(f"{crypto['Asset']}\t{crypto['Percentage']:.2f}%")

# Write to CSV
csv_file_path = r"C:\Users\valdr\Downloads\crypto_data.csv"
with open(csv_file_path, 'w', newline='') as csv_file:
    fieldnames = ['Asset', 'Percentage', 'Market Capitalization in billions']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the headers
    writer.writeheader()

    # Write the original data
    writer.writerows(original_cryptos)

    # Write a separator
    writer.writerow({})

    # Write the redistributed data
    for crypto in redistributed_crypto_list:
        # Format percentage to two decimal places
        crypto['Percentage'] = "{:.2f}%".format(float(crypto['Percentage']))
        writer.writerow(crypto)
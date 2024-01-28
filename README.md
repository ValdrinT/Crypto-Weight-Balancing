I'm creating a custom index that the largest cryptocurrencies from the most important categories.	


The eligibility criteria will be as follows:
Eligibility Criteria:

● Assets that are not index tokens, stablecoins or pegged to another asset.

● Are not deemed a security or banned by a financial regulatory authority.

● Can be deposited and withdrawn from at least three exchanges.

● Have a daily trading volume exceeding 10 million.

● Have at least six months of historical price data.

● Have a market capitalization higher than $700,000 million.

● Trade against a G10 currency.


The second index will include only metaverse tokens. The eligibility criteria will be as follows: 

Eligibility Criteria:

● Assets that are not index tokens, stablecoins or pegged to another asset.

● Are not deemed a security or banned by a financial regulatory authority.

● Can be deposited and withdrawn from at least three exchanges.

● Have a daily trading volume exceeding 2 million.

● Have at least six months of historical price data.

● Have a market capitalization higher than $100,000 million.

● Trade against a G10 currency.

● Are not “Meme coins”.



Both indexes will be weighed based on the market capitalization and rebalanced monthly. 

The next steps in the code will be to parse the data from coinmarketcap and coingecko so I won't have to input the market cap values automatically. Also, to add a rolling moving average of the past 30-days for the market capitalization, in order to remove the possibility that the market cap might increase/decrease more than expected in the day of the rebalancing. 

I'm creating a custom index that the largest cryptocurrencies from the most important categories. The eligibility criteria will be as follows:
Eligibility Criteria:
● Assets that are not index tokens, stablecoins or pegged to another asset.
● Are not deemed a security or banned by a financial regulatory authority.
● Can be deposited and withdrawn from at least three exchanges.
● Have a daily trading volume exceeding 10 million.
● Have at least six months of historical price data.
● Have a market capitalization higher than $700,000 million.
● Trade against a G10 currency.
Assets:
Bitcoin (BTC) : Market Capitalization $802,359 billion.
Layer 1 : Ethereum (ETH) -Market Capitalization $297,263 billion.
Smart Contracts : BNB - Market Capitalization $48,091 billion
DeFi : Uniswap (UNI) - Market Capitalization $4,741 billion
Centralized Exchanges : Cronos (CRO) - Market Capitalization of $2,160 billion (LEO and OKB
have higher MC but not enough volume)
Liquid Staking : Lido Dao (LDO) - Market capitalization $2,683 billion
NFT : The Sandbox (SAND) - Market Capitalization $1 billion
Governance : Internet Computer (ICP) - Market Capitalization $5,020 billion
Layer 2 : Polygon (MATIC) - Market Capitalization $7,248 billion
Decentralized Exchange THORChain (RUNE) - Market Capitalization of $1,235 billion

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
The assets selected are:
Render Token (RNDR):
● Facilitates rendering and streaming of virtual works.
● Distributed rendering on a peer-to-peer network.
● Aims to evolve into digital rights management and a decentralized
marketplace.
Axie Infinity (AXS):
● Game universe with collectible characters called Axies.
● Player-owned economy with NFT representation of in-game items.
The Sandbox (SAND):
● Virtual world enabling players to build, own, and monetize gaming
experiences.
● Main utility token: SAND.
● Decentralized platform through DAOs and NFTs.
Decentraland (MANA):
● Virtual reality platform for content creation, experience, and monetization.
● Users own virtual land on a blockchain ledger.
Gala (GALA):
● Play-to-earn game development company.
● In-game items represented as NFTs for trading on secondary markets.
Apecoin (APE):
● Governance and utility token within the APE ecosystem.
● Supports the evolution of art, gaming, entertainment, and web3.
Iluvium (ILV)
● Merges online gaming with cryptocurrencies
● Create NFTs that are playable in their play-to-earn games.
Enjin Coin (ENJ):
● Technology company for building gaming communities.
● Offers products for creating, managing, trading, and integrating
blockchain-based assets.
Treasure (MAGIC)
● Decentralized NFT ecosystem that sits on Arbitrum (ARB)
● Utility token that connects gaming communities in the Treasure Metaverse
Vulcan Forged (PYR):
● Creator of VulcanVerse, an open-world MMORPG.
● Ecosystem powered by the native token PYR.
● Operates an NFT gaming studio and marketplace.
● Supports blockchain game creation through incubation and crowdfunding


Both indexes will be weighed based on the market capitalization and rebalanced monthly. 

The next steps in the code will be to parse the data from coinmarketcap and coingecko so I won't have to input the market cap values automatically. Also, to add a rolling moving average of the past 30-days for the market capitalization, in order to remove the possibility that the market cap might increase/decrease more than expected in the day of the rebalancing. 

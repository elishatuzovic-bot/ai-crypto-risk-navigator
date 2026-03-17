import requests

def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    data = requests.get(url).json()
    return data["ethereum"]["usd"]

def get_fx_rate():
    url = "https://open.er-api.com/v6/latest/USD"
    data = requests.get(url).json()
    return data["rates"]["CAD"]

def explain_topic(topic, eth_price, usd_cad):
    topic = topic.lower()

    if topic == "eth staking":
        return f"""
Topic: ETH Staking

Live ETH Price: ${eth_price} USD
Live USD/CAD Rate: {usd_cad}

Overview:
ETH staking lets holders earn yield by helping secure the Ethereum network.

Key Risks:
- Validator or protocol risk
- Smart contract risk if using liquid staking platforms
- Liquidity lockup or withdrawal delays
- ETH price volatility

Why it matters:
Staking can generate passive yield, but returns may be outweighed by token price declines or platform-specific risks.
"""
    elif topic == "stablecoin remittance":
        return f"""
Topic: Stablecoin Remittance

Live ETH Price: ${eth_price} USD
Live USD/CAD Rate: {usd_cad}

Overview:
Stablecoins can be used to transfer value across borders faster and more cheaply than traditional payment rails.

Key Risks:
- Stablecoin depegging risk
- On/off-ramp friction
- Wallet/security risk
- Regulatory uncertainty

Why it matters:
This connects to on-chain FX and cross-border payments by reducing intermediaries and potentially lowering remittance costs.
"""
    elif topic == "liquidity pools":
        return f"""
Topic: Liquidity Pools

Live ETH Price: ${eth_price} USD
Live USD/CAD Rate: {usd_cad}

Overview:
Liquidity pools allow users to deposit crypto assets into decentralized exchanges to facilitate trading.

Key Risks:
- Impermanent loss
- Smart contract vulnerabilities
- Token volatility
- Platform risk

Why it matters:
Liquidity pools power much of DeFi trading and on-chain FX, but returns should always be weighed against loss risk.
"""
    else:
        return f"""
Topic not recognized.

Try one of these:
- ETH staking
- stablecoin remittance
- liquidity pools
"""

def main():
    print("AI Crypto Risk Navigator")
    print("------------------------")

    eth_price = get_eth_price()
    usd_cad = get_fx_rate()

    topic = input("Enter a topic (ETH staking, stablecoin remittance, liquidity pools): ")
    result = explain_topic(topic, eth_price, usd_cad)
    print(result)

if __name__ == "__main__":
    main()

import requests
import json

# Завантажуємо список криптовалют з portfolio.json
def load_portfolio():
    try:
        with open("portfolio.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Отримуємо актуальні ціни криптовалют з CoinGecko API
def get_prices(crypto_list):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": ",".join(crypto_list), "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    return response.json()

# Розраховуємо загальну вартість портфеля
def calculate_portfolio(portfolio, prices):
    total_value = 0
    for coin, amount in portfolio.items():
        price = prices.get(coin, {}).get("usd", 0)
        value = amount * price
        print(f"{coin.upper()}: {amount} x ${price:.2f} = ${value:.2f}")
        total_value += value
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

if __name__ == "__main__":
    portfolio = load_portfolio()
    if not portfolio:
        print("⚠️ Portfolio is empty! Add some coins in portfolio.json")
    else:
        print("Fetching prices...")
        prices = get_prices(portfolio.keys())
        calculate_portfolio(portfolio, prices)

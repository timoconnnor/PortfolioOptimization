import requests
import pandas as pd

def fetch_closing_prices(symbol):
    api_key = 'R5611881OCLUIZDG'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=full'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        closing_prices = []
        dates = []

        for date, values in data['Time Series (Daily)'].items():
            dates.append(date)
            closing_prices.append(float(values['4. close']))

        df_closing_prices = pd.DataFrame({'Date': pd.to_datetime(dates), 'Close': closing_prices})
        
        # Check for missing values
        missing_values = df_closing_prices.isnull().sum()
        print("Missing values:\n", missing_values)

        # Handle missing values (if any)
        df_closing_prices.fillna(df_closing_prices.mean(), inplace=True)

        return df_closing_prices
    else:
        print(f"Failed to retrieve data: {response.status_code}")

# Test the function
if __name__ == "__main__":
    symbol = input("Enter stock symbol: ")
    closing_prices = fetch_closing_prices(symbol)
    print(closing_prices)


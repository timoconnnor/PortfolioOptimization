import requests
import json

api_key = 'R5611881OCLUIZDG'
symbol = 'AAPL'

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=full'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # Pretty print JSON response with indentation
    formatted_data = json.dumps(data, indent=4)
    print(formatted_data)
else:
    print(f"Failed to retrieve data: {response.status_code}")

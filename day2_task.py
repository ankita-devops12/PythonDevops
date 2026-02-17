from http.client import responses

import requests
import json

# random_joke= "https://official-joke-api.appspot.com/random_joke"
# response= requests.get(url=random_joke)
# print(response.json()["setup"] + response.json()["punchline"])

api_key = "PQCM6TG8ACC2MVA7"
stock_market_url = "https://www.alphavantage.co/"

def get_stock_market_data(symbol, is_timeseries):
    if is_timeseries:
        query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    else:
        query = f"query?symbol={symbol}&apikey={api_key}"
    response = requests.get(url=stock_market_url + query)
    for key, value in response.json().items():
        if is_timeseries:

            print(key, value)
            with open('output_data.json','w') as json_file:
                json.dump(response.json(), json_file, indent=4)
            print("data successfully print in the file")
        else:
            print("data not print on the file")

symbol = input("Enter the Symbol you want for the Stock Market API eg. (AMZN, GOGL, IBM, etc)")
is_timeseries = True
get_stock_market_data(symbol, is_timeseries)
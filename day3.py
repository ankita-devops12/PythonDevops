from http.client import responses
from os import write

import requests
import json

# random_joke= "https://official-joke-api.appspot.com/random_joke"
# response= requests.get(url=random_joke)
# print(response.json()["setup"] + response.json()["punchline"])

api_key = "PQCM6TG8ACC2MVA7"
stock_market_url = "https://www.alphavantage.co/"
def get_stock_market_data(symbol, is_timeseries):
    try:
        if is_timeseries:
            query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
        else:
            query = f"query?symbol={symbol}&apikey={api_key}"
        #API Request
        response = requests.get(url=stock_market_url+query)
        response.raise_for_status() #Handles HTTP errors
        data = response.json()
        print(data)
    except ValueError:
        print("Invalid Json response from API")
        return
    if "Error Message" in data:
        print("Invalid stock symbol entered")
        return
    if "Note" in data:
        print("API limit reached. Please try after some time.")
        return

    #write data
    try:
        with open('output_data2.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("data successfully print in the file")
    except FileNotFoundError:
        print("file not found")
    except TypeError:
        print("error in file type")


symbol= input("Enter the Symbol you want for the Stock Market API eg. (AMZN, GOGL, IBM, etc)")
get_stock_market_data(symbol,is_timeseries=True)

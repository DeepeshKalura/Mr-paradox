import os
import datetime
import time
import argparse
from dotenv import load_dotenv
import requests


load_dotenv()

appid = os.getenv("APPID")

loc = "USA"
# date = "2023-01-01"



# url = f"http://api.wolframalpha.com/v2/query?input=Weather%20{loc}%20{date}&appid={appid}&format=plaintext&includepopid=WeatherSummary:WeatherData&output=JSON"
# response = requests.get(url)
# data = response.json()

# report:str = (data["queryresult"]["pods"][1]["subpods"][0]["plaintext"])
# print(report)
# time.sleep(5)


#  No guranatee that the data will be in the same format as the previous data ( true ) 

# Wolfram Alpha API  <-- fix response nhi dati

# Genai API <-- fix response deti hai
loc = "USA"
money = "2500" # INR 
date_year = 1934
money_url = f'http://api.wolframalpha.com/v2/query?input={money}+rupee+worth+in+{date_year}&appid={appid}&format=plaintext&output=JSON'

response = requests.get(money_url)
data = response.json()

report:str = (data["queryresult"]["pods"][1]["subpods"][0]["plaintext"])    
print(report)




# current money (1000 ) INR in date 
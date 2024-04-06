import os
import requests
from dotenv import load_dotenv
load_dotenv()

appid = os.getenv("APPID")
def get_weather(loc:str, date:str) -> str:
    url = f"http://api.wolframalpha.com/v2/query?input=Weather%20{loc}%20{date}&appid={appid}&format=plaintext&includepopid=WeatherSummary:WeatherData&output=JSON"
    response = requests.get(url)
    data = response.json()
    report:str = (data["queryresult"]["pods"][1]["subpods"][0]["plaintext"])
    return report

def get_money(money:str, date_year:int) -> str:
    money_url = f'http://api.wolframalpha.com/v2/query?input={money}+rupee+worth+in+{date_year}&appid={appid}&format=plaintext&output=JSON'
    response = requests.get(money_url)
    data = response.json()
    report:str = (data["queryresult"]["pods"][1]["subpods"][0]["plaintext"])    
    return report
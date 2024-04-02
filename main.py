import os
import datetime
from dotenv import load_dotenv
import requests


load_dotenv()

appid = os.getenv("APPID")

url = f"http://api.wolframalpha.com/v2/query?input=Weather%20Delhi%202024-04-02&appid={appid}&format=plaintext&includepopid=WeatherSummary:WeatherData&output=JSON"


response = requests.get(url)
data = response.json()
report:str = (data["queryresult"]["pods"][1]["subpods"][0]["plaintext"])

# print(report)

def clean_report(report:str) -> str:
    report = report.replace("\n", " | ")
    report = report.replace(" |  | ", "\n")
    report = report.replace(" | ", "\n")
    return report

def convert_report_to_dict(report:str) -> dict:
    report_dict:dict = {}
    for line in report.split("\n"):
        key, value = line.split(" | ")
        report_dict[key] = value
    return report_dict

print(convert_report_to_dict(clean_report(report)))


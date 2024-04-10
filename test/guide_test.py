import os
import sys

def model_response(location:str, time:str, money_value:str, money:str, weather:str )-> str:
    return "This is a fake model response"

class TestGuideCommand:
    location = "Mumbai"
    time = "02-09-1983"
    budget = "10000"
    money = "INR"
    weather = "sunny"

    def test_fake_model_response(self):
        assert model_response(location=self.location, time=self.time, money_value=self.budget, money=self.money, weather=self.weather) == "This is a fake model response"
        
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.llm_model import model_response

class TestGuideCommand:
    location = "Mumbai"
    time = "02-09-1983"
    budget = "10000"
    money = "INR"
    weather = "sunny"
    def test_google_api_working(self):
        a = model_response(location=self.location, dates=self.time, money_value=self.budget, money=self.money, weather=self.weather)
        assert a != None
        assert a != ""
        assert type(a) == str
    
    def test_fake_model_response(self):
        def model_response(location=self.location, dates=self.time, money_value=self.budget, money=self.money, weather=self.weather)-> str:
            return "This is a fake model response"
        
        assert model_response(location=self.location, dates=self.time, money_value=self.budget, money=self.money, weather=self.weather) == "This is a fake model response"
        
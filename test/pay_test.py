import os
import sys
import warnings

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import under_construction

class TestPaymentRequest:

    value = 100
    def test_pay(self):
        assert under_construction(self.value) == "This is payment feature is under construction! sob sob sob thanks for 100 money"
    

import requests
import pandas as pd
import defs
import utils

class OandaAPI():
    
    def __init__(self):
        self.session = requests.Session()

    def fetch_instruments(self):
        pass
    def get_instruments(self):
        pass
    def save_instruments(self):
        pass
    def save_candles(self, pair_name, count, granularity):
        url = f"{defs.OANDA_URL}/instruments/{pair_name}/candles"

if __name__ == "__main__":
    api = OandaAPI
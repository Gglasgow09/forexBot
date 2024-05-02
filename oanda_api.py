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
    def fetch_candles(self, pair_name, count, granularity):
        url = f"{defs.OANDA_URL}/instruments/{pair_name}/candles"

        params = dict(
            count = count,
            granularity = granularity,
            price = "MBA"
        )

        response =  self.session.get(url, params=params, headers=defs.SECURE_HEADER)
        return response.status_code, response.json()

if __name__ == "__main__":
    api = OandaAPI()
    print(api.fetch_candles("EUR_NOK", 50, "H4"))
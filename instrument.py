import pandas as pd
import utils

class Instrument():
    def __init__(self, object):
        self.name = object['name']
        self.ins_type = object['type']
        self.displayName = object['displayName']
        self.pipLocation = pow(10, object['pipLocation']) 
        self.marginRate = object['marginRate']

    def __repr__(self):
        return str(vars(self))
    
    @classmethod
    def get_instruments_df(cls):
        return pd.read_pickle(utils.get_instruments_data_filename())
    
    @classmethod
    def get_instruments_list(cls):
        df = cls.get_instruments_df()
        return [Instrument(x) for x in df.to_dict(orient='records')]


if __name__ == "__main__":
     print(Instrument.get_instruments_list())
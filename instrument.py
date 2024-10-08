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
    
    '''
        dict to access instruments by pair name 

        instrument_dict = 
        {
            "EUR_USD" : Instruments(),
            "EUR_GBP" : Instruments(),
            "..." : Instruments(),
        }
        
        our_instrument = instrument_dict["EUR_USD"]
    '''

    @classmethod
    def get_instrument_dict(cls):
        i_list = cls.get_instruments_list()
        i_keys = [ x.name for x in i_list ]
        return { k:v for (k,v) in zip(i_keys, i_list) }
    
    @classmethod
    def get_instrument_by_name(cls, pairname):
        d = cls.get_instrument_dict()
        if pairname in d:
            return d[pairname]
        else:
            return None


if __name__ == "__main__":
    #  for k,v in Instrument.get_instrument_dict().items():
    #      print(k,v)


    print(Instrument.get_instrument_by_name("EUR_USD"))

    
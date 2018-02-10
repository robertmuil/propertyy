import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)

fpaths = {}

fpaths['data_base'] = './data'

fpaths['ppd_sample1'] = os.path.join(fpaths['data_base'], 'ppd_data-LE16_7XG-1999_11_26-2018_01_01.csv.gz')
fpaths['ppd_sample2'] = os.path.join(fpaths['data_base'], 'ppd_data_LE16_2018-02-10.csv.gz')

column_enums = {
    'property_type': {
          'D': 'detached' #?
        , 'S': 'semi-detached' #?
        , 'T': 'terraced'
        , 'D': 'flat/maisonette'
        , 'O': 'other'
    }
}

def load_ppd(fpath=fpaths['ppd_sample2']):
    """
    Loads a Price-Paid Data set.
    """
    df = pd.read_csv(fpath
                    , parse_dates = ['deed_date'])
    
    logger.info('Loaded \'{}\': {}'.format(fpath, df.shape))
    
    return df
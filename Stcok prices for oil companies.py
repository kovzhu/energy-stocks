import tushare as ts
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

token = 'ff0abe11ff60a8ab965180971559c539d552c0e51de7e501593ff762'
ts.set_token(token)
pro = ts.pro_api()

yf.pdr_override()

OilCompanies = {'CNOOC': '00883.hk',
                'Yanchang': '00346.hk',
                'CNPC': '00857.hk',
                'Sinopec': '00386.hk'
                }

IOCs = {
    # 'Shell': 'RDS.A',
    'BP': 'BP',
    'Chevron': 'CVX',
    'Total': 'TOT',
    'Occidental': 'OXY',
    'PetroChina': 'PTR',
    'CNOOC': 'CEO',
    'Devon': 'DVN',
    'Chesapeake': 'CHK',
}

with pd.ExcelWriter('oil companies stocks.xlsx') as writer:
    for key in OilCompanies:
        df = pd.DataFrame(pro.hk_daily(ts_code=OilCompanies[key], start_date='20200101',
                                       end_date='20200317'))
        df.to_excel(writer, sheet_name=key)
    for key in IOCs:
        data = pd.DataFrame(pdr.get_data_yahoo(
            IOCs[key], start="2020-01-01", end="2020-03-17"))
        data.to_excel(writer, sheet_name=key)

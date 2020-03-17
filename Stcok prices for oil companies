import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt

token = 'your token for tushare'
ts.set_token(token)
pro = ts.pro_api()

OilCompanies = {'CNOOC': '00883.hk',
                'Yanchang': '00346.hk',
                'CNPC': '00857.hk',
                'Sinopec': '00386.hk'
                }

with pd.ExcelWriter('HK stocks.xlsx') as writer:
    for key in OilCompanies:
        df = pd.DataFrame(pro.hk_daily(ts_code=OilCompanies[key], start_date='20200101',
                                       end_date='20200317'))
        df.to_excel(writer, sheet_name=key)

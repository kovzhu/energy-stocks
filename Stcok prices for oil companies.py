import tushare as ts
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr


def main():

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
        'CNOOC.US': 'CEO',
        'Devon': 'DVN',
        'Chesapeake': 'CHK',
    }
    StartDateCN = '20100101'
    EndDateCN = '20200317'

    StartDateIOC = "2020-01-01"
    EndDateIOC = "2020-03-17"

    df1 = CNData(OilCompanies, StartDateCN, EndDateCN)
    StockChanges(df1)
    df2 = IOCData(IOCs, StartDateIOC, EndDateIOC)

    ToExcel(df1, df2)

# Write each dataframe into a tab of excel
# with pd.ExcelWriter('oil companies stocks.xlsx') as writer:
#     for key in OilCompanies:
#         df = pd.DataFrame(pro.hk_daily(ts_code=OilCompanies[key], start_date='20200101',
#                                        end_date='20200317'))
#         df['Company'] = key
#         df.to_excel(writer, sheet_name=key)
#     for key in IOCs:
#         data = pd.DataFrame(pdr.get_data_yahoo(
#             IOCs[key], start="2020-01-01", end="2020-03-17"))
#         data['Company'] = key
#         data.to_excel(writer, sheet_name=key)

# Combine the dataframes and write into a single tab


def ToExcel(df1, df2):
    with pd.ExcelWriter('oil companies stocks.xlsx') as writer:
        df1.to_excel(writer, sheet_name='Nocs')
        df2.to_excel(writer, sheet_name='Iocs')


def IOCData(IOCs, StartDateIOC, EndDateIOC):
    yf.pdr_override()
    data1 = pd.DataFrame()
    for key in IOCs:
        data = pd.DataFrame(pdr.get_data_yahoo(
            IOCs[key], start=StartDateIOC, end=EndDateIOC))
        data['Company'] = key
        data1 = pd.DataFrame.append(data1, data)
    return data1


def CNData(OilCompanies, startdate, enddate):
    token = 'your tushare token'
    ts.set_token(token)
    pro = ts.pro_api()
    df1 = pd.DataFrame()
    for key in OilCompanies:
        df = pd.DataFrame(pro.hk_daily(ts_code=OilCompanies[key], start_date=startdate,
                                       end_date=enddate))
        df['Company'] = key
        df1 = pd.DataFrame.append(df1, df)

    df1['Year'] = df1['trade_date'].str[0:4].apply(int)
    df1['Month'] = df1['trade_date'].str[4:6].apply(int)
    df1['Day'] = df1['trade_date'].str[6:8].apply(int)
    df1['Date'] = df1['trade_date'].apply(pd.to_datetime)
    return df1


def StockChanges(df1):
    Pivot = pd.pivot_table(df1, values='close',
                           index='Company', columns='Date')
    pivot2 = Pivot.transpose()
    base = pivot2.iloc[0]
    i = len(pivot2.index)
    pivot3 = pivot2
    for row in range(1, i):
        pivot3.iloc[row] = (pivot2.iloc[row] - base)/base
    pivot3.iloc[0] = 0
    plt.plot(pivot3)
    plt.savefig('stocks.png')


if __name__ == '__main__':
    main()

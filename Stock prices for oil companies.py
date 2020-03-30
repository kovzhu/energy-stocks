import tushare as ts
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
# from io import BytesIO


def main():

    HKOilCompanies = {'CNOOC': '00883.hk',
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

    OFS = {'Sinopec OFS': '600871.SH', 'COOEC': '600583.SH', 'COSL': '601808.SH', 'Zhudong': '002207.SZ', 'Hengtai': '300157.SZ',
           'Tongyuan': '300164.SZ', 'HBP': '002554.SZ', 'Renzhi': '002629.SZ', 'Beken': '002828.SZ', 'Zhongman': '603619.SH'}

    StartDateCN = '20200101'
    EndDateCN = '20200317'

    StartDateIOC = "2020-01-01"
    EndDateIOC = "2020-03-17"

    # df1 = HKData(HKOilCompanies, StartDateCN, EndDateCN)
    df2 = CNData(OFS, StartDateCN, EndDateCN)
    StockChanges(df2)

    # df2 = IOCData(IOCs, StartDateIOC, EndDateIOC)

    # ToExcel(df1, df2)


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


def HKData(OilCompanies, startdate, enddate):
    token = 'Your Tushare token'
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


def CNData(OilCompanies, startdate, enddate):
    token = 'your token'
    ts.set_token(token)
    pro = ts.pro_api()
    df1 = pd.DataFrame()
    for key in OilCompanies:
        df = pd.DataFrame(pro.daily(ts_code=OilCompanies[key], start_date=startdate,
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
    labels = pivot3.columns
    plt.legend(labels=labels, loc='best')
    # imgdata = BytesIO()
    plt.savefig('stocks.png')
    # plt.savefig(imgdata, format="png")
    # return imgdata

# with pd.ExcelWriter('test.xlsx') as writer:
#     df1.to_excel(writer, sheet_name='date')
#     Pivot.to_excel(writer, sheet_name='pivot')

# df1.to_excel('stock test2.xlsx')


if __name__ == '__main__':
    main()

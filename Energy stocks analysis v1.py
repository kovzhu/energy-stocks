import yfinance as yf
import pandas as pd


company_dict = {
        'Exxon Mobil Corporation':'XOM',
        'Chevron Corporation':'CVX',
        'Royal Dutch Shell plc A':'RDS-A',
        'BP plc':'BP'
    }

def get_company_historical_data(company_name,company_ticker):
    '''
    The function gets the historical stock data, and keeps only the close price with the company name as the column name
    '''
    try:
        data = yf.Ticker(company_ticker).history(period = "max")
        data.drop(columns=['Open','High','Low','Dividends','Stock Splits','Volume'], inplace=True)
        data.rename({'Close': company_name},axis=1,inplace=True)
        return data
    except:
        pass

def generate_combined_data(company_dict):
    '''
    The function gets all the historical close data in the company_dict and combine all the data into a dataframe.   
    '''
    data = pd.DataFrame()
    for key,value in company_dict.items():
        company_stock_close = get_company_historical_data(key,value)
        try:
            data = pd.merge(data,company_stock_close,how='outer', left_index=True,right_index=True )
        except:
            continue
    return data

def get_company_lists():
    '''
    The function fetches the list of companies and their tickers stored in Excel
    '''

    list_folder = r'C:\Users\Kunfeng.Zhu\OneDrive - IHS Markit\00_Upstream Transformation\03_Companies\Sentiment\SP 500 list.xlsx'
    sp500_companies_table = pd.read_excel(list_folder,sheet_name='sp 500 list',header=4,usecols="B:J")
    sp_sectors_table = pd.read_excel(list_folder,sheet_name='sp sector',header=7,usecols="C:H")
    yahoo_finance_energy_companies = pd.read_excel(list_folder,sheet_name='Yh finance energy', header=6, usecols="C:D")

    sp500_list = list(sp500_companies_table['Symbol'])
    sp_setcors_list = list(sp_sectors_table['Symbol'])
    yahoo_energy_companies_dict = dict(zip(list(yahoo_finance_energy_companies['Name']),list(yahoo_finance_energy_companies['Symbol'])))
    return sp500_list, sp_setcors_list, yahoo_energy_companies_dict


yahoo_energy_company_list = {
'Exxon Mobil Corporation': 'XOM',
 'Chevron Corporation': 'CVX',
 'Royal Dutch Shell plc': 'RDS-A',
 'PetroChina Company Limited': 'PTR',
 'TotalEnergies SE': 'TTE',
 'ConocoPhillips': 'COP',
 'BP p.l.c.': 'BP',
 'Equinor ASA': 'EQNR',
 'Enbridge Inc.': 'ENB',
 'China Petroleum & Chemical Corporation': 'SNP',
 'Petróleo Brasileiro S.A. - Petrobras': 'PBR-A',
 'EOG Resources, Inc.': 'EOG',
 'Eni S.p.A.': 'E',
 'Canadian Natural Resources Limited': 'CNQ',
 'Enterprise Products Partners L.P.': 'EPD',
 'TC Energy Corporation': 'TRP',
 'Pioneer Natural Resources Company': 'PXD',
 'Schlumberger Limited': 'SLB',
 'Marathon Petroleum Corporation': 'MPC',
 'Kinder Morgan, Inc.': 'KMI',
 'Suncor Energy Inc.': 'SU',
 'The Williams Companies, Inc.': 'WMB',
 'Phillips 66': 'PSX',
 'MPLX LP': 'MPLX',
 'Valero Energy Corporation': 'VLO',
 'Devon Energy Corporation': 'DVN',
 'Ecopetrol S.A.': 'EC',
 'Occidental Petroleum Corporation': 'OXY',
 'ONEOK, Inc.': 'OKE',
 'Energy Transfer LP': 'ET',
 'Cenovus Energy Inc.': 'CVE',
 'Hess Corporation': 'HES',
 'Baker Hughes Company': 'BKR',
 'Halliburton Company': 'HAL',
 'Diamondback Energy, Inc.': 'FANG',
 'Coterra Energy Inc.': 'CTRA',
 'Continental Resources, Inc.': 'CLR',
 'Pembina Pipeline Corporation': 'PBA',
 'Marathon Oil Corporation': 'MRO',
 'Tenaris S.A.': 'TS',
 'Targa Resources Corp.': 'TRGP',
 'Sasol Limited': 'SSL',
 'Texas Pacific Land Corporation': 'TPL',
 'Magellan Midstream Partners, L.P.': 'MMP',
 'APA Corporation': 'APA',
 'Cameco Corporation': 'CCJ',
 'Ovintiv Inc.': 'OVV',
 'Western Midstream Partners, LP': 'WES',
 'Phillips 66 Partners LP': 'PSXP',
 'EQT Corporation': 'EQT',
 'Chesapeake Energy Corporation': 'CHKEL',
 'Cosan S.A.': 'CSAN',
 'Plains All American Pipeline, L.P.': 'PAA',
 'Valvoline Inc.': 'VVV',
 'Whiting Petroleum Corporation': 'WLL',
 'Sinopec Shanghai Petrochemical Company Limited': 'SHI',
 'National Fuel Gas Company': 'NFG',
 'Antero Resources Corporation': 'AR',
 'Southwestern Energy Company': 'SWN',
 'DCP Midstream, LP': 'DCP-PC',
 'HollyFrontier Corporation': 'HFC',
 'NOV Inc.': 'NOV',
 'Magnolia Oil & Gas Corporation': 'MGY',
 'PDC Energy, Inc.': 'PDCE',
 'Range Resources Corporation': 'RRC',
 'Civitas Resources, Inc.': 'CIVI',
 'Matador Resources Company': 'MTDR',
 'ChampionX Corporation': 'CHX',
 'Antero Midstream Corporation': 'AM',
 'DT Midstream, Inc.': 'DTM',
 'Shell Midstream Partners, L.P.': 'SHLX',
 'Murphy Oil Corporation': 'MUR',
 'Equitrans Midstream Corporation': 'ETRN',
 'Denbury Inc.': 'DEN',
 'SM Energy Company': 'SM',
 'California Resources Corporation': 'CRC',
 'EnLink Midstream, LLC': 'ENLC',
 'Sunoco LP': 'SUN',
 'Callon Petroleum Company': 'CPE',
 'Crescent Point Energy Corp.': 'CPG',
 'Enable Midstream Partners, LP': 'ENBL',
 'CNX Resources Corporation': 'CNX',
 'TechnipFMC plc': 'FTI',
 'NuStar Energy L.P.': 'NS-PA',
 'Enerplus Corporation': 'ERF',
 'Helmerich & Payne, Inc.': 'HP',
 'Oasis Petroleum Inc.': 'OAS',
 'Valaris Limited': 'VAL',
 'Cactus, Inc.': 'WHD',
 'Renewable Energy Group, Inc.': 'REGI',
 'Black Stone Minerals, L.P.': 'BSM',
 'Plains GP Holdings, L.P.': 'PAGP',
 'Comstock Resources, Inc.': 'CRK',
 'Delek Logistics Partners, LP': 'DKL',
 'Liberty Oilfield Services Inc.': 'LBRT',
 'Weatherford International plc': 'WFRD',
 'Vermilion Energy Inc.': 'VET',
 'Euronav NV': 'EURN',
 'Patterson-UTI Energy, Inc.': 'PTEN',
 'Holly Energy Partners, L.P.': 'HEP',
 'Viper Energy Partners LP': 'VNOM',
 'World Fuel Services Corporation': 'INT',
 'Crestwood Equity Partners LP': 'CEQP-P',
 'CVR Energy, Inc.': 'CVI',
 'Clean Energy Fuels Corp.': 'CLNE',
 'USA Compression Partners, LP': 'USAC',
 'PBF Energy Inc.': 'PBF',
 'Teekay LNG Partners L.P.': 'TGP-PB',
 'Frontline Ltd.': 'FRO',
 'Expro Group Holdings N.V.': 'XPRO',
 'GasLog Ltd.': 'GLOG-PA',
 'Noble Corporation': 'NE',
 'Gulfport Energy Corporation': 'GPOR',
 'BP Midstream Partners LP': 'BPMP',
 'Genesis Energy, L.P.': 'GEL',
 'Arch Resources, Inc.': 'ARCH',
 'Alliance Resource Partners, L.P.': 'ARLP',
 'Golar LNG Limited': 'GLNG',
 'Peabody Energy Corporation': 'BTU',
 'Delek US Holdings, Inc.': 'DK',
 'Oceaneering International, Inc.': 'OII',
 'Archrock, Inc.': 'AROC',
 'Calumet Specialty Products Partners, L.P.': 'CLMT',
 'Laredo Petroleum, Inc.': 'LPI',
 'Core Laboratories N.V.': 'CLB',
 'FLEX LNG Ltd.': 'FLNG',
 'Oasis Midstream Partners LP': 'OMP',
 'GasLog Partners LP': 'GLOP-PC',
 'NGL Energy Partners LP': 'NGL-PB',
 'Brigham Minerals, Inc.': 'MNRL',
 'NOW Inc.': 'DNOW',
 'Bristow Group Inc.': 'VTOL',
 'DHT Holdings, Inc.': 'DHT',
 'ProPetro Holding Corp.': 'PUMP',
 'Kimbell Royalty Partners, LP': 'KRP',
 'Hess Midstream LP': 'HESM',
 'Talos Energy Inc.': 'TALO',
 'Par Pacific Holdings, Inc.': 'PARR',
 'Scorpio Tankers Inc.': 'STNG',
 'Global Partners LP': 'GLP-PA',
 'Nabors Industries Ltd.': 'NBR',
 'Navigator Holdings Ltd.': 'NVGS',
 'CrossAmerica Partners LP': 'CAPL',
 'U.S. Silica Holdings, Inc.': 'SLCA',
 'CONSOL Energy Inc.': 'CEIX',
 'DMC Global Inc.': 'BOOM',
 'GeoPark Limited': 'GPRK',
 'PBF Logistics LP': 'PBFX',
 'Select Energy Services, Inc.': 'WTTR',
 'Dril-Quip, Inc.': 'DRQ',
 'Berry Corporation': 'BRY',
 'Dorchester Minerals, L.P.': 'DMLP',
 'TORM plc': 'TRMD',
 'Sabine Royalty Trust': 'SBR',
 'Ranger Oil Corporation': 'ROCC',
 'MRC Global Inc.': 'MRC',
 'REX American Resources Corporation': 'REX',
 'Earthstone Energy, Inc.': 'ESTE',
 'Dorian LPG Ltd.': 'LPG',
 'Vista Oil & Gas, S.A.B. de C.V.': 'VIST',
 'Tidewater Inc.': 'TDW',
 'Precision Drilling Corporation': 'PDS',
 'Rattler Midstream LP': 'RTLR',
 'Permian Basin Royalty Trust': 'PBT',
 'Star Group, L.P.': 'SGU',
 'North American Construction Group Ltd.': 'NOA',
 'Teekay Tankers Ltd.': 'TNK',
 'SilverBow Resources, Inc.': 'SBOW',
 'Natural Resource Partners L.P.': 'NRP',
 'SandRidge Energy, Inc.': 'SD',
 'Sprague Resources LP': 'SRLP',
 'Oil States International, Inc.': 'OIS',
 'Tsakos Energy Navigation Limited': 'TNP',
 'San Juan Basin Royalty Trust': 'SJT',
 'Ranger Energy Services, Inc.': 'RNGR',
 'Solaris Oilfield Infrastructure, Inc.': 'SOI',
 'NACCO Industries, Inc.': 'NC',
 'Summit Midstream Partners, LP': 'SMLP',
 'Natural Gas Services Group, Inc.': 'NGS',
 'Geospace Technologies Corporation': 'GEOS',
 'Forum Energy Technologies, Inc.': 'FET',
 'MV Oil Trust': 'MVO',
 'North European Oil Royalty Trust': 'NRT',
 'PermRock Royalty Trust': 'PRT',
 'Dynagas LNG Partners LP': 'DLNG-PA',
 'Cross Timbers Royalty Trust': 'CRT',
 'Mesa Royalty Trust': 'MTR',
 'NuStar Energy L.P. 9.00% CUM PFD C': 'NS-PC',
 'DCP Midstream, LP 7.875 CUM RED B': 'DCP-PB',
 'Teekay LNG Partners L.P. PFD UNIT SER A': 'TGP-PA',
 'El Paso Energy Capital Trust I PFD CV TR SECS': 'EP-PC',
 'Höegh LNG Partners LP': 'HMLP-PA'}



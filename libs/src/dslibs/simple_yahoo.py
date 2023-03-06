import datetime
import pandas as pd


def date2unix(strdate):
    date = datetime.datetime.strptime(strdate, '%Y-%m-%d')
    return str(int(date.timestamp()))


def get_from_yahoo(currency, startDate, endDate):
    # Wczytanie danych z https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD
    return pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/' + currency
                       + '?period1=' + date2unix(startDate) + '&period2=' + date2unix(endDate)
                       + '&interval=1d&events=history&includeAdjustedClose=true')

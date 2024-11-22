import yfinance as yf
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from lxml import etree
from datetime import datetime
import requests
import pandas as pd
import numpy as np
import threading
import time
import json
import asyncio

params = {
  'access_key': 'fc86254346a54a4fa6f26c220adbfab8'
}

header = {
    'user-agent': 'Mozilla/5.0'
}

yf.pdr_override()

# getting all sp500 stocks 
all_tickers_xpath = '//span[text() = "S&P 500 component stocks"]/following::tbody[1]/tr/td[1]/a'
soup = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies', headers=header).content, 'html.parser')
dom = etree.HTML(str(soup))

# find all tickers
all_tickers = [i.text for i in dom.xpath(all_tickers_xpath)]

# function for getting all yahoo finance data
def yfinance_get_data(tickers: list[str], start: datetime = datetime(2022, 1, 3)):
    return pdr.get_data_yahoo(' '.join(tickers), start=start)

# get data for start time of 1, 1, 2021
data = yfinance_get_data(all_tickers, start = datetime(2021, 1, 1))

# write data into a .csv file 
data.to_csv('stockdata.csv')

print('stockdata.csv is made')
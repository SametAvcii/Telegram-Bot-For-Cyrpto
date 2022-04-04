from posixpath import split
from re import A
import requests


def get_categories_List(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/coins/categories/list').json()

    list = []
    count = 0
    for i in url:
        a = i['name']
        list.append(a)
        count += 1
        if count % 5 == 0:
            list.append("\n")
        if count == 30:
            break
    list = ", ".join(list)

    message = f'Coin Kategorileri \n {list}'
    update.message.reply_text(message)


def get_btc_comp(update, context):

    url = requests.get(
        'https://api.coingecko.com/api/v3/companies/public_treasury/bitcoin').json()
    list = []
    count = 0
    a = url['companies']
    for i in a:
        b = i['name']
        list.append(b)
        c = i['total_holdings']
        list.append(f': {c} \n')
        count += 1
        if count == 30:
            break
    list = "".join(list)
    message = f'Şirketlerin Sahip Oldukları Bitcoin Miktarları \n{list}'
    update.message.reply_text(message)


def get_eth_comp(update, context):

    url = requests.get(
        'https://api.coingecko.com/api/v3/companies/public_treasury/ethereum').json()
    list = []
    count = 0
    a = url['companies']
    for i in a:
        b = i['name']
        list.append(b)
        c = i['total_holdings']
        list.append(f': {c} \n')
        count += 1
        if count == 30:
            break
    list = "".join(list)
    message = f'Şirketlerin Sahip Oldukları Ethereum Miktarları \n{list}'
    update.message.reply_text(message)


def get_total_cur(update, context):
    url = requests.get('https://api.coingecko.com/api/v3/global').json()
    a = url['data']['active_cryptocurrencies']

    message = f'Toplam Kripto Para Birimi Sayısı: {a}'
    update.message.reply_text(message)


def get_total_market(update, context):
    url = requests.get('https://api.coingecko.com/api/v3/global').json()
    a = url['data']['markets']

    message = f'Toplam Kripto Borsa Sayısı: {a}'
    update.message.reply_text(message)


def get_market_cap_change_percentage_24h_usd(update, context):
    url = requests.get('https://api.coingecko.com/api/v3/global').json()
    a = url['data']['market_cap_change_percentage_24h_usd']
    message = f'Coinlerin 24 saatte değişim yüzdesi: {a}'
    update.message.reply_text(message)


def get_total_cap(update, context):

    url = requests.get('https://api.coingecko.com/api/v3/global').json()
    list = []
    count = 0
    a = url['data']['total_market_cap']
    for k in a:
        list.append(f'{k}: {a[k]} \n')
    list = "".join(list)
    message = f'Coinlerin Toplam Miktarları \n{list}'
    update.message.reply_text(message)

def get_total_future(update, context):

    url = requests.get('https://api.coingecko.com/api/v3/derivatives/exchanges').json()
    list = []
    a = url
    for k in a:
       list.append(k['name'])
       list.append(":")
       list.append(k['trade_volume_24h_btc'])
       list.append('\n')
      
      
  
    list="".join(list)
    message = f'Kaldıraçlı Borsa Adları: 24 saatlik Btc Hacimleri \n{list}'
    update.message.reply_text(message)



def get_market_cap_percentage(update, context):

    url = requests.get('https://api.coingecko.com/api/v3/global').json()
    list = []
    count = 0
    a = url['data']['market_cap_percentage']
    for k in a:
        list.append(f'{k}: {a[k]} \n')
    list = "".join(list)
    message = f'Coinlerin Market Dominansları \n{list}'
    update.message.reply_text(message)


def get_total_volume(update, context):

    url = requests.get('https://api.coingecko.com/api/v3/global').json()
    list = []
    count = 0
    a = url['data']['total_volume']
    for k in a:
        list.append(f'{k}: {a[k]} \n')
    list = "".join(list)
    message = f'Coinlerin Market Dominansları \n{list}'
    update.message.reply_text(message)

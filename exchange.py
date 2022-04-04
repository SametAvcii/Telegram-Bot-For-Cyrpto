
import requests


def exchangeList(update, context):
    url = requests.get('https://api.coingecko.com/api/v3/exchanges').json()

    list = []
    count = 0
    for i in url:
        a = i['id']
        list.append(a)
        count += 1
        if count % 5 == 0:
            list.append("\n")
        if count == 20:
            break
    list = ", ".join(list)

    message = f'Exchange List: \n {list}'
    update.message.reply_text(message)


def get_btcturk(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/btcturk').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    


def get_binance(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/binance').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)

def get_mxc(update,context):

    url=requests.get('https://api.coingecko.com/api/v3/exchanges/mxc').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)   

def get_okex(update,context):

    url=requests.get('https://api.coingecko.com/api/v3/exchanges/okex').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)       
    
def get_kucoin(update,context):

    url=requests.get('https://api.coingecko.com/api/v3/exchanges/kucoin').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    
    
def get_gate(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/gate').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    
    
def get_crypto_com(update,context):

    url=requests.get('https://api.coingecko.com/api/v3/exchanges/crypto_com').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    
    
def get_gdax(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/gdax').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    

def get_bitrue(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/bitrue').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    

def get_huobi(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/huobi').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    

def get_bitmart(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/bitmart').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    
    
def get_ftx_spot(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/ftx_spot').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    

def get_kraken(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/kraken').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    
    
def get_bitfinex(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/bitfinex').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    
    
def get_bybit_spot(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/bybit_spot').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    
    
def get_latoken(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/latoken').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    
    
def get_binance_us(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/binance_us').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    
    
def get_phemex(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/phemex').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    

def get_btse(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/btse').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    

def get_gemini(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/gemini').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    
    
def get_bittrex(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/bittrex').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)    
    
def get_cyrptology(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/cyrptology').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)        

def get_hotbit(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/hotbit').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)   

def get_paribu(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/paribu').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)   
                 

def get_bitci(update,context):
   
    url=requests.get('https://api.coingecko.com/api/v3/exchanges/bitci').json() 
    name=url['name']
    web_url=url['url']
    year_established=url['year_established']
    country=url['country']
    image=url['image']
    trade_volume_24h_btc=url['trade_volume_24h_btc']
    trust_score_rank=url['trust_score_rank']
    message=f'Borsa Adı: {name} \n Borsa Güven Sıralaması: {trust_score_rank} \n  Web Adresi: {web_url} \n Kuruluş Yılı: {year_established} \n Ulke: {country} \n Logo: {image} \n 24 saatlik btc işlem hacmi: {trade_volume_24h_btc} \n  '
    update.message.reply_text(message)   
                                  
import requests
def get_btc(update, context):

    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').json()
    btc = url['bitcoin']['usd']
    message = f'Coin Price: {btc}'

    update.message.reply_text(message)


def get_bnb(update, context):

    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd').json()

    binance = url['binancecoin']['usd']

    message = f'Coin Price: {binance}'

    update.message.reply_text(message)


def get_eth(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd').json()

    eth = url['ethereum']['usd']
    message = f'Coin Price: {eth}'
    update.message.reply_text(message)


def get_sol(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd').json()

    sol = url['solana']['usd']
    message = f'Coin Price: {sol}'
    update.message.reply_text(message)


def get_xrp(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd').json()

    xrp = url['ripple']['usd']
    message = f'Coin Price: {xrp}'
    update.message.reply_text(message)


def get_ada(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd').json()

    ada = url['cardano']['usd']
    message = f'Coin Price: {ada}'
    update.message.reply_text(message)


def get_dot(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=polkadot&vs_currencies=usd').json()

    dot = url['polkadot']['usd']
    message = f'Coin Price: {dot}'
    update.message.reply_text(message)


def get_doge(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd').json()
    doge = url['dogecoin']['usd']
    message = f'Coin Price: {doge}'
    update.message.reply_text(message)


def get_shib(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=shiba-inu&vs_currencies=usd').json()
    shib = url['shiba-inu']['usd']
    message = f'Coin Price: {shib}'
    update.message.reply_text(message)


def get_luna(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=terra-luna&vs_currencies=usd').json()
    luna = url['terra-luna']['usd']
    message = f'Coin Price: {luna}'
    update.message.reply_text(message)


def get_cro(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=cronos&vs_currencies=usd').json()
    cro = url['cronos']['usd']
    message = f'Coin Price: {cro}'
    update.message.reply_text(message)


def get_near(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=near&vs_currencies=usd').json()
    near = url['near']['usd']
    message = f'Coin Price: {near}'
    update.message.reply_text(message)


def get_dai(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=dai&vs_currencies=usd').json()
    dai = url['dai']['usd']
    message = f'Coin Price: {dai}'
    update.message.reply_text(message)


def get_ltc(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd').json()
    ltc = url['litecoin']['usd']
    message = f'Coin Price: {ltc}'
    update.message.reply_text(message)


def get_atom(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=cosmos&vs_currencies=usd').json()
    atom = url['cosmos']['usd']
    message = f'Coin Price: {atom}'
    update.message.reply_text(message)


def get_link(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=chainlink&vs_currencies=usd').json()
    link = url['chainlink']['usd']
    message = f'Coin Price: {link}'
    update.message.reply_text(message)


def get_uni(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=uniswap&vs_currencies=usd').json()
    uni = url['uniswap']['usd']
    message = f'Coin Price: {uni}'
    update.message.reply_text(message)


def get_tron(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=tron&vs_currencies=usd').json()
    tron = url['tron']['usd']
    message = f'Coin Price: {tron}'
    update.message.reply_text(message)


def get_ftx(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=ftx-token&vs_currencies=usd').json()
    ftx = url['ftx-token']['usd']
    message = f'Coin Price: {ftx}'
    update.message.reply_text(message)


def get_algo(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=algorand&vs_currencies=usd').json()
    algo = url['algorand']['usd']
    message = f'Coin Price: {algo}'
    update.message.reply_text(message)


def get_xlm(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=stellar&vs_currencies=usd').json()
    xlm = url['stellar']['usd']
    message = f'Coin Price: {xlm}'
    update.message.reply_text(message)


def get_waves(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=waves&vs_currencies=usd').json()
    waves = url['waves']['usd']
    message = f'Coin Price: {waves}'
    update.message.reply_text(message)


def get_vet(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=vechain&vs_currencies=usd').json()
    vet = url['vechain']['usd']
    message = f'Coin Price: {vet}'
    update.message.reply_text(message)


def get_mana(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=decentraland&vs_currencies=usd').json()
    mana = url['decentraland']['usd']
    message = f'Coin Price: {mana}'
    update.message.reply_text(message)


def get_fil(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=filecoin&vs_currencies=usd').json()
    fil = url['filecoin']['usd']
    message = f'Coin Price: {fil}'
    update.message.reply_text(message)


def get_axs(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=axie-infinity&vs_currencies=usd').json()
    axs = url['axie-infinity']['usd']
    message = f'Coin Price: {axs}'
    update.message.reply_text(message)


def get_ftm(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=fantom&vs_currencies=usd').json()
    ftm = url['fantom']['usd']
    message = f'Coin Price: {ftm}'
    update.message.reply_text(message)


def get_sand(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=the-sandbox&vs_currencies=usd').json()
    sand = url['the-sandbox']['usd']
    message = f'Coin Price: {sand}'
    update.message.reply_text(message)


def get_xtz(update, context):
    url = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=tezos&vs_currencies=usd').json()
    sand = url['the-sandbox']['usd']
    message = f'Coin Price: {sand}'
    update.message.reply_text(message)


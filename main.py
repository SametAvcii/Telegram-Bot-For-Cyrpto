from exchange import *
from coins import *
import config
from categories import *
from blockchainNetwork import *
from asyncio import shield
from posixpath import split
import config
from telegram.ext import *
import responses as R
import requests


def start_command(update, context):

    update.message.reply_text(config.coin_price)


def hello(update, context):
    update.message.reply_text("Hello, Welcome My Crypto Bot ")


def handle_message(update, context):
    text = str(update.message.text).lower()

    response = R.sample_responses(text)
    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(config.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("hello", hello))
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("btc", get_btc))
    dp.add_handler(CommandHandler("eth", get_eth))
    dp.add_handler(CommandHandler("bnb", get_bnb))
    dp.add_handler(CommandHandler("sol", get_sol))
    dp.add_handler(CommandHandler("xrp", get_xrp))
    dp.add_handler(CommandHandler("ada", get_ada))
    dp.add_handler(CommandHandler("dot", get_dot))
    dp.add_handler(CommandHandler("doge", get_doge))
    dp.add_handler(CommandHandler("shib", get_shib))
    dp.add_handler(CommandHandler("luna", get_luna))
    dp.add_handler(CommandHandler("cro", get_cro))
    dp.add_handler(CommandHandler("near", get_near))
    dp.add_handler(CommandHandler("dai", get_dai))
    dp.add_handler(CommandHandler("ltc", get_ltc))
    dp.add_handler(CommandHandler("atom", get_atom))
    dp.add_handler(CommandHandler("link", get_link))
    dp.add_handler(CommandHandler("uni", get_uni))
    dp.add_handler(CommandHandler("tron", get_tron))
    dp.add_handler(CommandHandler("ftx", get_ftx))
    dp.add_handler(CommandHandler("algo", get_algo))
    dp.add_handler(CommandHandler("xlm", get_xlm))
    dp.add_handler(CommandHandler("waves", get_waves))
    dp.add_handler(CommandHandler("vet", get_vet))
    dp.add_handler(CommandHandler("mana", get_mana))
    dp.add_handler(CommandHandler("xtz", get_xtz))
    dp.add_handler(CommandHandler("fil", get_fil))
    dp.add_handler(CommandHandler("axs", get_axs))
    dp.add_handler(CommandHandler("ftm", get_ftm))
    dp.add_handler(CommandHandler("sand", get_sand))

    dp.add_handler(CommandHandler("list", exchangeList))
    dp.add_handler(CommandHandler("btcturk", get_btcturk))
    dp.add_handler(CommandHandler("mexc", get_mxc))
    dp.add_handler(CommandHandler("coinbase", get_gdax))
    dp.add_handler(CommandHandler("binance", get_binance))
    dp.add_handler(CommandHandler("paribu", get_paribu))
    dp.add_handler(CommandHandler("bitrue", get_btcturk))
    dp.add_handler(CommandHandler("huobi", get_huobi))
    dp.add_handler(CommandHandler("bitmart", get_bitmart))
    dp.add_handler(CommandHandler("ftx", get_ftx_spot))
    dp.add_handler(CommandHandler("kraken", get_kraken))
    dp.add_handler(CommandHandler("bybit", get_bybit_spot))
    dp.add_handler(CommandHandler("latoken", get_latoken))
    dp.add_handler(CommandHandler("cyrpto_com", get_crypto_com))
    dp.add_handler(CommandHandler("binance_us", get_binance_us))
    dp.add_handler(CommandHandler("phemex", get_phemex))
    dp.add_handler(CommandHandler("btse", get_btse))
    dp.add_handler(CommandHandler("gemini", get_gemini))
    dp.add_handler(CommandHandler("bitci", get_bitci))
    dp.add_handler(CommandHandler("bittrex", get_bittrex))
    dp.add_handler(CommandHandler("cyrptology", get_cyrptology))
    dp.add_handler(CommandHandler("bitfinex", get_bitfinex))
    dp.add_handler(CommandHandler("blockchain", get_blockchainList))
    dp.add_handler(CommandHandler("kategoriler", get_categories_List))
    dp.add_handler(CommandHandler("btc_sirketler", get_btc_comp))
    dp.add_handler(CommandHandler("eth_sirketler", get_eth_comp))
    dp.add_handler(CommandHandler("coin_sayisi", get_total_cur))
    dp.add_handler(CommandHandler("toplam_miktar", get_total_cap))
    dp.add_handler(CommandHandler("toplam_hacim", get_total_volume))
    dp.add_handler(CommandHandler("dominans", get_market_cap_percentage))
    dp.add_handler(CommandHandler("market_sayisi", get_total_market))
    dp.add_handler(CommandHandler("degisim_yuzdesi",
                   get_market_cap_change_percentage_24h_usd))
    dp.add_handler(CommandHandler("future", get_total_future))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


main()

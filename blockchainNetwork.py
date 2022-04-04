import requests

def get_blockchainList(update, context):
    url = requests.get('https://api.coingecko.com/api/v3/asset_platforms').json()

    list = []
    count = 0
    for i in url:
        a = i['id']
        list.append(a)
        count += 1
        if count % 5 == 0:
            list.append("\n")
        if count == 30:
            break
    list = ", ".join(list)
    message = f'Blockchain Network List: \n {list}'
    update.message.reply_text(message)



import requests

def hit_sender(card,message,chat_id):
    bot_token = '6497076888:AAFffqvL1kBqstJe5dniTSGtlGBk8jkulQ4'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)

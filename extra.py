import requests

def hit_sender(card,message,chat_id):
    bot_token = '5625761910:AAGo4fCkoRE9J2oXk6Yt7wVwLOo'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)

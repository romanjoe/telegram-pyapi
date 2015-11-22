import telegram

TOKEN = '152394201:AAE6wwKF-y9gddMrXUTAnGNbGrifJKFHU-I'

bot = telegram.Telegram(token=TOKEN)

if not bot.get_me():
    exit(1)


def main():

    updates = bot.get_updates()

    for update in updates:
        bot.offset = update['update_id']

        bot.chat_id = update['message']['chat']['id']
        print (update['message']['text'])

if __name__ == '__main__':
    while True:
        main()

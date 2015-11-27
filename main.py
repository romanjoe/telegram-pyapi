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
#        print (update)
        print (telegram.Parser.get(update, extract_field='from'))
        print '----------'
        print (telegram.Parser.get(update, extract_field='chat'))
        print '----------'
        print (telegram.Parser.get(update, extract_field='message_id'))
        print '----------'
        print (telegram.Parser.get(update, extract_field='date'))

if __name__ == '__main__':
    while True:
        main()

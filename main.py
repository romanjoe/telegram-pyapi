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
        print (update)
        # print (telegram.Parser.get(update, extract_field='from'))
        # print '----------'
        # print (telegram.Parser.get(update, extract_field='chat'))
        # print '----------'
        # print (telegram.Parser.get(update, extract_field='message_id'))
        # print '----------'
        # print (telegram.Parser.get(update, extract_field='date'))
        # print '----------'

        """
        test getting thumbnails links
        thumbnails will receive a dictionary, were key is available resolution and value is file_id according
        then method getFile applied to each file_id of all available resolutions
        """

        # thumbnails = (telegram.Parser.get(update, extract_field='photo_size'))
        # for size in thumbnails.keys():
        #     link = bot.get_file(thumbnails.pop(size))
        #     print link

        """
        test getting sticker parameters
        """

        print (telegram.Parser.get(update, extract_field='sticker'))

if __name__ == '__main__':
    while True:
        main()

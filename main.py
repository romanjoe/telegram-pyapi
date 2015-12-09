import telegrambot as tb

TOKEN = '152394201:AAE6wwKF-y9gddMrXUTAnGNbGrifJKFHU-I'

bot = tb.TelegramBot(token=TOKEN)

if not bot.get_me():
    exit(1)


def main():

    updates = bot.get_updates()

    au = updates.Update.audio

#    username = updates.Update.forward_from.username

    print "done"

if __name__ == '__main__':
    while True:
        main()

import telegrambot as tb

TOKEN = '152394201:AAE6wwKF-y9gddMrXUTAnGNbGrifJKFHU-I'

bot = tb.TelegramBot(token=TOKEN)

if not bot.get_me():
    exit(1)


def main():

    updates = bot.get_updates()

    # sti = updates[0].Update.sticker
    aud = updates.Update.audio
    # voi = updates[2].Update.voice
    # vid = updates[3].Update.video
    # doc = updates[4].Update.document
#    username = updates.Update.forward_from.username

    print "done"

if __name__ == '__main__':
    while True:
        main()

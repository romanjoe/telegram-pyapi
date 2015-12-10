import telegrambot as tb

import urllib

TOKEN = '152394201:AAE6wwKF-y9gddMrXUTAnGNbGrifJKFHU-I'

bot = tb.TelegramBot(token=TOKEN)

if not bot.get_me():
    exit(1)


# image_url = "http://pixel.nymag.com/imgs/daily/vulture/2015/10/23/23-adele-hello.w529.h529.jpg"
# f = open('hello.jpg', 'wb')
# f.write(urllib.urlopen(image_url).read())
# f.close()


def main():

    resp = bot.get_updates()

    bot.send_chat_action(bot.chat_id, 'upload_photo')
    hello = 'hello.jpg'
    music = 'Balam Acab - Motion.mp3'
    video = 'Cortex-M4 FPU and DSP instruction usage in the STM32F4 family.mp4'

    bot.send_photo(bot.chat_id, hello, "from Adele", '', '')
    bot.send_message('hello \nit\'s me')
    bot.send_chat_action(bot.chat_id, 'upload_audio')
    bot.send_audio(bot.chat_id, music, '', '', '')
    bot.send_chat_action(bot.chat_id, 'upload_video')
    bot.send_video(bot.chat_id, video, '', '', '')

    # sti = updates[0].Update.sticker
    # aud = updates.Update.audio
    # voi = updates[2].Update.voice
    # vid = updates[3].Update.video
    # doc = updates[4].Update.document
    # username = updates.Update.forward_from.username

    print "done"

if __name__ == '__main__':
    while True:
        main()

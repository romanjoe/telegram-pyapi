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

    try:
        if resp.text.text_message == '/test':
            try:
                hello = 'test/hello.jpg'
                resp = bot.send_photo(bot.chat_id, hello, caption='Hello \n it\'s me', reply_markup='',
                                      reply_to_message_id='')

                available_thumbnail_sizes_array = []

                result = {}

                for photo in resp.photo:
                    available_thumbnail_sizes_array.append(photo)

                for size in available_thumbnail_sizes_array:
                    resolution = str(size['width']) + "x" + str(size['height'])
                    file_id = str(size['file_id'])
                    result[resolution] = file_id

                print "========== Parse response after sendPhoto ================"
                for res in result.keys():
                    link = bot.get_file(result.pop(res))
                    print "Photo thumbnail " + str(res)
                    print link
            except (AttributeError, IndexError):
                pass

            try:
                music = 'test/sample_audio.mp3'
                bot.send_chat_action(bot.chat_id, 'upload_audio')
                resp = bot.send_audio(bot.chat_id, music, performer='Nu Gravity', title='People', reply_markup='')
                audio = resp.audio

                print ("========== Parse response after sendAudio ================\n" +
                       "Audio file download link: " + str(bot.get_file(audio.file_id)) + "\n" +
                       "Performer: " + str(audio.performer) + "\n" +
                       "Title: " + str(audio.title) + "\n" +
                       "Duration: " + str(audio.duration) + "\n"
                       "Mime type: " + str(audio.mime_type) + "\n" +
                       "File Size: " + str(audio.file_size))
            except (AttributeError, IndexError):
                pass

            try:
                video = 'test/sample_video.mp4'
                resp = bot.send_video(bot.chat_id, video,
                                      caption='Have some fun!',
                                      reply_markup='', reply_to_message_id='',
                                      duration=45)
                video = resp.video

                print ("========== Parse response after sendAudio ================\n" +
                       "Video file download link: " + str(bot.get_file(video.file_id)) + "\n" +
                       "Height: " + str(video.height) + "\n" +
                       "Width: " + str(video.width) + "\n" +
                       "Duration: " + str(video.duration) + "\n"
                       "Mime type: " + str(video.mime_type) + "\n" +
                       "File Size: " + str(video.file_size))
            except (AttributeError, IndexError):
                pass

            try:
                document = 'test/LICENSE.pdf'
                resp = bot.send_document(bot.chat_id, document, '', '')
                document = resp.document

                print ("========== Parse response after sendDocument ================\n" +
                       "Document download link: " + str(bot.get_file(document.file_id)) + "\n" +
                       "Title: " + str(document.file_name) + "\n" +
                       "Mime type: " + str(document.mime_type) + "\n" +
                       "File Size: " + str(document.file_size))

            except (AttributeError, IndexError):
                pass

            try:
                voice = 'test/voice_record.mp3'
                resp = bot.send_voice(bot.chat_id, voice, duration=20, reply_markup='', reply_to_message_id='')
                voice = resp.voice

                print ("========== Parse response after sendVoice ================\n" +
                       "Voice file download link: " + str(bot.get_file(voice.file_id)) + "\n" +
                       "Duration: " + str(voice.duration) + "\n" +
                       "Mime type: " + str(voice.mime_type) + "\n" +
                       "File Size: " + str(voice.file_size))
            except (AttributeError, IndexError):
                pass

            try:
                # location found with this service http://www.mapcoordinates.net/en
                resp = bot.send_location(bot.chat_id, longitude=float(-21.90981746), latitude=float(64.54314655),
                                         reply_to_message_id='', reply_markup='')

                location = resp.location

                print ("========== Parse response after sendLocation ================\n" +
                       "Longitude = " + str(location.longitude) + "\n" +
                       "Latitude: " + str(location.latitude))
            except (AttributeError, IndexError):
                pass

            try:
                sticker_id = 'BQADAgADQAADyIsGAAGMQCvHaYLU_AI'
                resp = bot.send_sticker(bot.chat_id, sticker_id, '', '')
                sticker = resp.sticker

                print ("========== Parse response after sendSticker ================\n" +
                       "Sticker download link: " + str(bot.get_file(sticker.file_id)) + "\n" +
                       "Width: " + str(sticker.width) + "\n"
                       "Height: " + str(sticker.height) + "\n"
                       "File Size: " + str(sticker.file_size))

                resolution = str(sticker.thumb.width) + "x" + str(sticker.thumb.height)
                file_id = str(sticker.thumb.file_id)

                print "========== Parse thumbnail of sendSticker response =========="
                link = bot.get_file(file_id)
                print "Sticker thumbnail " + str(resolution)
                print link
                print "========================== WIN! ============================="
                exit(0)
            except (AttributeError, IndexError):
                pass
        else:
            pass
    except AttributeError:
        pass

if __name__ == '__main__':
    while True:
        main()

import telegrambot as tb
import unittest
import urlparse

# In order to run this unit tests on your bot and
# Telegram user account, please fill the following
# variables with values, corresponding to your

TOKEN = '152394201:AAE6wwKF-y9gddMrXUTAnGNbGrifJKFHU-I'
real_user_first_name = 'Roman'
real_user_last_name = 'Joe'
bot_first_name = 'Carl_bot'
bot_username = 'Carl_Carl_bot'

bot = tb.TelegramBot(token=TOKEN)


class TelegramBotTest(unittest.TestCase):

    """
    Feature: getMe method implementation from telegram bot API
    In order to test if the TOKEN is right
    Bot should send simple getMe method to
    receive response with description of himself
        Scenario: call getMe method
        Given: object of TelegramBot class with proper token
        When: getMe called
        Then: response with telegram API type of User received
        And: object of type User created and constructed
        And: checked through assertions of fields equality

    """
    def test_01_getMe(self):

        response = bot.get_me()
        self.assertIsNotNone(response)

    def test_02_get_updates(self):
        response = bot.get_updates()
        self.assertIsNotNone(response)

    def test_03_send_message(self):
        response = bot.send_message("Hello World!")
        self.assertIsNotNone(response)
        self.assertEqual('Hello World!', response.raw_message['text'])

    def test_04_send_photo(self):
        hello = 'test/hello.jpg'
        response = bot.send_photo(bot.chat_id,
                                  hello,
                                  caption='Hello \n it\'s me',
                                  reply_markup='',
                                  reply_to_message_id='')
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.raw_message['photo'])

    def test_05_send_audio(self):
        music = 'test/sample_audio.mp3'
        bot.send_chat_action(bot.chat_id, 'upload_audio')
        response = bot.send_audio(bot.chat_id,
                                  music,
                                  performer='Nu Gravity',
                                  title='People',
                                  reply_markup='')
        self.assertIsNotNone(response)
        self.assertEqual('audio/mpeg', response.raw_message['audio']['mime_type'])

    def test_06_send_document(self):
        document = 'test/LICENSE.pdf'
        response = bot.send_document(bot.chat_id, document, '', '')
        self.assertIsNotNone(response)
        self.assertEqual('application/pdf', response.raw_message['document']['mime_type'])

    def test_07_send_sticker(self):
        sticker_id = 'BQADAgADQAADyIsGAAGMQCvHaYLU_AI'
        response = bot.send_sticker(bot.chat_id, sticker_id, '', '')

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.raw_message['sticker']['thumb'])

    def test_08_send_voice(self):
        voice = 'test/voice_record.mp3'
        response = bot.send_voice(bot.chat_id,
                                  voice,
                                  duration=20,
                                  reply_markup='',
                                  reply_to_message_id='')

        self.assertIsNotNone(response)
        self.assertEqual('audio/mpeg', response.raw_message['voice']['mime_type'])

    def test_09_send_video(self):
        video = 'test/sample_video.mp4'
        response = bot.send_video(bot.chat_id, video,
                                  caption='Have some fun!',
                                  reply_markup='', reply_to_message_id='',
                                  duration=45)

        self.assertIsNotNone(response)
        self.assertEqual(45, response.raw_message['video']['duration'])

    def test_10_send_locations(self):
        # location found with this service http://www.mapcoordinates.net/en
        response = bot.send_location(bot.chat_id,
                                     longitude=float(-21.90981746),
                                     latitude=float(64.54314655),
                                     reply_to_message_id='',
                                     reply_markup='')
        self.assertIsNotNone(response)
        self.assertAlmostEqual(float(64.54314655),
                               response.raw_message['location']['latitude'], places=4)

    def test_11_get_file(self):
        file_id = "BQADAgADQAADyIsGAAGMQCvHaYLU_AI"

        response = bot.get_file(file_id)
        parsed = urlparse.urlparse(response)
        to_compare = '/file/bot' + TOKEN + '/document/file_630'
        self.assertEqual(to_compare, str(parsed[2]))

    def test_12_forward_message(self):
        res = bot.send_message("Forward")
        sent_message_id = int(res.message_id)
        response = bot.forward_message(bot.chat_id, bot.chat_id, sent_message_id)
        self.assertIsNotNone(response)
        self.assertEqual(bot_first_name, response.forward_from.first_name)
        self.assertEqual(response.message_id, sent_message_id + 1)

    def test_13_User(self):
        user_raw = {'username': bot_username, 'first_name': bot_first_name, 'id': 11223344}
        user = tb.User()
        user = user.from_json(user_raw)
        self.assertEqual(bot_username, user.username)
        self.assertEqual(bot_first_name, user.first_name)
        self.assertEqual(11223344, user.id)

    def test_14_Chat(self):
        chat_raw = {'first_name': real_user_first_name,
                    'last_name': real_user_last_name,
                    'type': 'private', 'id': 11223344}
        chat = tb.Chat()
        chat = chat.from_json(chat_raw)
        self.assertEqual(chat_raw['first_name'], chat.first_name)
        self.assertEqual(chat_raw['last_name'], chat.last_name)
        self.assertEqual(chat_raw['type'], chat.type)
        self.assertEqual(chat_raw['id'], chat.id)

    def test_15_PhotoSize(self):
        photo_raw = {'width': 90, 'height': 90,
                     'file_id': 'AgADAgADiKgxG9lZFQm4qp_yy4GhiHEagyoABFK11Vg4PdwQKjwAAgI',
                     'file_size': 1263}
        photo_size = tb.PhotoSize()
        photo_size = photo_size.from_json(photo_raw)
        self.assertEqual(photo_raw['width'], photo_size.width)
        self.assertEqual(photo_raw['height'], photo_size.height)
        self.assertEqual(photo_raw['file_id'], photo_size.file_id)
        self.assertEqual(photo_raw['file_size'], photo_size.file_size)

    def test_16_Voice(self):
        voice_raw = {'duration': 20,
                     'file_id': 'AwADAgADQgIAAtlZFQk8hHdbJQKRDAI',
                     'mime_type': 'audio/mpeg',
                     'file_size': 282547}
        voice = tb.Voice()
        voice = voice.from_json(voice_raw)
        self.assertEqual(voice_raw['duration'], voice.duration)
        self.assertEqual(voice_raw['file_id'], voice.file_id)
        self.assertEqual(voice_raw['mime_type'], voice.mime_type)
        self.assertEqual(voice_raw['file_size'], voice.file_size)

    def test_17_Audio(self):
        audio_raw = {'performer': 'Nu Gravity',
                     'title': 'People',
                     'file_id': 'BQADAgADQwIAAtlZFQl-JLBvpCb2JwI',
                     'file_size': 3005153,
                     'duration': 188,
                     'mime_type': 'audio/mpeg'}
        audio = tb.Audio()
        audio = audio.from_json(audio_raw)
        self.assertEqual(audio_raw['performer'], audio.performer)
        self.assertEqual(audio_raw['title'], audio.title)
        self.assertEqual(audio_raw['file_id'], audio.file_id)
        self.assertEqual(audio_raw['file_size'], audio.file_size)
        self.assertEqual(audio_raw['duration'], audio.duration)
        self.assertEqual(audio_raw['mime_type'], audio.mime_type)

    def test_18_Video(self):
        video_raw = {'duration': 45, 'width': 640,
                     'file_size': 917214,
                     'file_id': 'BAADAgADTwIAAtlZFQlRi0lUkQ0nDwI',
                     'height': 480}
        video = tb.Video()
        video = video.from_json(video_raw)
        self.assertEqual(video_raw['duration'], video.duration)
        self.assertEqual(video_raw['width'], video.width)
        self.assertEqual(video_raw['height'], video.height)
        self.assertEqual(video_raw['file_id'], video.file_id)
        self.assertEqual(video_raw['file_size'], video.file_size)

    def test_19_Sticker(self):
        sticker_raw = {'thumb': {'height': 90, 'file_path': 'thumb/file_564.jpg',
                                 'width': 63, 'file_id': 'AAQCABMbzlkqAAR-48dHTQ5BGXh-AAIC',
                                 'file_size': 2142}, 'height': 512, 'width': 362,
                                 'file_id': 'BQADAgADQAADyIsGAAGMQCvHaYLU_AI',
                                 'file_size': 36326, 'file_path': 'document/file_630'}
        sticker = tb.Sticker()
        sticker = sticker.from_json(sticker_raw)
        self.assertEqual(sticker_raw['width'], sticker.width)
        self.assertEqual(sticker_raw['height'], sticker.height)
        self.assertEqual(sticker_raw['file_id'], sticker.file_id)
        self.assertEqual(sticker_raw['file_size'], sticker.file_size)
        self.assertEqual(sticker_raw['file_path'], sticker.file_path)
        self.assertEqual(sticker_raw['thumb']['width'], sticker.thumb.width)
        self.assertEqual(sticker_raw['thumb']['height'], sticker.thumb.height)
        self.assertEqual(sticker_raw['thumb']['file_id'], sticker.thumb.file_id)
        self.assertEqual(sticker_raw['thumb']['file_size'], sticker.thumb.file_size)

    def test_20_Document(self):
        document_raw = {'file_name': 'LICENSE.pdf',
                        'file_id': 'BQADAgADUAIAAtlZFQn3aBlQqPEFMAI',
                        'mime_type': 'application/pdf', 'file_size': 239074}
        document = tb.Document()
        document = document.from_json(document_raw)
        self.assertEqual(document_raw['file_name'], document.file_name)
        self.assertEqual(document_raw['mime_type'], document.mime_type)
        self.assertEqual(document_raw['file_id'], document.file_id)
        self.assertEqual(document_raw['file_size'], document.file_size)

    def test_21_Location(self):
        location_raw = {'latitude': 64.543153, 'longitude': -21.909839}

        location = tb.Location()
        location = location.from_json(location_raw)
        self.assertAlmostEqual(location_raw['latitude'], location.latitude, places=4)
        self.assertAlmostEqual(location_raw['longitude'], location.longitude, places=4)


if __name__ == '__main__':
    unittest.main()

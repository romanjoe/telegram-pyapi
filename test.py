import telegrambot as tb
import unittest

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

    response = tb.Message()
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
    @classmethod
    def push_response(cls, resp):
        cls.response = resp

    @classmethod
    def pop_response(cls):
        return cls.response

    def test_getMe(self):

        response = bot.get_me()
        self.assertIsNotNone(response)

    def test_get_updates(self):
        response = bot.get_updates()
        self.assertIsNotNone(response)

    def test_send_message(self):
        response = bot.send_message("Hello World!")
        self.assertIsNotNone(response)
        self.assertEqual('Hello World!', response.raw_message['text'])

    def test_forward_message(self):
        pass

    def test_send_photo(self):
        hello = 'test/hello.jpg'
        response = bot.send_photo(bot.chat_id,
                                  hello,
                                  caption='Hello \n it\'s me',
                                  reply_markup='',
                                  reply_to_message_id='')
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.raw_message['photo'])

    def test_send_audio(self):
        music = 'test/sample_audio.mp3'
        bot.send_chat_action(bot.chat_id, 'upload_audio')
        response = bot.send_audio(bot.chat_id,
                                  music,
                                  performer='Nu Gravity',
                                  title='People',
                                  reply_markup='')
        self.assertIsNotNone(response)
        self.assertEqual('audio/mpeg', response.raw_message['audio']['mime_type'])

    def test_send_document(self):
        document = 'test/LICENSE.pdf'
        response = bot.send_document(bot.chat_id, document, '', '')
        self.assertIsNotNone(response)
        self.assertEqual('application/pdf', response.raw_message['document']['mime_type'])

    def test_send_sticker(self):
        sticker_id = 'BQADAgADQAADyIsGAAGMQCvHaYLU_AI'
        response = bot.send_sticker(bot.chat_id, sticker_id, '', '')

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.raw_message['sticker']['thumb'])

    def test_send_voice(self):
        voice = 'test/voice_record.mp3'
        response = bot.send_voice(bot.chat_id,
                                  voice,
                                  duration=20,
                                  reply_markup='',
                                  reply_to_message_id='')

        self.assertIsNotNone(response)
        self.assertEqual('audio/mpeg', response.raw_message['voice']['mime_type'])

    def test_send_locations(self):
        # location found with this service http://www.mapcoordinates.net/en
        response = bot.send_location(bot.chat_id,
                                     longitude=float(-21.90981746),
                                     latitude=float(64.54314655),
                                     reply_to_message_id='',
                                     reply_markup='')
        self.assertIsNotNone(response)
        self.assertAlmostEqual(float(64.54314655),
                               response.raw_message['location']['latitude'], places=4)

    # def test_User(self):
    #     re = self.pop_response()
    #     user_inst = tb.User()
    #     user = user_inst.from_json(re)
    #     self.assertEqual(user.first_name, bot_first_name)
    #     self.assertEqual(user.last_name, '')
    #     self.assertEqual(user.id, 152394201)  # bot derived id
    #     self.assertEqual(user.username, bot_username)

    #     self.assertEqual(response.text.text_message, "/start")
    #     self.assertIsNotNone(response.message_id)
    #     self.assertIsNotNone(response.chat.id)
    #     self.assertIsNotNone(response.date)
    #     self.assertIsNotNone(response.message_from)

    # def test_User_type(self):
    #     response = bot.get_updates()
    #     message = response.Update.from_json(response)
    #     user = message.message_from
    #     self.assertEqual(user.first_name, real_user_first_name)
    #     self.assertEqual(user.last_name, real_user_last_name)
    #     self.assertIsNotNone(user.id)
    #     self.assertEqual(user.username, '')


    #     message = tb.Message()
    #     message = message.from_json(response)
    #     self.assertEqual(message.text.text_message, "Hello World!")
    #

    #
    #
    #     resp = tb.Response.construct(resp)
    #     self.assertIsNotNone(resp.photo)
    #     self.assertEqual(resp.caption.text_message, "Hello \n it\'s me")
    #

    #
    #     resp = tb.Response.construct(resp)
    #     audio = resp.audio
    #     self.assertEqual(audio.title, 'People')
    #     self.assertEqual(audio.performer, 'Nu Gravity')
    #     self.assertEqual(audio.mime_type, 'audio/mpeg')
    #     self.assertIsNotNone(audio.file_id)
    #     self.assertIsNotNone(audio.file_size)
    #

    #
    #     resp = tb.Response.construct(resp)
    #     document = resp.document
    #     self.assertEqual(document.file_name, 'LICENSE.pdf')
    #     self.assertEqual(document.mime_type, 'application/pdf')
    #     self.assertIsNotNone(document.file_id)
    #     self.assertIsNotNone(document.file_size)
    #

    #
    #     resp = tb.Response.construct(resp)
    #     sticker = resp.sticker
    #     self.assertIsNotNone(resp.photo)
    #     self.assertEqual(sticker.file_id, 'BQADAgADQAADyIsGAAGMQCvHaYLU_AI')
    #     self.assertIsNotNone(sticker.width)
    #     self.assertIsNotNone(sticker.height)
    #     self.assertIsNotNone(sticker.file_id)
    #     self.assertIsNotNone(sticker.file_size)
    #
    # def test_send_video(self):
    #     video = 'test/sample_video.mp4'
    #     resp = bot.send_video(bot.chat_id, video,
    #                           caption='Have some fun!',
    #                           reply_markup='', reply_to_message_id='',
    #                           duration=45)
    #
    #     resp = tb.Response.construct(resp)
    #     video = resp.video
    #     self.assertIsNotNone(video.duration)
    #     self.assertEqual(video.mime_type, '')
    #     self.assertIsNotNone(resp.photo)
    #     self.assertIsNotNone(video.file_id)
    #     self.assertIsNotNone(video.width)
    #     self.assertIsNotNone(video.height)
    #     self.assertIsNotNone(video.file_id)
    #     self.assertIsNotNone(video.file_size)
    #

    #
    #     resp = tb.Response.construct(resp)
    #     voice = resp.voice
    #     self.assertIsNotNone(voice.duration)
    #     self.assertEqual(voice.mime_type, 'audio/mpeg')
    #     self.assertIsNotNone(voice.file_id)
    #     self.assertIsNotNone(voice.duration)
    #     self.assertIsNotNone(voice.file_id)
    #     self.assertIsNotNone(voice.file_size)
    #
    #
    #
    #     resp = tb.Response.construct(resp)
    #     location = resp.location
    #     self.assertGreaterEqual(location.latitude, float(64.54314655))
    #     self.assertLessEqual(location.longitude, float(-21.90981746))

if __name__ == '__main__':
    unittest.main()

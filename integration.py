import telegrambot as tb
import unittest
import urllib2

# In order to run this unit tests on your bot and
# Telegram user account, please fill the following
# variables with values, corresponding to your

TOKEN = '152394201:AAE6wwKF-y9gddMrXUTAnGNbGrifJKFHU-I'
real_user_first_name = 'Roman'
real_user_last_name = 'Joe'
master_id = 162457279
bot_first_name = 'Carl_bot'
bot_username = 'Carl_Carl_bot'

bot = tb.TelegramBot(token=TOKEN)


class TelegramBotIntegrationTests(unittest.TestCase):
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
    def test_getMe(self):

        response = bot.get_me()
        self.assertIsNotNone(response)

    def test_1_set_master(self):
        bot.set_master()
        print "---"

    def test_get_updates(self):
        response = bot.get_updates()
        self.assertIsNotNone(response)

    def test_send_message(self):
        res = bot.get_updates()
        response = bot.send_message("Hello World!")
        self.assertIsNotNone(response)
        self.assertEqual('Hello World!', response.raw_message['text'])

    def test_forward_message(self):
        res = bot.get_updates()
        res = bot.send_message("Forward")
        sent_message_id = int(res.message_id)
        response = bot.forward_message(bot.chat_id, bot.chat_id, sent_message_id)
        self.assertIsNotNone(response)
        self.assertEqual(bot_first_name, response.forward_from.first_name)
        self.assertEqual(response.message_id, sent_message_id + 1)

    # def test_send_photo(self):
    #     res = bot.get_updates()
    #     hello = 'test/hello.jpg'
    #     response = bot.send_photo(bot.chat_id,
    #                               hello,
    #                               caption='Hello \n it\'s me',
    #                               reply_markup='',
    #                               reply_to_message_id='')
    #     self.assertIsNotNone(response)
    #     self.assertIsNotNone(response.raw_message['photo'])
    #
    # def test_send_audio(self):
    #     res = bot.get_updates()
    #     music = 'test/sample_audio.mp3'
    #     bot.send_chat_action(bot.chat_id, 'upload_audio')
    #     response = bot.send_audio(bot.chat_id,
    #                               music,
    #                               performer='Nu Gravity',
    #                               title='People',
    #                               reply_markup='')
    #     self.assertIsNotNone(response)
    #     self.assertEqual('audio/mpeg', response.raw_message['audio']['mime_type'])
    #
    # def test_send_document(self):
    #     res = bot.get_updates()
    #
    #     document = 'test/LICENSE.pdf'
    #     response = bot.send_document(bot.chat_id, document, '', '')
    #     self.assertIsNotNone(response)
    #     self.assertEqual('application/pdf', response.raw_message['document']['mime_type'])
    #
    # def test_send_sticker(self):
    #     res = bot.get_updates()
    #     sticker_id = 'BQADAgADQAADyIsGAAGMQCvHaYLU_AI'
    #     response = bot.send_sticker(bot.chat_id, sticker_id, '', '')
    #
    #     self.assertIsNotNone(response)
    #     self.assertIsNotNone(response.raw_message['sticker']['thumb'])
    #
    # def test_send_voice(self):
    #     res = bot.get_updates()
    #     voice = 'test/voice_record.mp3'
    #     response = bot.send_voice(bot.chat_id,
    #                               voice,
    #                               duration=20,
    #                               reply_markup='',
    #                               reply_to_message_id='')
    #
    #     self.assertIsNotNone(response)
    #     self.assertEqual('audio/mpeg', response.raw_message['voice']['mime_type'])
    #
    # def test_send_video(self):
    #     res = bot.get_updates()
    #     video = 'test/sample_video.mp4'
    #     response = bot.send_video(bot.chat_id, video,
    #                               caption='Have some fun!',
    #                               reply_markup='', reply_to_message_id='',
    #                               duration=45)
    #
    #     self.assertIsNotNone(response)
    #     self.assertEqual(45, response.raw_message['video']['duration'])
    #
    # def test_send_locations(self):
    #     res = bot.get_updates()
    #     # location found with this service http://www.mapcoordinates.net/en
    #     response = bot.send_location(bot.chat_id,
    #                                  longitude=float(-21.90981746),
    #                                  latitude=float(64.54314655),
    #                                  reply_to_message_id='',
    #                                  reply_markup='')
    #     self.assertIsNotNone(response)
    #     self.assertAlmostEqual(float(64.54314655),
    #                            response.raw_message['location']['latitude'], places=4)
    #
    # def test_get_file(self):
    #     res = bot.get_updates()
    #     file_id = "BQADAgADQAADyIsGAAGMQCvHaYLU_AI"
    #
    #     response = bot.get_file(file_id)
    #     resp = urllib2.urlopen(str(response))
    #     self.assertEqual(200, resp.code)

if __name__ == '__main__':
    unittest.main()
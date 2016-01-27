import telegrambot as tb
import unittest

TOKEN = '152394201:AAE6wwKF-y9gddMrXUTAnGNbGrifJKFHU-I'
real_user_first_name = 'Roman'
real_user_last_name = 'Joe'
bot_first_name = 'Carl_bot'
bot_username = 'Carl_Carl_bot'

BLANK_STR_VAL = ''


class TelegramBotTest(unittest.TestCase):

    def test_User_Full_Params_List(self):
        user_raw = {'username': bot_username,
                    'last_name': real_user_last_name,
                    'first_name': real_user_first_name,
                    'id': 11223344}
        user = tb.User()
        user = user.from_json(user_raw)

        self.assertIsNotNone(user)
        self.assertEqual(user_raw['id'], user.id)
        self.assertEqual(bot_username, user.username)
        self.assertEqual(real_user_first_name, user.first_name)
        self.assertEqual(real_user_last_name, user.last_name)

    def test_User_Without_Optional_Params(self):
        user_raw = {'first_name': real_user_first_name,
                    'id': 11223344}
        user = tb.User()
        user = user.from_json(user_raw)

        self.assertIsNotNone(user)
        self.assertEqual(user_raw['id'], user.id)
        self.assertEqual(BLANK_STR_VAL, user.username)
        self.assertEqual(real_user_first_name, user.first_name)
        self.assertEqual(BLANK_STR_VAL, user.last_name)

    def test_Chat_Full_Params_List(self):
        chat_raw = {'first_name': real_user_first_name,
                    'last_name': real_user_last_name,
                    'type': 'private', 'id': 11223344, 'username': bot_username,
                    'title': 'simple chat'}
        chat = tb.Chat()
        chat = chat.from_json(chat_raw)

        self.assertIsNotNone(chat)
        self.assertEqual(chat_raw['first_name'], chat.first_name)
        self.assertEqual(chat_raw['last_name'], chat.last_name)
        self.assertEqual(chat_raw['type'], chat.chat_type)
        self.assertEqual(chat_raw['id'], chat.id)
        self.assertEqual(chat_raw['title'], chat.title)
        self.assertEqual(chat_raw['username'], chat.username)

    def test_Chat_Without_Optional_Params(self):
        chat_raw = {'type': 'private', 'id': 11223344}
        chat = tb.Chat()
        chat = chat.from_json(chat_raw)

        self.assertIsNotNone(chat)
        self.assertEqual(BLANK_STR_VAL, chat.first_name)
        self.assertEqual(BLANK_STR_VAL, chat.last_name)
        self.assertEqual(chat_raw['type'], chat.chat_type)
        self.assertEqual(chat_raw['id'], chat.id)
        self.assertEqual(BLANK_STR_VAL, chat.title)
        self.assertEqual(BLANK_STR_VAL, chat.username)


class TelegramBotMediaObjTest(unittest.TestCase):

    def test_Media(self):

        raw_media = {'file_id': 'AgADAgADiKgxG9lZFQm4qp_yy4GhiHEagyoABFK11Vg4PdwQKjwAAgI',
                     'file_size': 1263, 'mime_type': 'some/type'}
        media_object = tb.Media()
        media_object.from_json(raw_media)

        self.assertIsNotNone(media_object)
        self.assertEqual(raw_media['file_id'], media_object.file_id)
        self.assertEqual(raw_media['file_size'], media_object.file_size)
        self.assertEqual(raw_media['mime_type'], media_object.mime_type)

    def test_PhotoSize_Full_Params_List(self):
        photo_raw = {'width': 90, 'height': 90,
                     'file_id': 'AgADAgADiKgxG9lZFQm4qp_yy4GhiHEagyoABFK11Vg4PdwQKjwAAgI',
                     'file_size': 1263}
        photo_size = tb.PhotoSize()
        photo_size = photo_size.from_json(photo_raw)

        self.assertIsNotNone(photo_size)
        self.assertEqual(photo_raw['width'], photo_size.width)
        self.assertEqual(photo_raw['height'], photo_size.height)
        self.assertEqual(photo_raw['file_id'], photo_size.file_id)
        self.assertEqual(photo_raw['file_size'], photo_size.file_size)

    def test_PhotoSize_Without_Optional_Params(self):
        photo_raw = {'width': 90, 'height': 90,
                     'file_id': 'AgADAgADiKgxG9lZFQm4qp_yy4GhiHEagyoABFK11Vg4PdwQKjwAAgI'}
        photo_size = tb.PhotoSize()
        photo_size = photo_size.from_json(photo_raw)

        self.assertEqual(photo_raw['width'], photo_size.width)
        self.assertEqual(photo_raw['height'], photo_size.height)
        self.assertEqual(photo_raw['file_id'], photo_size.file_id)
        self.assertEqual(0, photo_size.file_size)

    def test_Voice_Full_Params_List(self):
        voice_raw = {'duration': 20,
                     'file_id': 'AwADAgADQgIAAtlZFQk8hHdbJQKRDAI',
                     'mime_type': 'audio/mpeg',
                     'file_size': 282547}
        voice = tb.Voice()
        voice = voice.from_json(voice_raw)

        self.assertIsNotNone(voice)
        self.assertEqual(voice_raw['duration'], voice.duration)
        self.assertEqual(voice_raw['file_id'], voice.file_id)
        self.assertEqual(voice_raw['mime_type'], voice.mime_type)
        self.assertEqual(voice_raw['file_size'], voice.file_size)

    def test_Voice_Without_Optional_Params(self):
        voice_raw = {'duration': 20,
                     'file_id': 'AwADAgADQgIAAtlZFQk8hHdbJQKRDAI'}
        voice = tb.Voice()
        voice = voice.from_json(voice_raw)

        self.assertIsNotNone(voice)
        self.assertEqual(voice_raw['duration'], voice.duration)
        self.assertEqual(voice_raw['file_id'], voice.file_id)
        self.assertEqual(BLANK_STR_VAL, voice.mime_type)
        self.assertEqual(0, voice.file_size)

    def test_Audio_Full_Params_List(self):
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

    def test_Audio_Without_Optional_Params(self):
        audio_raw = {'file_id': 'BQADAgADQwIAAtlZFQl-JLBvpCb2JwI',
                     'duration': 188}
        audio = tb.Audio()
        audio = audio.from_json(audio_raw)

        self.assertEqual(BLANK_STR_VAL, audio.performer)
        self.assertEqual(BLANK_STR_VAL, audio.title)
        self.assertEqual(0, audio.file_size)
        self.assertEqual(BLANK_STR_VAL, audio.mime_type)

    def test_Video_Full_Params_List(self):
        video_raw = {'duration': 45, 'width': 640,
                     'file_size': 917214, 'thumb': {'width': 90, 'height': 90,
                                                    'file_id': 'AgADAgADiKgxG9lZFQm4qp_y',
                                                    'file_size': 1112},
                     'file_id': 'BAADAgADTwIAAtlZFQlRi0lUkQ0nDwI',
                     'height': 480}
        video = tb.Video()
        video = video.from_json(video_raw)

        self.assertEqual(video_raw['duration'], video.duration)
        self.assertEqual(video_raw['width'], video.width)
        self.assertEqual(video_raw['height'], video.height)
        self.assertEqual(video_raw['file_id'], video.file_id)
        self.assertEqual(video_raw['file_size'], video.file_size)
        self.assertEqual(video_raw['thumb']['width'], video.thumb.width)
        self.assertEqual(video_raw['thumb']['height'], video.thumb.height)
        self.assertEqual(video_raw['thumb']['file_id'], video.thumb.file_id)
        self.assertEqual(video_raw['thumb']['file_size'], video.thumb.file_size)

    def test_Video_Without_Optional_Params(self):
        video_raw = {'file_id': 'BAADAgADTwIAAtlZFQlRi0lUkQ0nDwI'}
        video = tb.Video()
        video = video.from_json(video_raw)

        self.assertIsNotNone(video.thumb)
        self.assertEqual(0, video.duration)
        self.assertEqual(0, video.width)
        self.assertEqual(0, video.height)
        self.assertEqual(0, video.file_size)

    def test_Sticker_Full_Params_List(self):
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

    def test_Sticker_Without_Optional_Params(self):
        sticker_raw = {'height': 512, 'width': 362,
                                 'file_id': 'BQADAgADQAADyIsGAAGMQCvHaYLU_AI',
                                 'file_path': 'document/file_630'}
        sticker = tb.Sticker()
        sticker = sticker.from_json(sticker_raw)

        self.assertIsNotNone(sticker.thumb)
        self.assertEqual(0, sticker.file_size)
        self.assertEqual(sticker_raw['file_path'], sticker.file_path)

    def test_Document_Full_Params(self):
        document_raw = {'file_name': 'LICENSE.pdf',
                        'file_id': 'BQADAgADUAIAAtlZFQn3aBlQqPEFMAI',
                        'mime_type': 'application/pdf', 'file_size': 239074}
        document = tb.Document()
        document = document.from_json(document_raw)

        self.assertEqual(document_raw['file_name'], document.file_name)
        self.assertEqual(document_raw['mime_type'], document.mime_type)
        self.assertEqual(document_raw['file_id'], document.file_id)
        self.assertEqual(document_raw['file_size'], document.file_size)

    def test_Document_Without_Optional_Params(self):
        document_raw = {'file_id': 'BQADAgADUAIAAtlZFQn3aBlQqPEFMAI'}
        document = tb.Document()
        document = document.from_json(document_raw)

        self.assertEqual(BLANK_STR_VAL, document.file_name)
        self.assertEqual(BLANK_STR_VAL, document.mime_type)
        self.assertEqual(0, document.file_size)

    def test_Location(self):
        location_raw = {'latitude': 64.543153, 'longitude': -21.909839}

        location = tb.Location()
        location = location.from_json(location_raw)

        self.assertAlmostEqual(location_raw['latitude'], location.latitude, places=4)
        self.assertAlmostEqual(location_raw['longitude'], location.longitude, places=4)

    # def test_Message_Humanize_date(self):
    #     sample_time_in_unix_format = 1451421039
    #     expected_after_conversion = '2015-12-29 22:30:39'
    #     date = tb.Message.humanize_date(sample_time_in_unix_format)
    #
    #     self.assertEqual(expected_after_conversion, date)

    def test_Message_With_Text(self):
        message_raw = {'date': 1451421039,
                       'text': 'This is test message',
                       'from': {'first_name': 'Roman',
                                'last_name': 'Joe', 'id': 162457279},
                       'message_id': 2656, 'chat': {'first_name': 'Roman',
                                                    'last_name': 'Joe', 'type': 'private',
                                                    'id': 162457279}}
        message = tb.Message()
        message = message.from_json(message_raw)
        self.assertEqual(message_raw['message_id'], 2656)
        self.assertEqual(message_raw['text'], message.text.text_message)
        self.assertEqual(message_raw['from']['first_name'], message.message_from.first_name)
        self.assertEqual(message_raw['from']['last_name'], message.message_from.last_name)
        self.assertEqual(message_raw['from']['id'], message.message_from.id)
        self.assertEqual(message_raw['chat']['first_name'], message.chat.first_name)
        self.assertEqual(message_raw['chat']['last_name'], message.chat.last_name)
        self.assertEqual(message_raw['chat']['id'], message.chat.id)

    def test_Update(self):
        update_raw = {'message': {'date': 1451421039,
                                  'text': 'This is test message',
                                  'from': {'first_name': 'Roman',
                                           'last_name': 'Joe', 'id': 162457279},
                                  'message_id': 2656, 'chat': {'first_name': 'Roman',
                                                               'last_name': 'Joe', 'type': 'private',
                                                               'id': 162457279}},
                      'update_id': 67525620}

        update = tb.Update()
        update = update.from_json(update_raw)

        self.assertIsNotNone(update.message)
        self.assertEqual(update_raw['update_id'], update.update_id)

if __name__ == '__main__':
    unittest.main()

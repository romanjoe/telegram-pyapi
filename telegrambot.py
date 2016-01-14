import exceptions
import time
from abc import ABCMeta
from datetime import datetime as dt

import requests

DEBUG = False


class Telegram(object):

    """
    Abstract class
    """

    __metaclass__ = ABCMeta

    API_BASE = 'https://api.telegram.org/bot'

    def __init__(self, token):
        self.token = token
        self.url_token = self.API_BASE + token

    def post_request(self, data, files, api_call):

        response = requests.post(self.url_token +
                                 api_call, files=files, data=data)

        if response.json()['ok'] is not True:
            print " ++++ Bad request, 'ok' field in response was False"

        if not response.status_code == 200:
            return False

        # TODO add raise exceptions for other codes

        return response.json()['result']

    @staticmethod
    def construct(update):

        if type(update) is bool:
            print " ++++ Update has not been received"
           #exit(-1)

        if 'message' in update:
            try:
                update_object = Update()
                return update_object.from_json(update=update)
            except KeyError:
                pass
        else:
            try:
                message_object = Message()
                message_object.raw_message = update
                return message_object.from_json(response=message_object.raw_message)
            except KeyError:
                pass


class TelegramBot(Telegram):

    """
    Telegram bot class, implements API calls
    """

    offset = 0
    chat_id = 0
    master_id = 0
    master_pass = '12345'
    last_update = ''

    api = {'getMe': '/getMe',
           'sendMessage': '/sendMessage',
           'forwardMessage': '/forwardMessage',
           'sendPhoto': '/sendPhoto',
           'sendAudio': '/sendAudio',
           'sendDocument': '/sendDocument',
           'sendSticker': '/sendSticker',
           'sendVideo': '/sendVideo',
           'sendVoice': '/sendVoice',
           'sendLocation': '/sendLocation',
           'sendChatAction': '/sendChatAction',
           'getUpdates': '/getUpdates',
           'setWebhook': '/setWebhook',
           'getFile': '/getFile'}

    def __init__(self, token):
        Telegram.__init__(self, token=token)
        self.token = token
        self.offset = 0
        self.chat_id = 0

    def set_master(self):

        """
        This method allows you to assign a master user ID by a password
        provided in a message. Then you can use self.master_id for
        authentication before handling some commands.
        This is useful if you are going to use a bot for triggering some
        events, which should have some amount of secure.
        :return: bool result of operation
        """

        update = self.get_updates()
        try:
            password = update.message.text.text_message

            if password == self.master_pass:
                self.master_id = update.message.message_from.id
                self.send_message("Password is correct! Hello, master!")
                return True
            else:
                self.send_message("Wrong password, you are no a master!")
                return False
        except AttributeError:
            return False

    def get_me(self):

        data = {}
        return self.post_request(data, '', self.api['getMe'])

    def send_message(self, text):

        """
        Method to send text messages
        APIdoc URL: https://core.telegram.org/bots/api#sendmessage

        :param text: message to send
        :return: Message json object type
        refference - https://core.telegram.org/bots/api#message
        """
        if self.chat_id is 0:
            data = {'chat_id': self.master_id, 'text': text}
        else:
            data = {'chat_id': self.chat_id, 'text': text}
        response = self.post_request(data, '', self.api['sendMessage'])
        return self.construct(response)

    def forward_message(self, chat_id, from_chat_id, message_id):

        """
        Method for forwarding messages, using id's

        APIdoc URL: https://core.telegram.org/bots/api#forwardmessage

        :param chat_id: from what chat to forward
        :param from_chat_id: to which chat forward
        :param message_id: which message to forward
        :return: Message json object with sent message
        """
        data = {'chat_id': chat_id, 'from_chat_id': from_chat_id,
                'message_id': message_id}
        response = self.post_request(data, '', self.api['forwardMessage'])
        return self.construct(response)

    def send_photo(self, chat_id, photo, caption='',
                   reply_to_message_id='', reply_markup=''):

        """
        Send photo by id (already uploaded to telegram) or as object of this
        type https://core.telegram.org/bots/api#inputfile

        APIdoc URL: https://core.telegram.org/bots/api#sendphoto

        :param chat_id: must
        :param photo: must
        :param caption: optional
        :param reply_to_message_id: optional
        :param reply_markup: optional
        :return: constructed object of type Message
        """
        self.send_chat_action(self.chat_id, 'upload_photo')

        data = {'chat_id': chat_id, 'caption': caption,
                'reply_to_message_id': reply_to_message_id,
                'reply_markup': reply_markup}

        files = {'photo': (photo, open(photo, 'rb'))}

        response = self.post_request(data, files, self.api['sendPhoto'])
        return self.construct(response)

    def send_audio(self, chat_id, audio, duration='',
                   performer='', title='', reply_to_message_id='',
                   reply_markup=''):

        """
        Send audio by id (already uploaded to telegram) or as object of this
        type https://core.telegram.org/bots/api#inputfile

        APIdoc URL: https://core.telegram.org/bots/api#sendaudio

        :param chat_id: must
        :param audio: must
        :param duration: optional
        :param performer: optional
        :param title: optional
        :param reply_to_message_id: optional
        :param reply_markup: optional
        :return: Message json object with sent message
        """
        self.send_chat_action(self.chat_id, 'upload_audio')

        data = {'chat_id': chat_id, 'duration': duration,
                'performer': performer, 'title': title,
                'reply_to_message_id': reply_to_message_id,
                'reply_markup': reply_markup}
        files = {'audio': (open(audio, 'rb'))}

        response = self.post_request(data, files, self.api['sendAudio'])
        return self.construct(response)

    def send_document(self, chat_id, document, reply_to_message_id,
                      reply_markup):
        """
        Send document by id (already uploaded to telegram) or as object of this
        type https://core.telegram.org/bots/api#inputfile

        APIdoc URL: https://core.telegram.org/bots/api#senddocument

        :param chat_id: must
        :param document: must
        :param reply_to_message_id: optional
        :param reply_markup: optional
        :return: Message json object with sent message
        """

        self.send_chat_action(self.chat_id, 'upload_document')

        data = {'chat_id': chat_id,  # 'document': document,
                'reply_to_message_id': reply_to_message_id,
                'reply_markup': reply_markup}
        files = {'document': (document, open(document, 'rb'))}

        response = self.post_request(data, files, self.api['sendDocument'])
        return self.construct(response)

    def send_sticker(self, chat_id, sticker, reply_to_message_id,
                     reply_markup):
        """
        Send sticker by id (already uploaded to telegram) or as object of this
        type https://core.telegram.org/bots/api#inputfile

        APIdoc URL: https://core.telegram.org/bots/api#sendsticker

        :param chat_id: must
        :param sticker: must
        :param reply_to_message_id: optional
        :param reply_markup: optional
        :return: Message json object with sent message
        """

        data = {'chat_id': chat_id, 'sticker': sticker,
                'reply_to_message_id': reply_to_message_id,
                'reply_markup': reply_markup}

        response = self.post_request(data, '', self.api['sendSticker'])
        return self.construct(response)

    def send_video(self, chat_id, video, duration=0,
                   caption='', reply_to_message_id='',
                   reply_markup=''):

        """
        Send video by id (already uploaded to telegram) or as object of this
        type https://core.telegram.org/bots/api#inputfile

        APIdoc URL: https://core.telegram.org/bots/api#sendvideo

        :param chat_id: must
        :param video: must
        :param duration: optional
        :param caption: optional
        :param reply_to_message_id: optional
        :param reply_markup: optional
        :return: Message json object with sent message
        """

        self.send_chat_action(self.chat_id, 'upload_video')

        data = {'chat_id': chat_id, 'duration': duration, 'caption': caption,
                'reply_to_message_id': reply_to_message_id,
                'reply_markup': reply_markup}
        files = {'video': (video, open(video, 'rb'))}

        response = self.post_request(data, files, self.api['sendVideo'])
        return self.construct(response)

    def send_voice(self, chat_id, voice, duration='',
                   reply_to_message_id='', reply_markup=''):

        """
        Send voice by id (already uploaded to telegram) or as object of this
        type https://core.telegram.org/bots/api#inputfile

        APIdoc URL: https://core.telegram.org/bots/api#sendvoice

        :param chat_id: must
        :param voice: must
        :param duration: optional
        :param reply_to_message_id: optional
        :param reply_markup: optional
        :return: Message json object with sent message
        """

        self.send_chat_action(self.chat_id, 'record_audio')

        data = {'chat_id': chat_id, 'duration': duration,
                'reply_to_message_id': reply_to_message_id,
                'reply_markup': reply_markup}

        files = {'voice': (voice, open(voice, 'rb'))}
        response = self.post_request(data, files, self.api['sendVoice'])
        return self.construct(response)

    def send_location(self, chat_id, latitude, longitude,
                      reply_to_message_id='', reply_markup=''):

        """
        Send latitude by id (already uploaded to telegram) or as object of this
        type https://core.telegram.org/bots/api#inputfile

        APIdoc URL: https://core.telegram.org/bots/api#sendlocation

        :param chat_id: must
        :param latitude: must
        :param longitude: must
        :param reply_to_message_id: optional
        :param reply_markup: optional
        :return: Message json object with sent message
        """

        self.send_chat_action(self.chat_id, 'find_location')

        data = {'chat_id': chat_id, 'latitude': latitude,
                'longitude': longitude,
                'reply_to_message_id': reply_to_message_id,
                'reply_markup': reply_markup}

        response = self.post_request(data, '', self.api['sendLocation'])
        return self.construct(response)

    def send_chat_action(self, chat_id, action):

        """
        This method can tell bot what to do if he need some time to process
        request, for example to record and upload video

        :param chat_id:
        :param action: Types of action to broadcast:
                        @typing@ for text messages
                        @upload_photo@ for photos
                        @record_video@ or @upload_video@ for videos
                        @record_audio@ or @upload_audio@ for audio files
                        @upload_document@ for general files
                        @find_location@ for location data.
        :return: Message json object with sent message
        """

        data = {'chat_id': chat_id, 'action': action}
        return self.post_request(data, '', self.api['sendChatAction'])

    def get_updates(self, limit=1):

        """
        This method for receiving array of updates
        Link for description: https://core.telegram.org/bots/api#getupdates

        :parameter limit: sets maximum amount of messages to request.
                          default = 1
        :return: If limit parameter equals 1, as in default case -
                 single update_object returned
                 if limit parameter is bigger than one, then an Array of
                 updates_objects returned
                 https://core.telegram.org/bots/api#update
        """

        data = {'offset': self.offset + 1, 'limit': limit, 'timeout': 0}
        updates = self.post_request(data, '', self.api['getUpdates'])

        if limit == 1:
            try:
                single_update_object = self.construct(updates[0])

                self.offset = updates[0]['update_id']
                self.chat_id = updates[0]['message']['chat']['id']

                return single_update_object

            except IndexError:

                return []

        elif limit > 1:

            array_of_updates_objects = []

            for update in updates:
                array_of_updates_objects.append(Update(update))
                self.offset = update['update_id']
                self.chat_id = update['message']['chat']['id']

            return array_of_updates_objects

        elif limit == 0:
            raise exceptions.ValueError("[MESSAGE] Cant retrieve 0 updates, \
                                         please, specify value bigger than 1"
                                        " to get_updates() method or leave it"
                                        " blank to retrieve first of unread \
                                        updates")

    def get_file(self, file_id):

        """
        This method return a download link for a requested file by id

        :param file_id:
        :return: download link for requested file
        """

        data = {'file_id': file_id}
        message = self.post_request(data, '', self.api['getFile'])
        file_path = message['file_path']

        download_link = ('https://api.telegram.org/file/bot' +
                         self.token + "/" + file_path)

        return download_link


class User(object):

    """
    This object represents a Telegram user or bot
    """

    def __init__(self,  user_id=0, first_name='', last_name='', username=''):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def from_json(self, user):

        self.id = user['id']
        self.first_name = user['first_name']
        # the following parameters are optional
        try:
            self.last_name = user['last_name']
        except KeyError:
            pass
        try:
            self.username = user['username']
        except KeyError:
            pass

        return self


class Chat(object):

    """
    This object represents a chat
    """

    def __init__(self, chat_id=0, chat_type='',
                 first_name='', last_name='', username='',
                 title=''):

        self.id = chat_id
        self.chat_type = chat_type
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.title = title

    def from_json(self, chat):

        self.id = chat['id']
        self.chat_type = chat['type']

        # the following parameters are optional
        try:
            self.last_name = chat['last_name']
        except KeyError:
            pass
        try:
            self.first_name = chat['first_name']
        except KeyError:
            pass
        try:
            self.title = chat['title']
        except KeyError:
            pass
        try:
            self.username = chat['username']
        except KeyError:
            pass

        return self


class Media(object):

    """
    Abstract class to combine same attributes
    """

    __metaclass__ = ABCMeta

    def __init__(self, file_id='', file_size=0, mime_type=''):
        self.file_id = file_id
        self.file_size = file_size
        self.mime_type = mime_type

    def from_json(self, media):

        self.file_id = media['file_id']

        try:
            self.file_size = media['file_size']
        except KeyError:
            pass
        try:
            self.mime_type = media['mime_type']
        except KeyError:
            pass
        return self

    @staticmethod
    def get_thumb(media):

        try:
            thumbnail = PhotoSize()
            return thumbnail.from_json(media['thumb'])
        except KeyError:
            return PhotoSize()


class Voice(Media):

    """
    This object represents a voice note.
    """

    duration = 0

    def __init__(self):
        super(Voice, self).__init__()

    def from_json(self, voice):

        super(Voice, self).from_json(voice)
        try:
            self.duration = voice['duration']
        except KeyError:
            pass
        return self


class Audio(Voice):

    """
    This object represents an audio file to be treated as music
    by the Telegram clients.
    """

    performer = ''
    title = ''

    def __init__(self):
        super(Audio, self).__init__()

    def from_json(self, audio):

        super(Audio, self).from_json(audio)
        try:
            self.performer = audio['performer']
        except KeyError:
            pass
        try:
            self.title = audio['title']
        except KeyError:
            pass

        return self


class PhotoSize(Media):

    """
    This object represents one size of a photo or a file / sticker thumbnail
    """
    # attributes:
    width = 0
    height = 0

    def from_json(self, photo_size):

        super(PhotoSize, self).from_json(photo_size)
        try:
            self.width = photo_size['width']
            self.height = photo_size['height']
        except KeyError:
            pass

        return self


class Sticker(PhotoSize):

    """
    This object represents a sticker.
    """
    file_path = ''
    thumb = PhotoSize()

    def __init__(self):
        super(Sticker, self).__init__()

    def from_json(self, sticker):

        super(Sticker, self).from_json(sticker)
        self.thumb = Media.get_thumb(sticker)
        try:
            self.file_path = sticker['file_path']
        except KeyError:
            pass
        return self


class Document(Sticker):

    """
    This object represents a general file (as opposed to photos, voice messages
    and audio files).
    """

    thumb = PhotoSize()
    file_name = ''

    def __init__(self):
        super(Document, self).__init__()

    def from_json(self, document):

        super(Document, self).from_json(document)
        try:
            self.file_name = document['file_name']
        except:
            pass
        self.thumb = Media.get_thumb(document)

        return self


class Video(Voice, Sticker):

    def __init__(self):
        Sticker.__init__(self)

    def from_json(self, video):

        Voice.from_json(self, voice=video)
        Sticker.from_json(self, sticker=video)

        return self


class Text(object):

    """
    This object represents a text field in Message()
    """

    text_message = ''

    def __init__(self, message=''):
        self.text_message = message

    def from_json(self, plain_text):
        # TODO make is possible to process russian and ukrainian letters
        #self.text_message = unicode(plain_text, 'utf-8')
        self.text_message = plain_text
        return self


class Location(Media):

    """
    This object represents a point on the map.
    """

    longitude = 0.0
    latitude = 0.0

    def __init__(self, longitude=0.0, latitude=0.0):
        self.longitude = longitude
        self.latitude = latitude

    def from_json(self, location):

        self.longitude = location['longitude']
        self.latitude = location['latitude']

        return self


class Message(Media):

    """
    This object represents a message
    """
    raw_message = ''
    # TODO to be added in future
    # new_chat_participant = ''
    # left_chat_participant = ''
    # new_chat_title = ''
    # new_chat_photo = ''
    # group_chat_created = ''
    # supergroup_chat_created = ''
    # channel_chat_created = ''
    # migrate_to_chat_id = ''
    # migrate_from_chat_id = ''

    def __init__(self,
                 message_id=0,
                 message_from=User(),
                 date='',
                 chat=Chat(),
                 forward_from=User(),
                 forward_date='',
                 # reply_to_message='',
                 text=Text(),
                 audio=Audio(),
                 document=Document(),
                 photo=[],
                 sticker=Sticker(),
                 video=Video(),
                 voice=Voice(),
                 caption='',
                 # contact=Contact(),
                 location=Location()
                 ):
        self.message_id = message_id
        self.message_from = message_from
        self.date = date
        self.chat = chat
        self.text = text
        self.forward_from = forward_from
        self.forward_date = forward_date
        # self.reply_to_message =
        self.audio = audio
        self.document = document
        self.photo = photo
        self.sticker = sticker
        self.video = video
        self.voice = voice
        self.caption = caption
        # self.contact = contact
        self.location = location

    def from_json(self, response):

        try:
            self.message_id = response['message_id']
        except (KeyError, TypeError):
            pass

        try:
            self.date = response['date']
        except (KeyError, TypeError):
            pass

        try:
            from_user = User()
            self.message_from = from_user.from_json(response['from'])
        except (KeyError, TypeError):
            pass

        try:
            forwarded_from_user = User().from_json(response['forward_from'])
            self.forward_from = forwarded_from_user
        except (KeyError, TypeError):
            pass

        try:
            self.date = self.humanize_date(response['date'])
        except (KeyError, TypeError):
            pass

        try:
            self.forward_date = self.humanize_date(
                response['forward_date'])
        except (KeyError, TypeError):
            pass

        try:
            chat = Chat()
            self.chat = chat.from_json(response['chat'])
        except (KeyError, TypeError):
            pass

        try:
            text = Text()
            self.text = text.from_json(response['text'])
        except (KeyError, TypeError):
            pass

        try:
            au = Audio()
            self.audio = au.from_json(response['audio'])
        except (KeyError, TypeError):
            pass

        try:
            document = Document()
            self.document = document.from_json(response['document'])
        except (KeyError, TypeError):
            pass

        try:
            for i in response['photo']:
                self.photo.append(i)
        except (KeyError, TypeError):
            pass

        try:
            sticker = Sticker()
            self.sticker = sticker.from_json(response['sticker'])
        except (KeyError, TypeError):
            pass

        try:
            video = Video()
            self.video = video.from_json(response['video'])
        except (KeyError, TypeError):
            pass

        try:
            voice = Voice()
            self.voice = voice.from_json(response['voice'])
        except (KeyError, TypeError):
            pass

        try:
            self.caption = Text.from_json(response['caption'])
        except (KeyError, TypeError):
            pass

        try:
            location = Location()
            self.location = location.from_json(response['location'])
        except (KeyError, TypeError):
            pass

        return self

    @staticmethod
    def humanize_date(unix_date):
        return dt.fromtimestamp(unix_date).strftime('%Y-%m-%d %H:%M:%S')


class Update(Message):
    raw_update = ''

    def __init__(self):
        self.update_id = 0
        self.message = Message()

    def from_json(self, update):

        self.raw_update = update

        self.update_id = update['update_id']
        self.message.from_json(update['message'])

        return self

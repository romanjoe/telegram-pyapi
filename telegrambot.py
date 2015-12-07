import requests
import time
import exceptions
from datetime import datetime as dt

DEBUG = False


class Telegram(object):
    """
    Abstract class
    """
    API_BASE = 'https://api.telegram.org/bot'

    def __init__(self, token):
        self.token = token
        self.url_token = self.API_BASE + token

    @staticmethod
    def log_event(text):
        event = '%s >> %s' % (time.ctime(), text)
        print event

    def post_request(self, data, api_call):

        if DEBUG:
            Telegram.log_event('Sending json %s to %s' % (data, data['chat_id'],))
            # TODO: make more precise function fro logging

        response = requests.post(self.url_token + api_call, data=data)

        if not response.status_code == 200:
            return False

        # TODO add raise exceptions for other codes

        return response.json()['result']


class TelegramBot(Telegram):

    """
    Telegram bot class, implements API calls
    """

    offset = 0
    chat_id = 0

    api = {'getMe': '/getMe',
           'sendMessage': '/sendMessage',
           'forwardMessage': '/forwardMessage',
           'sendPhoto': '/sendPhoto',
           'sendAudio': '/sendAudio',
           'sendDocument' : '/sendDocument',
           'sendSticker': '/sendSticker',
           'sendVideo': '/sendVideo',
           'sendVoice': '/sendVoice',
           'sendLocation': '/sendLocation',
           'sendChatAction': '/getUserProfilePhotos',
           'getUpdates': '/getUpdates',
           'setWebhook': '/setWebhook',
           'getFile': '/getFile'}

    def __init__(self, token):
        Telegram.__init__(self, token=token)
        self.token = token
        self.offset = 0
        self.chat_id = 0

    def get_me(self):

        if DEBUG:
            self.log_event('Sending getMe to check token is correct')

        data = {}
        return self.post_request(data, self.api['getMe'])

    def send_message(self, text):

        """
        Method to send text messages
        APIdoc URL: https://core.telegram.org/bots/api#sendmessage

        :param text: message to send
        :return: Message json object type - https://core.telegram.org/bots/api#message
        """
        if DEBUG:
            self.log_event('Sending text to %s: %s' % (self.chat_id, text))

        data = {'chat_id': self.chat_id, 'text': text}
        return self.post_request(data, self.api['sendMessage'])

    def forward_message(self, chat_id, from_chat_id, message_id):

        """
        Method for forwarding messages, using id's

        APIdoc URL: https://core.telegram.org/bots/api#forwardmessage

        :param chat_id: from what chat to forward
        :param from_chat_id: to which chat forward
        :param message_id: which message to forward
        :return: Message json object with sent message
        """

        data = {'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id}
        return self.post_request(data, self.api['forwardMessage'])

    def send_photo(self, chat_id, photo, caption='',
                   reply_to_message_id='', reply_markup=''):

        """
        Send photo by id (already uploaded to telegram) or as object of this type
        https://core.telegram.org/bots/api#inputfile

        APIdoc URL: https://core.telegram.org/bots/api#sendphoto

        :param chat_id: must
        :param photo: must
        :param caption: optional
        :param reply_to_message_id: optional
        :param reply_markup: optional
        :return:
        """

        data = {'chat_id': chat_id, 'photo': photo,
                'caption': caption, 'reply_to_message_id': reply_to_message_id,
                'reply_markup': reply_markup}

        return self.post_request(data, self.api['sendPhoto'])

    def send_audio(self, chat_id, audio, duration='',
                   performer='', title='', reply_to_message_id='',
                   reply_markup=''):

        """
        Send audio by id (already uploaded to telegram) or as object of this type
        https://core.telegram.org/bots/api#inputfile

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

        data = {'chat_id': chat_id, 'audio': audio,
                'duration': duration, 'performer': performer,
                'title': title, 'reply_to_message_id': reply_to_message_id,
                'reply_markup': reply_markup}

        return self.post_request(data, self.api['sendAudio'])

    def send_document(self, chat_id, document, reply_to_message_id, reply_markup):
        """
        Send document by id (already uploaded to telegram) or as object of this type
        https://core.telegram.org/bots/api#inputfile

        APIdoc URL: https://core.telegram.org/bots/api#senddocument

        :param chat_id: must
        :param document: must
        :param reply_to_message_id: optional
        :param reply_markup: optional
        :return: Message json object with sent message
        """

        data = {'chat_id': chat_id, 'document': document,
                'reply_to_message_id': reply_to_message_id,
                'reply_markup': reply_markup}

        return self.post_request(data, self.api['sendDocument'])

    def send_sticker(self, chat_id, sticker, reply_to_message_id, reply_markup):
        """
        Send sticker by id (already uploaded to telegram) or as object of this type
        https://core.telegram.org/bots/api#inputfile

        APIdoc URL: https://core.telegram.org/bots/api#senddocument

        :param chat_id: must
        :param sticker: must
        :param reply_to_message_id: optional
        :param reply_markup: optional
        :return: Message json object with sent message
        """

        data = {'chat_id': chat_id, 'sticker': sticker,
                'reply_to_message_id': reply_to_message_id,
                'reply_markup': reply_markup}

        return self.post_request(data, self.api['sendSticker'])

    def send_video(self, chat_id, video, duration='',
                   caption='', reply_to_message_id='',
                   reply_markup=''):

        """
        Send video by id (already uploaded to telegram) or as object of this type
        https://core.telegram.org/bots/api#inputfile

        APIdoc URL: https://core.telegram.org/bots/api#sendvideo

        :param chat_id: must
        :param video: must
        :param duration: optional
        :param caption: optional
        :param reply_to_message_id: optional
        :param reply_markup: optional
        :return: Message json object with sent message
        """

        data = {'chat_id': chat_id, 'video': video,
                'duration': duration, 'caption': caption,
                'reply_to_message_id': reply_to_message_id,
                'reply_markup': reply_markup}

        return self.post_request(data, self.api['sendVideo'])

    def send_voice(self, chat_id, voice, duration='',
                   reply_to_message_id='', reply_markup=''):

        """
        Send voice by id (already uploaded to telegram) or as object of this type
        https://core.telegram.org/bots/api#inputfile

        APIdoc URL: https://core.telegram.org/bots/api#sendvoice

        :param chat_id: must
        :param voice: must
        :param duration: optional
        :param reply_to_message_id: optional
        :param reply_markup: optional
        :return: Message json object with sent message
        """

        data = {'chat_id': chat_id, 'voice': voice,
                'duration': duration, 'reply_to_message_id': reply_to_message_id,
                'reply_markup': reply_markup}

        return self.post_request(data, self.api['sendVoice'])

    def send_location(self, chat_id, latitude, longitude,
                      reply_to_message_id='', reply_markup=''):

        """
        Send latitude by id (already uploaded to telegram) or as object of this type
        https://core.telegram.org/bots/api#inputfile

        APIdoc URL: https://core.telegram.org/bots/api#sendlocation

        :param chat_id: must
        :param latitude: must
        :param longitude: must
        :param reply_to_message_id: optional
        :param reply_markup: optional
        :return: Message json object with sent message
        """

        data = {'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude,
                'reply_to_message_id': reply_to_message_id,
                'reply_markup': reply_markup}

        return self.post_request(data, self.api['sendLocation'])

    def send_chat_action(self, chat_id, action):

        """
        This method can tell bot what to do if he need some time to process request,
        for example to record and upload video

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
        return self.post_request(data, self.api['sendChatAction'])

    def get_updates(self, limit=1):

        """
        This method for receiving array of updates
        Link for description: https://core.telegram.org/bots/api#getupdates

        :parameter limit: sets maximum amount of messages to request. default = 1
        :return: If limit parameter equals 1, as in default case - single update_object returned
                 if limit parameter is bigger than one, then an Array of updates_objects returned
                 https://core.telegram.org/bots/api#update
        """

        data = {'offset': self.offset + 1, 'limit': limit, 'timeout': 0}
        updates = self.post_request(data, self.api['getUpdates'])

        if limit == 1:
            try:
                single_update_object = Update(updates[0])
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
            raise exceptions.ValueError("[MESSAGE] Cant retrieve 0 updates, please, specify value bigger than 1"
                                        " to get_updates() method or leave it"
                                        " blank to retrieve first of unread updates")

    def get_file(self, file_id):

        """
        This method return a download link for a requested file by id

        :param file_id:
        :return: download link for requested file
        """

        data = {'file_id': file_id}
        message = self.post_request(data, self.api['getFile'])
        file_path = message['file_path']

        download_link = ('https://api.telegram.org/file/bot' + self.token + "/" + file_path)

        return download_link

    def get_last_update(self, limit=1):

        """
        This method for receiving array of updates
        Link for description: https://core.telegram.org/bots/api#getupdates

        :parameter limit: sets maximum amount of messages to request. default = 1
        :return: An Array of Update json objects is returned https://core.telegram.org/bots/api#update
        """

        data = {'offset': self.offset + 1, 'limit': limit, 'timeout': 0}

        req = self.post_request(data, self.api['getUpdates'])

        return req[0]['message']['text']


class User(object):

    """
    This object represents a Telegram user or bot
    """

    # attributes:
    id = 0
    first_name = ''
    last_name = ''
    username = ''

    def __init__(self, id=0, first_name='', last_name=''):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

#    @classmethod
    def from_json(self, user):

        self.id = user['id']
        self.first_name = user['first_name']

        try:
            self.last_name = user['last_name']
        except KeyError:
            self.last_name = ''
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
    # attributes:
    id = 0
    type = ''
    title = ''
    first_name = ''
    last_name = ''

    def __init__(self, id=0, type='', first_name='', last_name=''):

        self.id = id
        self.type = type
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_json(cls, chat):
        return cls(chat['id'], chat['type'], chat['first_name'], chat['last_name'])


class PhotoSize(object):

    """
    This object represents one size of a photo or a file / sticker thumbnail
    """
    # attributes:
    file_id = ''
    width = 0
    height = 0
    file_size = 0

    def __init__(self, file_id='', width=0, height=0, files_size=0):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.file_size = files_size

    @classmethod
    def from_json(cls, photo_size):
        return cls(photo_size['file_id'], photo_size['width'], photo_size['height'], photo_size['file_size'])


class Text(object):

    """
    This object represents a text field in Message()
    """

    text_message = ''

    def __init__(self, message=''):
        self.text_message = message

    @classmethod
    def from_json(cls, plain_text):
        return cls(str(plain_text))


class Audio(object):

    """
    This object represents an audio file to be treated as music by the Telegram clients.
    """

    file_id = ''
    duration = 0
    performer = ''
    title = ''
    mime_type = ''
    file_size = 0

    def __init__(self, file_id='', duration=0, performer='', title='', mime_type='', file_size=0):
        self.file_id = file_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.mime_type = mime_type
        self.file_size = file_size

    @classmethod
    def from_json(cls, audio):

        cls.file_id = audio['file_id']
        cls.duration = audio['duration']
        cls.performer = audio['performer']
        cls.title = audio['title']
        cls.mime_type = audio['mime_type']
        cls.file_size = audio['file_size']

        return cls


class Document(object):

    """
    This object represents a general file (as opposed to photos, voice messages and audio files).
    """

    file_id = ''
    thumb = PhotoSize()
    file_name = ''
    mime_type = ''
    file_size = 0

    def __init__(self, file_id='', thumb=PhotoSize(), file_name='', mime_type='', file_size=0):
        self.file_id = file_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    @classmethod
    def from_json(cls, document):

        cls.file_size = document['file_size']
        cls.file_id = document['file_id']
        cls.file_name = document['file_name']
        cls.mime_type = document['mime_type']

        try:
            """
            Since thumbnails is available not for every document
            """

            cls.thumb = document['thumb']
            return cls
        finally:
            return cls


class Sticker(object):

    """
    This object represents a sticker.
    """

    file_id = ''
    width = 0
    height = 0
    thumb = PhotoSize()
    file_size = 0

    def __init__(self, file_id='', width=0, height=0, thumb=PhotoSize(), file_size=0):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.thumb = thumb
        self.file_size = file_size

    @classmethod
    def from_json(cls, sticker):

        cls.thumb = PhotoSize.from_json(sticker['thumb'])
        cls.file_id = sticker['file_id']
        cls.width = sticker['width']
        cls.height = sticker['height']
        cls.file_size = sticker['file_size']

        return cls


class Video(object):

    """
    This object represents a video file.
    """

    file_id = ''
    width = 0
    height = 0
    duration = 0
    thumb = PhotoSize()
    mime_type = ''
    file_size = 0

    def __init__(self, file_id='', width=0, height=0, duration=0, thumb=PhotoSize(), mime_type='', file_size=0):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = PhotoSize()
        self.mime_type = mime_type
        self.file_size = file_size

    @classmethod
    def from_json(cls, video):

        cls.file_id = video['file_id']
        cls.width = video['width']
        cls.height = video['height']
        cls.duration = video['duration']
        cls.file_size = video['file_size']

        try:
            cls.mime_type = video['mime_type']
        except KeyError:
            pass

        try:
            cls.thumb = PhotoSize.from_json(video['thumb'])

            return cls

        finally:
            return cls


class Voice(object):

    """
    This object represents a voice note.
    """

    file_id = ''
    mime_type = ''
    duration = 0
    file_size = 0

    def __init__(self, file_id='', mime_type='', duration=0, file_size=0):
        self.file_id = file_id
        self.mime_type = mime_type
        self.duration = duration
        self.file_size = file_size

    @classmethod
    def from_json(cls, voice):

        cls.file_id = voice['file_id']
        cls.mime_type = voice['mime_type']
        cls.duration = voice['duration']
        cls.file_size = voice['file_size']

        return cls


class Contact(object):

    """
    This object represents a phone contact.
    """

    phone_number = ''
    first_name = ''
    last_name = ''
    user_id = 0

    def __init__(self, phone_number='', first_name='', last_name='', user_id=0):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id

    @classmethod
    def from_json(cls, contact):

        cls.phone_number = contact['phone_number']
        cls.first_name = contact['first_name']

        try:
            cls.last_name = contact['last_name']
        except KeyError:
            pass
        try:
            cls.user_id = contact['user_id']
        except KeyError:
            pass

        return cls


class Location(object):

    """
    This object represents a point on the map.
    """

    longitude = 0.0
    latitude = 0.0

    def __init__(self, longitude=0.0, latitude=0.0):
        self.longitude = longitude
        self.latitude = latitude

    @classmethod
    def from_json(cls, location):

        cls.longitude = location['longitude']
        cls.latitude = location['latitude']

        return cls


class UserProfilePhotos(object):

    """
    This object represent a user's profile pictures.
    """

    total_count = 0
    photos = []


class File(object):

    """
    This object represents a file ready to be downloaded.
    The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>.
    It is guaranteed that the link will be valid for at least 1 hour.
    When the link expires, a new one can be requested by calling getFile.
    """

    file_id = ''
    file_size = 0
    file_path = ''


class Message(object):

    """
    This object represents a message
    """
    # attributes:
    message_id = 0
    message_from = User()
    date = ''
    chat = Chat()
    forward_from = User(),
    forward_date = '',
    # reply_to_message = '',
    text = Text(),
    audio = Audio(),
    document = Document(),
    photo = []
    sticker = Sticker()
    video = Video(),
    voice = Voice(),
    # caption = ''
    contact = Contact(),
    location = Location()

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
                 # caption = '',
                 contact=Contact(),
                 location=Location()
                 ):
        self.message_id = message_id
        self.message_from = message_from
        self.date = date
        self.chat = chat
        self.forward_from = forward_from
        self.forward_date = forward_date
#        self.reply_to_message = reply_to_message
        self.audio = audio
        self.document = document
        self.photo = photo
        self.sticker = sticker
        self.video = video
        self.voice = voice
        self.contact = contact
        self.location = location

    @classmethod
    def from_json(cls, response):

        try:
            cls.message_id = response['message_id']
            cls.date = response['date']
        except KeyError:
            pass

        try:
            from_user = User()
            cls.message_from = from_user.from_json(response['from'])
        except KeyError:
            pass

        try:
            forwarded_from_user = User().from_json(response['forward_from'])
            cls.forward_from = forwarded_from_user
        except KeyError:
            pass

        try:
            cls.date = dt.fromtimestamp(response['date']).strftime('%Y-%m-%d %H:%M:%S')
        except KeyError:
            pass

        try:
            cls.forward_date = dt.fromtimestamp(response['forward_date']).strftime('%Y-%m-%d %H:%M:%S')
        except KeyError:
            pass

        try:
            cls.chat = Chat.from_json(response['chat'])
        except KeyError:
            pass

        try:
            cls.text = Text.from_json(response['text'])
        except KeyError:
            pass

        try:
            cls.audio = Audio.from_json(response['audio'])
        except KeyError:
            pass

        try:
            cls.document = Document.from_json(response['document'])
        except KeyError:
            pass

        try:
            for i in response['photo']:
                cls.photo.append(i)
        except KeyError:
            pass

        try:
            cls.sticker = Sticker.from_json(response['sticker'])
        except KeyError:
            pass

        try:
            cls.video = Video.from_json(response['video'])
        except KeyError:
            pass

        try:
            cls.voice = Voice.from_json(response['voice'])
        except KeyError:
            pass

        try:
            cls.contact = Contact.from_json(response['contact'])
        except KeyError:
            pass

        try:
            cls.location = Location.from_json(response['location'])
        except KeyError:
            pass

        return cls


class Update:

    raw_update = ''

    def __init__(self, update):
        self.raw_update = update
        self.Update = self.construct(update)

    @staticmethod
    def construct(message):
        return Message.from_json(response=message['message'])

import requests
import time
from datetime import datetime as dt

DEBUG = False


class Bot(object):
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
            Bot.log_event('Sending json %s to %s' % (data, data['chat_id'], ))
            # TODO: make more precise function fro logging

        response = requests.post(self.url_token + api_call, data=data)

        if not response.status_code == 200:
            return False

        # TODO add raise exceptions for other codes

        return response.json()['result']


class Telegram(Bot):

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
        Bot.__init__(self, token=token)
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
        :return: An Array of Update json objects is returned https://core.telegram.org/bots/api#update
        """

        data = {'offset': self.offset + 1, 'limit': limit, 'timeout': 0}
        return self.post_request(data, self.api['getUpdates'])

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

    @classmethod
    def from_json(cls, user):
        return cls(user['id'], user['first_name'], user['last_name'])


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


class Audio(object):

    file_id = ''
    duration = 0
    performer = ''
    title = ''
    mime_type = ''
    file_size = 0


class Document(object):

    file_id = ''
    thumb = ''
    file_name = ''
    mime_type = ''
    file_size = 0


class Sticker(object):

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

        return cls #(sticker['file_id'], sticker['width'], sticker['height'], sticker['file_size'])


class Video(object):

    file_id = ''
    width = 0
    height = 0
    duration = 0
    thumb = []
    mime_type = ''
    file_size = 0


class Voice(object):

    file_id = ''
    mime_type = ''
    duration = 0
    file_size = 0


class Contact(object):

    phone_number = ''
    first_name = ''
    last_name = ''
    user_id	= 0


class Location(object):

    longitude = 0.0
    latitude = 0.0


class UserProfilePhotos(object):

    total_count = 0
    photos = []


class File(object):

    file_id = ''
    file_size = 0
    file_path = ''


class Message(object):

    """
    This object represents a message
    """
    # attributes:
    message_id = 0
    message_from = ''
    date = 0
    chat = ''
    # forward_from = ''
    # forward_date = ''
    # reply_to_massage = ''
    # text = ''
    # audio = ''
    # document = ''
    photo = []
    sticker = Sticker()
    # video = ''
    # voice = ''
    # caption = ''
    # contact = ''
    # location = ''

    # TODO to be added in future
    # new_chat_participant = ''
    # left_chat_participant = ''
    # new_chat_title = ''
    # new_chat_photo = ''
    # group_chat_created = ''
    # supergrop_chat_created = ''
    # channel_chat_created = ''
    # migrate_to_chat_id = ''
    # migrate_from_chat_id = ''

    def __init__(self,
                 message_id=0,
                 message_from='',
                 date=0,
                 chat='',
                 # forward_from = '',
                 # forward_date = '',
                 # reply_to_massage = '',
                 # text = '',
                 # audio = '',
                 # document = '',
                 photo=[],
                 sticker=Sticker()
                 # video = '',
                 # voice = '',
                 # caption = '',
                 # contact = '',
                 # location = ''
                 ):
        self.message_id = message_id
        self.message_from = message_from
        self.date = date
        self.chat = chat
        self.photo = photo
        self.sticker = sticker

    @classmethod
    def from_json(cls, response):

        # photo field must be filled with array of retrieved array of PhotoSize
        try:
            for i in response['photo']:
                cls.photo.append(i)
            # TODO: investigate if response['photo'] needed in return string (suppose NO)
        except:
            pass

        try:
            cls.sticker = Sticker.from_json(response['sticker'])
        except:
            pass

        return cls(response['message_id'], response['from'], response['date'], response['chat'])


class Parser:

    result = ''

    def __init__(self, result=''):
        self.result = result

    @classmethod
    def get(cls, message, **kwargs):

        result = ''

        json = Message.from_json(response=message['message'])

        if DEBUG:
            print "+++++++ This is json message" + str(json.chat)

        # chat = Chat.from_json(json.chat)
        # chat_from = User.from_json(json.message_from)

        for key, val in kwargs.iteritems():

            if key == 'extract_field':
                if val == 'from':
                    result = (chat_from.username + ' (' +
                              chat_from.first_name + ' ' +
                              chat_from.last_name + ') ' + ' ' +
                              str(chat_from.id))

                elif val == 'chat':
                    result = ("Message received in " + chat.type + " chat " +
                              str(chat.id) + " from " + chat.first_name + " " +
                              chat.last_name)

                elif val == 'message_id':
                    result = ("Message id = " + str(json.message_id))

                elif val == 'date':
                    result = ('Message received at ' + dt.fromtimestamp(json.date).strftime('%Y-%m-%d %H:%M:%S'))

                elif val == 'photo_size':
                    available_photo_sizes_array = []

                    result = {}

                    for photo in json.photo:
                        available_photo_sizes_array.append(PhotoSize.from_json(photo))

                    for size in available_photo_sizes_array:
                        resolution = str(size.width) + "x" + str(size.height)
                        file_id = str(size.file_id)
                        result[resolution] = file_id

                elif val == 'sticker':
                    sticker = json.sticker
                    print str(sticker)

                    result = str(sticker.height) + "x" + str(sticker.width)

        return result


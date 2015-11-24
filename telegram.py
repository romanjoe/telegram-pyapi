import requests
import time

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

        download_link = ('https://api.telegram.org/file/bot' + self.token + file_path)

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
        print (user)
        return cls(user['id'], user['first_name'], user['last_name'])


class Parser:

    result = ''

    def __init__(self, result=''):
        self.result = result

    @classmethod
    def get(cls, message, **kwargs):

        result = ''

        for key, val in kwargs.iteritems():

            if key == 'chat':
                if val == 'from':
                    chat_from = User.from_json(user=message)
                    result = (chat_from.username + ' (' +
                              chat_from.first_name + ' ' +
                              chat_from.last_name + ') ' + ' ' +
                              str(chat_from.id))
        return result

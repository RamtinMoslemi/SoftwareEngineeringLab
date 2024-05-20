import re


class MessageService:
    def send_message(self, message):
        raise NotImplemented

    def validate(self, port):
        raise NotImplemented

    def __repr__(self):
        return f'{self.__class__.__name__}()'


class SmsMessageService(MessageService):
    phone_regex = r'[0-9]+'

    def send_message(self, message):
        if self.validate(message.source) and self.validate(message.target):
            print('Sending an SMS from ' + message.source + ' to ' +
                  message.target + ' with content ' + message.content)
        else:
            print('Invalid phone number!')

    def validate(self, port):
        if len(port) != 11:
            return False
        return re.fullmatch(self.phone_regex, port)


class EmailMessageService(MessageService):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    def send_message(self, message):
        if self.validate(message.source) and self.validate(message.target):
            print('Sending an Email from ' + message.source + ' to ' +
                  message.target + ' with content ' + message.content)
        else:
            print('Invalid email!')

    def validate(self, port):
        return re.fullmatch(self.email_regex, port)

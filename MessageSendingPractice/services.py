class MessageService:
    def send_message(self, message):
        raise NotImplemented

    def validate(self, access_point):
        raise NotImplemented


class SmsMessageService(MessageService):
    def send_message(self, message):
        if self.validate(message.source) and self.validate(message.target):
            print('Sending an SMS from ' + message.source + ' to ' +
                  message.target + ' with content ' + message.content)

    def validate(self, access_point):
        if len(access_point) != 11:
            return False
        return True


class EmailMessageService(MessageService):
    def send_message(self, message):
        if self.validate(message.source) and self.validate(message.target):
            print('Sending an Email from ' + message.source + ' to ' +
                  message.target + ' with content ' + message.content)

    def validate(self, access_point):
        if len(access_point) != 11:
            return False
        return True

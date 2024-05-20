from services import EmailMessageService, SmsMessageService
from message import Message

if __name__ == '__main__':
    print('Hello and Welcome to SE Lab Messenger.\n')

    while True:
        command = input('In order to send SMS message enter 1\n'
                        'In order to sent Email message enter 2\n'
                        'In order to exit, enter 0\n')

        if command == '0':
            break
        elif command == '1' or command == '2':
            port_type = 'phone number' if command == '1' else 'email'
            message_service = SmsMessageService() if command == '1' else EmailMessageService()
            source = input(f'Enter source {port_type}: ')
            target = input(f'Enter target {port_type}: ')
            content = input('Write your message:\n')
            message = Message(source=source, target=target, content=content)
            message_service.send_message(message)

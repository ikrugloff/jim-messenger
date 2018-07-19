import os
import sys
import time
import argparse
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

from client import Client
import jim

DEFAULT_IP = '0.0.0.0'
DEFAULT_PORT = 8888

app = QApplication(sys.argv)
w = uic.loadUi(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ui/client.ui'))


def receive_callback(parcel):
    if parcel.action == 'contact_list':
        w.contactList.addItem(parcel.account_name)
    elif parcel.action == 'msg':
        w.chatArea.addItem('{}: {}'.format(parcel.sender, parcel.text))
    elif parcel.response == 400:
        w.chatArea.addItem('Error: {}'.format(parcel.error))


class Handler:
    def __init__(self, client):
        self.__client = client
        w.sendButton.clicked.connect(self.send_message)
        w.newContactButton.clicked.connect(self.add_contact)
        w.deleteContactButton.clicked.connect(self.delete_contact)
        w.newContactInput.returnPressed.connect(w.newContactButton.click)
        w.setWindowTitle('Echo ({})'.format(client.name))
        w.show()

        client.send(jim.Message(action='get_contacts'))

    def send_message(self):
        text = w.messageInput.toPlainText()
        if text:
            params = {'action': 'msg', 'text': text}
            selected_index = w.contactList.currentIndex()
            if selected_index:
                user_name = selected_index.data()
                params['to'] = user_name
            if self.__client.send(jim.Message(**params)):
                w.chatArea.addItem('{}: {}'.format(self.__client.name, text))
                w.messageInput.clear()

    def add_contact(self):
        contact_name = w.newContactInput.text()
        if contact_name:
            self.__client.send(jim.Message(action='add_contact', user_name=contact_name))
            time.sleep(0.2)
            w.contactList.clear()
            self.__client.send(jim.Message(action='get_contacts'))

    def delete_contact(self):
        selected_index = w.contactList.currentIndex()
        if selected_index:
            self.__client.send(jim.Message(action='del_contact', user_name=selected_index.data()))
            time.sleep(0.2)
            w.contactList.clear()
            self.__client.send(jim.Message(action='get_contacts'))


def run():
    def args():
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '-a',
            '--address',
            default=DEFAULT_IP,
            nargs='?',
            help='IP (default {})'.format(DEFAULT_IP))
        parser.add_argument(
            '-p',
            '--port',
            default=DEFAULT_PORT,
            nargs='?',
            help='Port (default {})'.format(DEFAULT_PORT))
        parser.add_argument(
            '-u',
            '--user',
            default='Anonymous_{}'.format(randint(1, 1000)),
            nargs='?',
            help='User name (default Anonymous_XXXX)')
        return parser.parse_args()
    console_params = args()
    cl = Client((console_params.address, console_params.port), console_params.user, receive_callback)
    if cl.connect():
        handler = Handler(cl)
        sys.exit(app.exec_())


if __name__ == "__main__":
    run()

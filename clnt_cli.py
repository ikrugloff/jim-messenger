import argparse
from random import randint

from client import Client
import jim

ACTIONS = (
    {
        'action': 'msg',
        'name': 'Send message',
        'params': ('text',)
    },
    {
        'action': 'get_contacts',
        'name': 'Contact List',
    },
    {
        'action': 'add_contact',
        'name': 'Add contact',
        'params': ('user_name',)
    },
    {
        'action': 'del_contact',
        'name': 'Delete contact',
        'params': ('user_name',)
    }
)
DEFAULT_IP = '0.0.0.0'
DEFAULT_PORT = 8888

def interact():
    print('\n'.join(['{}. {}'.format(key, action['name']) for key, action in enumerate(ACTIONS, 1)]))
    try:
        num = abs(int(input('Choose action: ')))
    except ValueError:
        num = 0
    config = ACTIONS[num - 1] if num <= len(ACTIONS) else ACTIONS[0]
    params = {'action': config['action']}
    if 'params' in config:
        for param in config['params']:
            p = str(input('Choose parameter "{}": '.format(param)))
            params[param] = p
    return jim.Message(**params)


def receive_callback(parcel):
    if parcel.action == 'contact_list':
        print('\n{}'.format(parcel.account_name))
    elif parcel.action == 'msg':
        print('\nMessage from {}: {}'.format(parcel.sender, parcel.text))


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
        while True:
            message = interact()
            cl.send(message)


if __name__ == "__main__":
    run()

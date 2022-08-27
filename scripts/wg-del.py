#!/usr/bin/python3

import re
import sys
import argparse
import colorama

config_path = "/usr/local/etc/wg-scripts/"
sys.path.append(config_path)
from wg_add_config import *


def text_highlighting(pattern: str, text: str):
    return re.sub(pattern, colorama.Back.RED + pattern + colorama.Back.RESET, text)


def delete_items_from_text(items: list, text: str):
    for item in items:
        text = text.replace("[Peer]\n" + item, '')
    return text


def main():
    parser = argparse.ArgumentParser(
        description="delete peer from wireguard vpn"
    )
    parser.add_argument("-k", "--key", dest="key", help="key for search", type=str)
    args = parser.parse_args()

    with open(CONFIG_PATH, "r") as rf:
        config = rf.read()

    peers = config.split('[Peer]\n')
    del peers[0]

    colorama.init()

    while 1:
        matched = []

        reg = args.key if args.key else input("Type key for search\n~# ")
        args.key = None

        for peer in peers:
            if re.search(reg, peer):
                matched.append(peer)

        print('The result of search:')
        for m in matched:
            print('[Peer]\n' + text_highlighting(reg, m).strip() + '\n')

        print(f'Matched peers: {len(matched)}/{len(peers)}')

        while (answer := input('Do you really want to delete this items y/n: (n to research)')) not in ('y', 'n'):
            print('Incorrect type "y" or "n" (Ctrl+ C to exit)')

        if answer == 'y':
            break

    print('New config files:\n"""')
    print(new_config := delete_items_from_text(matched, config), end='"""\n')

    while (answer := input('Please confirm the changes y/n: ')) not in ('y', 'n'):
        print('Incorrect type "y" or "n" (Ctrl+ C to exit)')

    if answer == 'y':
        with open(CONFIG_PATH, 'w') as wf:
            wf.write(new_config)

        print('Success!')
        print("You can type it:")
        print(f"cat {CONFIG_PATH}")
        print("wg-quick down wg0; wg-quick up wg0")


if __name__ == "__main__":
    main()
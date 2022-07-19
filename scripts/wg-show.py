#!/usr/bin/python3

import re
import sys
import json
import hashlib
import colorama
import subprocess
from wh_show_conf import *

config_path = "/usr/local/etc/wg-scripts/"
sys.path.append(config_path)
from wg_show_config import *


def key_val(line: str) -> (str, str):
    """:return key and value from key = value"""
    splitter = line.find("=")
    return line[:splitter].strip(), line[splitter+1:].strip()


def find_checksum(filename: str) -> str:
    md5 = hashlib.md5()
    with open(filename, "rb") as rf:
        while 1:
            data = rf.read(32768)
            if not data:
                break
            md5.update(data)

    return md5.hexdigest()


def make_association() -> dict:
    with open(CONFIG_PATH, "r") as rf:
        lines = rf.read().split("\n")

    key = ""
    associations = {}

    for line in lines:
        if "PublicKey" in line:
            key = key_val(line)[1]
            associations[key] = [None] * 2
        elif "#Name" in line:
            associations[key][0] = key_val(line)[1]
        elif "#Description" in line:
            associations[key][1] = key_val(line)[1]

    associations['last_hash'] = find_checksum(CONFIG_PATH)

    return associations

def modify_output(associations: dict):
    #wg_show = open("wgshow", "r").read()
    wg_show = subprocess.check_output("wg show", shell=True).decode()
    coloring(wg_show)
    wg_show = wg_show.split("\n")

    for line in wg_show:
        if "peer" in line:
            try:
                name, desc = associations[line.split(' ')[1]]
                if name:
                    line += '(' + name + ')'
                if desc:
                    line += '\n  description: ' + desc

            except KeyError: pass
        print(coloring(line))

def update_associations():
    with open(ASSOCIATION_CASH_PATH, 'w') as wf:
        json.dump(make_association(), wf)

def get_associations():
    try:
        with open(ASSOCIATION_CASH_PATH, "r") as rj:
            return json.load(rj)
    except:
        return {'last_hash': ''}

def to_color(text, color):
    return color + text + colorama.Fore.RESET + colorama.Style.NORMAL + colorama.Back.RESET

def coloring(text):
    for color in colors:
        matched = re.search(color[0], text)
        if matched:
            m = matched.group()
            text = text.replace(m, to_color(m, color[1]))

    return text

if __name__ == '__main__':
    colorama.init()

    associations = get_associations()
    conf_hash = find_checksum(CONFIG_PATH)

    if conf_hash != associations['last_hash']:
        update_associations()
        associations = get_associations()

    modify_output(associations)
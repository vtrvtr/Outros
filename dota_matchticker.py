import argparse
import logging
import sys
from subprocess import Popen
import json


class Streams(object):  # Base stream class, you need to load the dictionary

    def __init__(self, stream_dict=None):
        if stream_dict is not None:
            self.streams = stream_dict
        else:
            self.streams = {}

    def addStream(self, game, stream_url):
        try:
            if stream_url not in self.streams[game.upper()]:
                self.streams[game.upper()].append(stream_url)
            else:
                pass
        except:
            self.streams[game.upper()] = [stream_url]

    def getStream(self, stream_url):
        for v in self.streams.values():
            if v == stream_url:
                return v

    def getAllStreams(self):
        return self.streams

    def getGameStreams(self, game):
        return self.streams[game]

STREAM_LIST_PATH = 'E:\Code\Outros\stream_list.json'
TEXT_PATH = 'E:\\Documents\livestreamer.txt'

def open_dict():
    with open(STREAM_LIST_PATH) as f:
        read_dict = json.load(f)
        stream_dict = Streams(read_dict)
    return stream_dict


def add_streams(url, game):
    stream_dict = open_dict()
    stream_dict.addStream(game.upper(), str(url))
    with open(STREAM_LIST_PATH, 'w') as f:
        json.dump(stream_dict.getAllStreams(), f)


def open_livestreamer(stream_urls):
    for stream_url in stream_urls:
        Popen('livestreamer {} source'.format(str(stream_url)))


def main(game=None):
    streams = open_dict()
    if game == None:
        for v in streams.getAllStreams().values():
            open_livestreamer(v)
    else:
        open_livestreamer(streams.getGameStreams(game.upper()))


def massive_add(text):
    with open(text, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            if line == line.upper():
                game = line
            else:
                url = line.split()
                add_streams(''.join(url[1::3]), game)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Game streams to open')
    if len(sys.argv) == 2:
        parser.add_argument('game')
        args = parser.parse_args()
        main(args.game)
    elif len(sys.argv) == 3:
        parser.add_argument('url',  help="add stream to the list")
        parser.add_argument('add_game',  help="add stream to the list")
        args = parser.parse_args()
        add_streams(args.url, args.add_game)
    else:
        main()

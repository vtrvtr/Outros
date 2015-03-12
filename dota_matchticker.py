import argparse
import sys
from subprocess import Popen
import json


class Streams(object):

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


def open_dict():
    with open('E:\Code\Outros\stream_list.json') as f:
    return stream_dict


def add_streams(url, game):
    stream = open_dict()
    stream_dict.addStream(game.upper(), url)
    with open('E:\Code\Outros\stream_list.json', 'w') as f:
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


if __name__ == "__main__":
    if len(sys.argv) == 2:
        parser = argparse.ArgumentParser(description='Game streams to open')
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

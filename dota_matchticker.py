
from subprocess import call
import json
import urllib2
import pprint


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
        read_dict = json.load(f)
        stream_dict = Streams(read_dict)
    return stream_dict


def add_streams(url, game):
    stream = open_dict()
    stream_dict.addStream(game.upper(), url)
    with open('E:\Code\Outros\stream_list.json', 'w') as f:
        json.dump(stream_dict.getAllStreams(), f)


def open_livestreamer(stream_urls):
    for stream_url in stream_urls:
        call('livestreamer {} source'.format(str(stream_url)))


def main(game):
    streams = open_dict()
    open_livestreamer(streams.getGameStreams(game.upper()))


main('dota')

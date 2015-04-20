#!python3

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


def open_livestreamer(stream_urls, verbose = True):
    for stream_url in stream_urls:
        Popen('livestreamer {} best -Q'.format(str(stream_url)), shell=verbose)


def main(verbose = True, game=None):
    streams = open_dict()
    if game == None:
        for v in streams.getAllStreams().values():
            open_livestreamer(v, verbose)
    else:
        open_livestreamer(streams.getGameStreams(game.upper()), verbose)


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
    parser.add_argument('-s', help='opens a single stream', action="store")
    parser.add_argument('-m',  help="open multiple streams", action="store")
    parser.add_argument('-add', help="add stream to the list URL GAME", nargs=2 action="store")
    parser.add_argument('--verbose', help="Makes cmd windows appear")
    args = parser.parse_args()
    verbose = False if args.verbose else True
    if args.s:
        open_livestreamer([args.s], verbose)
    elif args.m:    
        main(args.m, verbose)
    elif args.add:
        add_streams(args.add[0], args.add[1])
    else:
        main()




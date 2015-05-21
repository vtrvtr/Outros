#!python3

import argparse
import logging
from subprocess import Popen
import json
from livestreamer import streams as livestreamer_stream
from stream_lib import Streams
import configparser
from configparser import SafeConfigParser, ParsingError, BasicInterpolation


# Reading and loading configs
try:
    conf = SafeConfigParser()
    conf.read('E:\code\outros\stream check\config.ini')
    STREAM_LIST_PATH = conf.get('stream_dict', 'path')
    TEXT_PATH = conf.get('massiveadd', 'path')
    LOG_PATH = conf.get('log', 'path')
    FORMATTER = '%(asctime)-15s | %(levelname)-8s \n %(message)-8s'
    logging.basicConfig(
        filename=LOG_PATH, level=logging.INFO, format=FORMATTER)
    logging.getLogger("requests").setLevel(logging.WARNING)
except ParsingError as e:
    print(e)



def open_dict():
    with open(STREAM_LIST_PATH) as f:
        logging.info('Opening dictionary')
        read_dict = json.load(f)
        stream_dict = Streams(read_dict)
    return stream_dict


def add_streams(url, game):
    stream_dict = open_dict()
    stream_dict.addStream(game.upper(), str(url))
    with open(STREAM_LIST_PATH, 'w') as f:
        json.dump(stream_dict.getAllStreams(), fj)
        logging.info('Added url: {} \n category: {}'.format(url, game))


def check_stream(url):
    try:
        if livestreamer_stream(url):
            return True
        else:
            return False
    except Exception as e:
        if args.verbose:
            logging.error('Couldnt open: {} ({})'.format(stream_url, e))
        else:
            logging.error('Couldnt open: {}'.format(stream_url))


def open_livestreamer(stream_urls, quality, verbose):
    for stream_url in stream_urls:
        if check_stream(stream_url):
            Popen(
                'livestreamer {} {} -Q'.format(str(stream_url), quality), shell=verbose)
            logging.info('Opening: {} \n Quality: {} \n verbose: {}'.format(
                stream_url, quality, verbose))


def massive_add(text):
    with open(text, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            if line == line.upper():
                game = line
            else:
                url = line.split()
                add_streams(''.join(url[1::3]), game)


def main(game=None, quality='source', verbose=True):
    streams = open_dict()
    if game == None:
        for v in streams.getAllStreams().values():
            open_livestreamer(v, quality, verbose)
    else:
        open_livestreamer(
            streams.getGameStreams(game.upper()), quality, verbose)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Game streams to open')
    parser.add_argument(
        '--single', '-s', help='opens a single stream', action="store")
    parser.add_argument(
        '--multi', '-m',  help="open multiple streams", action="store")
    parser.add_argument(
        '--add', '-a', help="add stream to the list URL GAME", nargs=2, action="store")
    parser.add_argument(
        '-v', '--verbose', help="Makes cmd windows appear", action="store_true")
    parser.add_argument(
        '--quality', '-q', help='Chooses the quality to open streams, default = source', default='source')
    args = parser.parse_args()
    verbose = False if args.verbose else True
    if args.single:
        open_livestreamer([args.single], args.quality, verbose)
    elif args.multi:
        main(args.multi, args.quality, verbose)
    elif args.add:
        add_streams(args.add[0], args.add[1])
    else:
        main()

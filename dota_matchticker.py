
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
        if stream_url not in self.streams.values():
            if game.upper() in self.streams:
                self.streams[game.upper()].append(stream_url)
            else:
                self.streams[game.upper()] = [stream_url]
        else:
            return 'Stream already there'

    def getStream(self, stream_url):
        for v in self.streams.values():
            if v == stream_url:
                return v

    def getAllStreams(self):
        return self.streams


def main():
    add_list = '''livestreamer.exe http://www.twitch.tv/beyondthesummit2 source
livestreamer.exe http://www.twitch.tv/beyondthesummit source
livestreamer.exe http://www.twitch.tv/dotastarladder_en source
livestreamer.exe http://www.twitch.tv/joindotared source
livestreamer.exe http://www.dailymotion.com/embed/video/x1b1h6o best
livestreamer.exe http://www.twitch.tv/joindotablue source
livestreamer.exe http://www.twitch.tv/joindotacommunity source
livestreamer.exe http://www.twitch.tv/dotacinema/popout best
livestreamer.exe http://www.twitch.tv/d2l source
livestreamer.exe http://www.twitch.tv/neodota source
livestreamer.exe http://www.hitbox.tv/bountyhunterseries source
livestreamer.exe http://www.twitch.tv/esltv_dota source
livestreamer.exe http://www.dailymotion.com/embed/video/x1b1h6o?autoplay=1&hidePopoutButton=1 best
livestreamer.exe http://www.twitch.tv/dreamleague/popout best   
livestreamer.exe http://www.twitch.tv/highgroundtv/popout best
livestreamer.exe http://www.twitch.tv/esportal/popout best'''
    urls = add_list.split()[1::3]
    with open('E:\Code\Outros\stream_list.json') as f:
        stream_dict = json.load(f)
        stream = Streams(stream_dict)
        for url in urls:
            stream_dict.addStream('DOTA', url)
        json.dump(stream_dict.getAllStreams(), f)

main()


from subprocess import call

# call('livestreamer twitch.tv/joindotared source')

from pytvdbapi import api
from pathlib import Path
from collections import namedtuple

def episode_rename(season, episode):
    return u"S{}{}E{}{} ".format(0 if season < 10 else '', season, 0 if episode < 10 else '', episode).encode('utf-8')

class Serie(object):

    def __init__(self, series_name, language='en'):
        self.name = series_name
        self.db = api.TVDB('667CE371BAA23809')
        self.show = self.db.search(series_name, language)[0]

    def get_episodes(self, seasons=None):
        self.seasons = [seasons] or seasons
        if seasons is None:
            for episode in self.show:
                yield episode.SeasonNumber, episode.EpisodeNumber, ''.join([letter for letter in episode.EpisodeName if letter not in '?!:,'])
        else:
            for season in self.seasons:
                for episode in self.show[season]:
                    yield episode.SeasonNumber, episode.EpisodeNumber, ''.join([letter for letter in episode.EpisodeName if letter not in '?!:,'])

    def print_episodes(self, seasons=None):
        self.seasons = [seasons] or seasons
        if seasons is None:
            for episode in self.show:
                yield episode.SeasonNumber, episode.EpisodeNumber, episode.EpisodeName
        else:
            for season in self.seasons:
                for episode in self.show[season]:
                    yield u"S{}{}E{}{} - {}".format(0 if episode.SeasonNumber < 10 else '', episode.EpisodeNumber, 0 if episode.EpisodeNumber< 10 else '', episode.EpisodeNumber, episode.EpisodeName).encode('utf-8')


    def get_episode(self, season, episode):
        self.season = season
        self.episode = episode
        episode = self.show[self.season][self.episode]
        E = namedtuple('Episode', ['number', 'name', 'overview'])
        # return E(u'{}x{} - '.format(episode.SeasonNumber, episode.EpisodeNumber).encode('utf-8'), episode.EpisodeName, episode.Overview)
        return E(episode_rename(episode.SeasonNumber, episode.EpisodeNumber), episode.EpisodeName, episode.Overview)

db = api.TVDB('667CE371BAA23809')
show = db.search('naruto', 'en')[0]


# print(dir(show[1][2]))

a = Serie('naruto')

b = a.get_episode(1, 1)

for e in a.print_episodes(1):
    print(e)
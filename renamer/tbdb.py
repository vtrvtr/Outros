from pytvdbapi import api
from pytvdbapi.error import TVDBIndexError, ConnectionError, BadData
from pathlib import Path
from collections import namedtuple


def episode_rename(season, episode):
    return u"S{}{}E{}{}".format(0 if season < 10 else '', season, 0 if episode < 10 else '', episode).encode('utf-8')


class Serie(object):

    def __init__(self, series_name, language='en'):
        self.name = series_name
        self.db = api.TVDB('667CE371BAA23809')
        try:
            self.show = self.db.search(series_name, language)[0]
            self.show.update()
        except TVDBIndexError:
            raise ValueError('Show not found, try another name')
        except ConnectionError:
            raise ValueError('Connection to database failed')
        except BadData:
            raise ValueError('Corrupted data')

    def get_episodes(self, seasons=None):
        self.seasons = [seasons] or seasons
        self.episodes = []
        if seasons is None:
            for season in self.show:
                for episode in season:
                    self.episodes.append((episode.SeasonNumber, episode.EpisodeNumber, ''.join([letter for letter in episode.EpisodeName if letter not in '?!:,'])))
        else:
            for season in self.seasons:
                for episode in self.show[int(season)]:
                    self.episodes.append((episode.SeasonNumber, episode.EpisodeNumber, ''.join([letter for letter in episode.EpisodeName if letter not in '?!:,'])))
        return self.episodes

    def __str__(self, seasons=None):
        self.seasons = [seasons] or seasons
        if seasons is None:
            for episode in self.show:
                yield episode.SeasonNumber, episode.EpisodeNumber, episode.EpisodeName
        else:
            for season in self.seasons:
                for episode in self.show[season]:
                    yield u"{} - {}".format(episode_rename(episode.SeasonNumber, episode.EpisodeNumber), episode.EpisodeName).encode('utf-8')

    def get_episode(self, season, episode):
        self.season = season
        self.episode = episode
        episode = self.show[self.season][self.episode]
        E = namedtuple('Episode', ['number', 'name', 'overview'])
        return E(episode_rename(episode.SeasonNumber, episode.EpisodeNumber), episode.EpisodeName, episode.Overview)



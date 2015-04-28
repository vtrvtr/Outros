from pytvdbapi import api
from pathlib import Path
import renamer


class Serie(object):

    def __init__(self, series_name, language='en'):
        self.name = series_name
        self.db = api.TVDB('667CE371BAA23809')
        self.show = self.db.search(series_name, language)[0]

    def get_episodes(self, seasons=None):
        self.seasons = [seasons] or seasons
        if seasons is None:
            for episode in self.show:
                yield episode.SeasonNumber, episode.EpisodeNumber, episode.EpisodeName
        else:
            for season in self.seasons:
                for episode in self.show[season]:
                    yield episode.SeasonNumber, episode.EpisodeNumber, ''.join([letter for letter in episode.EpisodeName if letter not in '?!:,'])


a = Serie('naruto')

b = list(a.get_episodes(1))


# print(b)

renamer.rename(Path("E:\\", 'code', 'outros', 'renamer', 'test'), b)

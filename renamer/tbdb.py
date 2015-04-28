import tvdb_api
from pytvdbapi import api
from pathlib import Path
import renamer
import sys



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
                    yield episode.SeasonNumber, episode.EpisodeNumber, ''.join([letter for letter in episode.EpisodeName if letter not in '!:,'])




a = Serie('code geass')

b = list(a.get_episodes(1))

# print(u'{}'.format(b[19][2]).encode('utf8'))]

# print(type(b[19][0]))


renamer.rename(Path("E:\\", 'code', 'outros', 'renamer', 'test'), b[0])
# print 'S{}{}E{}{} - {}'.format('0' if int(epi[0]) < 10 else '', epi[0], '0' if int(epi[1]) < 10 else '',epi[1], epi[2])

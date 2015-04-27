import tvdb_api
import sys
# sys.path.insert(0, 'E:\\code\outros\\renamer\\renamer.py')
import renamer
from pathlib import Path


class Serie(object):

    def __init__(self, series_name):
        self.name = series_name
        self.t = tvdb_api.Tvdb()

    def get_episodes(self, seasons=None):
        self.seasons = [seasons] or seasons
        try:
            show = self.t[self.name]
            for season in show:
                if None in self.seasons or season in self.seasons:
                    for _, name in show[season].items():
                        # yield season
                        yield u'S{}{}E{}{} - {}'.format('0' if season < 10 else '', season, '0' if int(name['episodenumber']) < 10 else '',name['episodenumber'], name['episodename']).encode('utf-8')

        except tvdb_api.tvdb_shownotfound:
            raise




a = Serie()

for epi in a.get_episodes(1):
    print epi
    # print 'S{}{}E{}{} - {}'.format('0' if int(epi[0]) < 10 else '', epi[0], '0' if int(epi[1]) < 10 else '',epi[1], epi[2])

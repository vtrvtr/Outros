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
                        # yield str(name).split()[1].split('x')
                        yield map(str, (name['dvd_season'], name['episodenumber'], name['episodename']))


        except tvdb_api.tvdb_shownotfound:
            raise




a = Serie('Code geass')

for epi in a.get_episodes(1):
    print 'S{}{}E{}{} - {}'.format('0' if int(epi[0]) < 10 else '', epi[0], '0' if int(epi[1]) < 10 else '',epi[1], epi[2])

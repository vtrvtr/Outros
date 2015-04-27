import tvdb_api
import sys
sys.path.insert(0, 'E:\\code\outros\\renamer\\renamer.py')
import renamer
from pathlib import Path




def get_episodes(show_name, seasons = None):
    t = tvdb_api.Tvdb()
    seasons = [seasons] or seasons
    print seasons
    try:
        show = t[show_name]
        for season in show:
            if None in seasons or season in seasons: 
                for number, name in show[season].items():
                    yield str(name).split()[1].split('x')
    except tvdb_api.tvdb_shownotfound:
        raise


for epi in get_episodes('code geass'):
    print 'S{}E{}'.format(epi[0], epi[1])

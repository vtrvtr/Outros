
import json
import urllib2
import pprint
from dota_web_api import Dota



a = Dota()
for games in a.live_league_games()[u'result'][u'games']:
    if games[u'league_tier'] == 3:
        try:
            print games[u'radiant_team'][u'team_name'] + ' vs ' + games[u'dire_team'][u'team_name']
        except KeyError:
            pass


api_key = '0848B3D94AE091E328050562DDF89B15'
import json
import urllib2
import pprint


class Dota(object):
    url = 'https://api.steampowered.com/IDOTA2Match_570/%s/V001/?'
    lang = 'en_us'

    def __get(self, method, *args, **kwargs):
        kwargs['key'] = '0848B3D94AE091E328050562DDF89B15'
        url = self.url % (
            method) + '&'.join([str(keys) + '=' + str(items) for keys, items in kwargs.items()])
        return json.loads(urllib2.urlopen(url).read())

    def match_history(self, *args, **kwargs):
        return self.__get('GetMatchHistory', *args, **kwargs)

    def match_details(self, matchid):
        return self.__get('GetMatchDetails', match_id=matchid)

    def league_listing(self):
        return self.__get('GetLeagueListing', langage=self.lang)

    def live_league_games(self):
        return self.__get('GetLiveLeagueGames', language=self.lang)

a = Dota()
for games in a.live_league_games()[u'result'][u'games']:
    if games[u'league_tier'] == 3:
        try:
            print games[u'radiant_team'][u'team_name'] + ' vs ' + games[u'dire_team'][u'team_name']

        except KeyError:
            pass

import mechanize
import pyperclip
import re
import google
from BeautifulSoup import BeautifulSoup
# site.select_form(nr=0)
# # site.formB['q'] = 'Hellraisers'
# resp = site.submit()
# soup = BeautifulSoup(site.response().read())
def main(player_name = '', team_name = ''):
    search = google.search('{} {} dotabuff'.format(player_name, team_name), num=1,stop=1)
    site_link = '{}/{}'.format(search.next(), 'matches')
    site = mechanize.Browser()
    site.addheaders = [('User-agent', 'Mozzila/5.0 ayy')]
    site.set_handle_robots(False)
    resp = site.open(site_link)
    soup = BeautifulSoup(resp)
    for links in soup('a'):
        if '/matches/' in str(links):
            #18 and 28 are where the game id are in the string
            print('Copied {} to the clipboard'.format(str(links)[18:28]))
            pyperclip.copy(str(links)[18:28])
 
            break

if __name__ == '__main__':
    try:
        team_name = raw_input('Team name?\n')
        player_name = raw_input('Player name?\n')
    except SyntaxError:
        team_name = ''
        player_name = raw_input('player name?\n')
    main(player_name, team_name)



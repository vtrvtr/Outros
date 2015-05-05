import logging
from pykeyboard import PyKeyboard
import time
from datetime import datetime
import argparse

PROCESSES = {'CouchPotato.exe': 'C:\Users\\vtrvtr\AppData\Roaming\CouchPotato\\application\CouchPotato.exe',
             'deluge.exe': 'E:\Programs\Deluge\deluge.exe',
             "SABnzbd.exe": 'E:\Programs\SABnzb\SABnzbd.exe',
             'transmission-qt.exe': 'E:\Programs\Transmission\\transmission-qt.exe',
             'nzbget.exe': 'E:\Programs\NZBGet\\nzbget.exe -s'}

logging.basicConfig(
    filename='E:\Code\Outros\Open Dowloaders\open_downloaders.log', level=logging.INFO)


def check_process(process_name):
    process_dict = {}
    for proc in psutil.process_iter():
        try:
            if proc.name() in process_name:
                logging.info(
                    '{} {} ({}) found'.format(datetime.now(), proc.name(), proc.pid))
                process_dict[proc.name().encode('ascii', 'ignore')] = proc.pid
        except psutil.AccessDenied:
            logging.error(
                '{} pid={} access denied'.format(datetime.now(), proc.pid))
            continue
    return process_dict


def open_p(processes):
    for proc in processes:
        sp.Popen(proc)
        logging.info('{} Opening {}'.format(datetime.now(), proc))


def close_p(processes):
    for proc in processes:
        p = psutil.Process(proc)
        p.terminate()
        logging.info('{} Closing {}'.format(datetime.now(), proc))


def main():
    parser = argparse.ArgumentParser(
        description="Opens or closes processes for Downloaders (Nzbget, CouchPotato, SabNzb, Deluge and Transmission")
    parser.add_argument(
        '--open', '-o', help="Open processes \n OBS: 'all' opens all processes", nargs='*', default=[])
    parser.add_argument(
        '--close', '-c', default=[], help="Close processes \n OBS: 'all' closes all processes", nargs='*')
    parser.add_argument('--quality', '-q', help='Chooses the quality to open streams, default = source', default='source')
    args = parser.parse_args()
    keyboard_needed = [
        True if 'couch' in args.open or 'couch' in args.close else False][0]
    # QOL change here to make easier to open / close specific processes
    translate_dic = {'couch': 'CouchPotato.exe',
                     'sab': 'SABnzbd.exe',
                     'transmission': 'transmission-qt.exe',
                     'deluge': 'deluge.exe',
                     'nzb': 'nzbget.exe'}
    if args.open == ['all']:
        open_p(PROCESSES.values())
    elif args.open and args.open is not False:
        # Get processes paths
        processes_to_open = [PROCESSES[v]
                             for k, v in translate_dic.items() if k in args.open]
        open_p(processes_to_open)
    if args.close == ['all']:
        close_p(check_process(PROCESSES.keys()).values())
    elif args.close != ['all'] and args.close is not False:
        processes_to_close = [v
                              for k, v in translate_dic.items() if k in args.close]
        close_p(check_process(processes_to_close).values())
    #This fixed the silly CouchPotato bug with its icon on windows
    if keyboard_needed:
        logging.info('{} Keyboard needed'.format(datetime.now()))
        keyboard = PyKeyboard()
        time.sleep(3)
        keyboard.tap_key(keyboard.enter_key)

if __name__ == "__main__":
    main()

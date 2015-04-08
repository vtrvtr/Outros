import subprocess as sp
import psutil
import logging
from pykeyboard import PyKeyboard
import time
from datetime import datetime

PROCESSES = {'CouchPotato.exe': 'C:\Users\\vtrvtr\AppData\Roaming\CouchPotato\\application\CouchPotato.exe',
             'deluge.exe': 'E:\Programs\Deluge\deluge.exe',
             "SABnzbd.exe": 'E:\Programs\SABnzb\SABnzbd.exe',
             'transmission-qt.exe': 'E:\Programs\Transmission\\transmission-qt.exe'}

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
    processes = check_process(PROCESSES.keys())
    keyboard_needed = [
        True if 'CouchPotato.exe' not in processes.keys() else False][0]
    if len(processes) != 4:
        print 'lol'
        closed_processes = [
            v for k, v in PROCESSES.items() if k not in processes.keys()]
        open_p(closed_processes)
    else:
        close_p(processes.values())
    if keyboard_needed:
        logging.info('{} Keyboard needed'.format(datetime.now()))
        keyboard = PyKeyboard()
        time.sleep(1)
        keyboard.tap_key(keyboard.enter_key)

if __name__ == "__main__":
    main()
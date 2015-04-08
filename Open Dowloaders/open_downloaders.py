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
    process_names = []
    process_pid = []
    for proc in psutil.process_iter():
        try:
            if proc.name() in process_name:
                logging.info(
                    '{} {} ({}) found'.format(datetime.now(), proc.name(), proc.pid))
                process_names.append(proc.name().encode('ascii', 'ignore'))
                process_pid.append(proc.pid)
        except:
            logging.error(
                '{} pid={} access denied'.format(datetime.now(), proc.pid))
            continue
    return (process_names, process_pid) if len(process_names) > 0 else False


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
    keyboard_needed = any(
        [True if 'CouchPotato.exe' in value else False for value in processes])
    if processes:
        close_p(processes[1])
    elif processes is False:
        open_p(PROCESSES.values())
    else:
        closed_processes = [v for k, v in PROCESSES.items() for i in range(
            len(processes[0])) if k != processes[0][i]]
        open_p(closed_processes)
    if keyboard_needed:
        logging.info('{} Keyboard needed'.format(datetime.now()))
        keyboard = PyKeyboard()
        time.sleep(1)
        keyboard.tap_key(keyboard.enter_key)

main()
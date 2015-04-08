import subprocess as sp
import psutil
import logging 
from pykeyboard import PyKeyboard
import time

PROCESSES = {'CouchPotato.exe': 'C:\Users\\vtrvtr\AppData\Roaming\CouchPotato\\application\CouchPotato.exe',
             'deluge.exe': 'E:\Programs\Deluge\deluge.exe',
             "SABnzbd.exe": 'E:\Programs\SABnzb\SABnzbd.exe',
             'transmission-qt.exe': 'E:\Programs\Transmission\\transmission-qt.exe'}


def check_process(process_name):
    process_names = []
    process_pid = []
    for proc in psutil.process_iter():
        try:
            if proc.name() in process_name:
                print proc.name()
                process_names.append(proc.name().encode('ascii', 'ignore'))
                process_pid.append(proc.pid)
        except:
            continue
    return (process_names, process_pid) if len(process_names) > 0 else False


def open_p(processes):
    for proc in processes:
        sp.Popen(proc)


def close_p(processes):
    for proc in processes:
        p = psutil.Process(proc)
        p.terminate()


def main():
    processes = check_process(PROCESSES.keys())
    if processes:
        close_p(processes[1])
    elif processes is False:
        open_p(PROCESSES.values())
    else:
        closed_processes = [v for k,v in PROCESSES.items() for i in range(len(processes[0])) if k != processes[0][i]]
        open_p(closed_processes)
    keyboard = PyKeyboard()
    time.sleep(1)
    keyboard.tap_key(keyboard.enter_key)





main()
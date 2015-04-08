import subprocess as sp
import psutil
from os import kill

PROCESSES = {'CouchPotato.exe': 'C:\Users\\vtrvtr\AppData\Roaming\CouchPotato\\application\CouchPotato.exe',
             'deluge.exe': 'E:\Programs\Deluge\deluge.exe',
             "SABnzbd.exe": 'E:\Programs\SABnzb\SABnzbd.exe',
             'transmission-qt.exe': 'E:\Programs\Transmission\\transmission-qt.exe'}


def check_process(process_name):
    opened_processes = []
    for proc in psutil.process_iter():
        try:
            if proc.name() in process_name:
                opened_processes.append(proc.pid)
        except:
            continue
    return opened_processes if len(opened_processes) > 0 else False


def open_p(processes):
    for proc in processes:
        sp.Popen(processes)


def close_p(processes):
    for proc in processes:
        p = psutil.Process(proc)
        p.terminate()


def main():
    processes = check_process(PROCESSES.keys())
    if processes:
        close_p(processes)
    else:
        open_p(PROCESSES.values())


print PROCESSES.values()

import subprocess as sp
import psutil


def check_process(process_name):
    opened_processes = []
    for proc in psutil.process_iter():
        try:
            if proc.name() in process_name:
                opened_processes.append(proc.name())
        except:
            continue
    return opened_processes if len(opened_processes) > 0 else False

print check_process(['CouchPotato.exe', 'deluge.exe'])

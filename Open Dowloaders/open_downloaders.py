import subprocess as sp
import psutil


def check_process(process_name):
    for proc in psutil.process_iter():
        try:
            if proc.name() in process_name:
                return True
        except:
            continue
    return False

print check_process(['CouchPotato.exe', 'deluge.exe'])
# print check_process('deluge.exe')

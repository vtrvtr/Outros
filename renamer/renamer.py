import argparse
import shutil
import logging
from pathlib import Path, WindowsPath
from tbdb import Serie


def transverse_directory(directory):
    yield directory
    for sub in directory.iterdir():
        if sub.is_dir():
            for subdirectory in transverse_directory(sub):
                yield subdirectory
        else:
            yield sub


def move_files(source, dest=None, extensions=[]):
    dest = dest or Path(source)
    for f in transverse_directory(Path(source)):
        if not f.is_dir():
            if f.suffix in extensions or len(extensions) == 0:
                try:
                    shutil.move(str(f), str(dest))
                    # print(str(f), str(dest))
                except shutil.Error:
                    pass


def count_files(source):
    if type(source) is not WindowsPath:
        source = Path(source)
    return len([f for f in source.iterdir() if f.is_file])


def rename(source, epi_info_list, extensions=['all']):
    files_in_folder = count_files(source)
    if type(source) is not WindowsPath:
        source = Path(source)
    if files_in_folder != len(epi_info_list):
        return 'Number of files different from number of episodes \n Files in folder: {} \n # of Episodes: {}'.format(files_in_folder, len(epi_info_list))
    for episode, epi_info in zip(source.iterdir(), epi_info_list):
        if not episode.is_dir():
            if episode.suffix in extensions or 'all' in extensions:
                with open(str(source / '{}_backup.txt'.format(source.name)), 'w+', encoding='utf-8') as f:
                    f.write('{}\n'.format(episode.name))
                # Goddanm japanese fucking characters are so sensitive when it
                # comes to strings, this fixes it
                path = "{}\S{}{}E{}{} - {}.mkv".format(str(source), 0 if epi_info[0] < 10 else '', epi_info[
                                                       0], 0 if epi_info[1] < 10 else '', epi_info[1], str(epi_info[2]))
                episode.replace(path)


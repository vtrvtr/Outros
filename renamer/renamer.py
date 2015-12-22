import argparse
import shutil
import logging
from pathlib import Path, WindowsPath
from tbdb import Serie
import sys


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
                except shutil.Error:
                    pass


def count_files(source):
    if type(source) is not WindowsPath:
        source = Path(source)
    return len([f for f in source.iterdir() if f.is_file])


def rename(source, epi_info, extensions=['all']):
    files_in_folder = count_files(source)
    n_episodes = len(epi_info)
    if type(source) is not WindowsPath:
        source = Path(source)
    if files_in_folder != n_episodes:
        print('Number of files different from number of episodes \n Files in folder: {} \n # of Episodes: {}'.format(
            files_in_folder, n_episodes))
        sys.exit()
    for episode, epi_info in zip(source.iterdir(), epi_info):
        if not episode.is_dir():
            if episode.suffix in extensions or 'all' in extensions:
                with open(str(source / '{}_backup.txt'.format(source.name)), 'a', encoding='utf-8') as f:
                    f.write('{}\n'.format(episode.name))
                # Goddanm japanese fucking characters are so sensitive when it
                # comes to strings, this fixes it
                path = "{}\S{}{}E{}{} - {}.mkv".format(str(source), 0 if epi_info[0] < 10 else '', epi_info[
                                                       0], 0 if epi_info[1] < 10 else '', epi_info[1], str(epi_info[2]))
                episode.replace(path)


def main(source_path, epi_info, extensions):
    rename(source_path, epi_info, extensions)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Rename files accordingly to TVDB info")
    parser.add_argument(
        '--path', '-p', help='Source path of the folder with video files', action="store")
    parser.add_argument('--info', '-i', help="Series name", action="store")
    parser.add_argument(
        '--extensions', '-e', help='media file extensions', default=['all'])
    args = parser.parse_args()
    if args.info:
        try:
            serie = Serie(args.info)
        except Exception as e:
            print(e)
        seasons = input('Which season to you like? Nothing for all seasons ')
        if seasons == '':
            seasons = None
        # for episode in serie.get_episodes(seasons):
        #     print(episode)
        # confirm = input('Do want to rename? y/n')
        # if not confirm:
        #     sys.exit()
        # else:
        main(args.path, serie.get_episodes(seasons), args.extensions)
    else:
        print('wrong info')

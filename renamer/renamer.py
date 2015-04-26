import argparse
import shutil
import logging
from pathlib import Path


def transverse_directory(directory):
    yield directory
    for sub in directory.iterdir():
        if sub.is_dir():
            yield from transverse_directory(sub)
        else:
            yield sub


def move_files(source, dest=None, extensions=[]):
    dest = dest or source.parent
    for f in transverse_directory(Path(source)):
        if not f.is_dir():
            if f.suffix in extensions or len(extensions) == 0:
                try:
                    shutil.move(str(f), str(dest))
                except shutil.Error:
                    pass


def rename(source, season='1', extensions=['.mkv', '.mp4', '.mov']):
    i_episode = 1
    for episode in transverse_directory(Path(source)):
        if not episode.is_dir():
            if episode.suffix in extensions:
                episode.rename(
                    source / 'S0{}E{}{}.mkv'.format(season, '0' if i_episode < 10 else '', i_episode))
                i_episode += 1


def main():
    parser = argparse.ArgumentParser(
        description='Renames files properly for easy Sonarr recognition')
    parser.add_argument('--move', '-m', help="Move all files with the EXTENSIONS from SOURCE to DEST \n default dest = source.parent", nargs='+')
    parser.add_argument(
        '--rename', '-r', help="Rename all files in SOURCE folder, needs to provide the correct SEASON", nargs='+')
    args = parser.parse_args()
    



if __name__ == '__main__':
    main()

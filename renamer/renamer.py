import argparse
import shutil
import logging
from pathlib import Path, WindowsPath

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


def rename(source, epi_info, extensions=['all']):
    if type(source) is not WindowsPath:
        source = Path(source)
    for episode in transverse_directory(source):
        if not episode.is_dir():
            if episode.suffix in extensions or 'all' in extensions:
                with open(str(source / '{}_backup.txt'.format(source.name)), 'w+', encoding='utf-8') as f:
                    f.write('{}\n'.format(episode.name))
                #Goddanm japanese fucking characters are so sensitive when it comes to strings, this fixes it
                path = "{}\S{}{}E{}{} - {}.mkv".format(str(source), 0 if epi_info[0] < 10 else '', epi_info[0], 0 if epi_info[1] < 10 else '', epi_info[1], str(epi_info[2]))
                # print(path)
                episode.replace(path)

def count_files(source):
    if type(source) is not WindowsPath:
        source = Path(source)
    return len([f for f in source.iterdir() if f.is_file])

def main():
    parser = argparse.ArgumentParser(
        description='Renames files properly for easy Sonarr recognition')
    parser.add_argument(
        '--move', '-m', help="Move all files with the EXTENSIONS from SOURCE to DEST \n default dest = source", action='store_true')
    parser.add_argument(
        '--rename', '-r', help="Rename all files in SOURCE folder, needs to provide the correct SEASON", action='store_true')
    args = parser.parse_args()
    if args.move:
        source = input('Where are the files now?\n')
        dest = input(
            'Where the files should be? \ntype ENTER for default folder\n')
        dest = dest if dest is not '' else None
        extensions = input(
            'Extensions of files you want to move \n type nothing to default types \n')
        extensions = extensions if extensions is not '' else [
            '.mkv', '.mp4', '.mov']
        move_files(source, dest, extensions)
    elif args.rename:
        source = input('Where are the files now?\n')
        season = input('What\'s the season?\n type nothing to 1')
        season = season if season is not '' else '1'
        extensions = input(
            'Extensions of files you want to move \n type nothing to default types \n')
        extensions = extensions if extensions is not '' else [
            '.mkv', '.mp4', '.mov']
        rename(source, season, extensions)

# if __name__ == '__main__':
#     main()



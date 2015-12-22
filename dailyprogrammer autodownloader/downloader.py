# Reddit Dailyprogrammer auto downloader
import praw
import os
from pathlib import Path
import datetime as dt
import logging
import sys

base_dir = os.path.dirname('E:\Code\Exercise-Codes\lol')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('downloader_log.log')
handler.setLevel(logging.INFO)
logger.addHandler(handler)


def get_Title():
    r = praw.Reddit('Dailyprogrammer daily question downloader')
    subreddit = r.get_subreddit('dailyprogrammer').get_new(limit=1)
    for s in subreddit:
        submission = r.get_submission(submission_id=s.id)
    return submission.title


def get_text():
    r = praw.Reddit('Dailyprogrammer daily question downloader')
    subreddit = r.get_subreddit('dailyprogrammer').get_new(limit=1)
    for s in subreddit:
        return s.selftext


def pathify_titles(titles):  # Makes the title into a correct path
    return Path(os.path.join(base_dir, titles))


# Creates the  if they don't already exist
def create_folders(titles, base_dir):
    title_path = pathify_titles(titles)
    if title_path.exists():
        logger.info('Folder {} already exists'.format(title_path))
    else:
        os.makedirs(str(title_path))
        logger.info('Creating folder {}'.format(title_path))

# Create the instruction file


def create_files(dir, message):
    instruction_path = str(dir / 'intructions.txt')
    py_path = str(dir / '{}.py'.format(dir.name))
    try:
        with open(instruction_path, 'a') as f:
            f.write(message)
    except IOError:
        print('File doesn`t exist')
    try:
        with open(py_path, 'w') as g:
            g.write(''' #{}
        def someFunction():
            pass'''.format(dir.name))
    except IOError:
        print('File doesn`t exist')


def main():
    title = get_Title()
    title_path = pathify_titles(title)
    if title_path.exists():
        logger.info(
            '{} Problem `{}` already exists'.format(dt.datetime.now(), title))
    else:
        submission_text = get_text()
        create_folders(title, base_dir)
        logger.info(
            '{} Creating folder {}'.format(dt.datetime.now(), title_path))
        create_files(title_path, submission_text)
        logger.info('{} Creating files `instruction.txt` and {}.py '.format(
            dt.datetime.now(), title))

if __name__ == "__main__":
    import traceback
    try:
        main()
    except:
        logger.info(
            '{} Error: {}'.format(dt.datetime.now(), traceback.print_exc()))


import urllib.request
import urllib.parse
import re
import pickle

FILE_PATH = 'E:\Code\clovis_video_crawler\\videos.p'

def search_youtube(query):
    query_string = urllib.parse.urlencode({"search_query" : query})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return set(search_results)

def update_links_library(old_links, new_links):
    '''old_links: links already in the pickle file -> set
       new_links: links from the new query -> set'''
    return old_links.union(new_links)

def store_videos(links):
    '''links: complete set of links'''
    with open(FILE_PATH, 'wb') as f:
        pickle.dump(links, f)

def open_pickle():
    with open(FILE_PATH, 'rb') as f:
        return pickle.load(f)

def main():
    old_links = open_pickle()
    new_links = search_youtube('clovis de barros')
    updated_library = update_links_library(old_links, new_links)
    store_videos(updated_library)

if __name__ == '__main__':
    main()


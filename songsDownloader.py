# -*- coding: utf-8 -*-
"""
@author: Surendra
"""

from __future__ import unicode_literals
import youtube_dl
import urllib2
import warnings
import os
from bs4 import BeautifulSoup

def getDirName(str):
    source = urllib2.urlopen(str)
    BS = BeautifulSoup(source)
    plName = BS.find('div', attrs={'class':'playlist-header-content'})
    print(plName)
    if(plName != None):
	    plName = plName['data-list-title']
	    return ''.join(e for e in plName if (e.isalnum() or e.isspace()))
    return None

ydl_opts = {
    'format': 'bestaudio/best',
    'ignoreerrors' : True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '0',
    }],
}

playLists = ['playlist1', 'playlist2', 'song2', '...']

def main():
    for pl in playLists:
        plName = getDirName(pl)
        if(plName != None):
            if not os.path.exists(plName):
                os.makedirs(plName)
            os.chdir(plName)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([pl])
        if(plName != None):
            os.chdir("..")
            
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    main()

#!pip install pytube
from pytube import Playlist
from threading import Thread
import argparse
import os
def downloader(video,download_type,folder_name) :
        print("Download started",video.title)
        if download_type ==  'audio' :
            orgiginal_file=video.streams.filter(only_audio=True)[0].download(folder_name+'audio')
            base, ext = os.path.splitext(orgiginal_file)
            new_file = base + '.mp3'
            os.rename(orgiginal_file, new_file)  
        else :
            orgiginal_file=video.streams.first().download(folder_name+'video')

        
        print("Downloaded",video.title)


def load(url,download_type) :
    pl = Playlist(url)
    folder_name='PLAYLIST_'+pl.title

    for video in pl.videos:
        process = Thread(target=downloader, args=[video,download_type,folder_name])
        process.start()
        
        

parser = argparse.ArgumentParser(description='enter playlist link')
parser.add_argument('--playlist', help='playlist link')
parser.add_argument('--type', help='audio video')        
        
args = parser.parse_args()

load(args.playlist,args.type)     
        
#load('https://www.youtube.com/playlist?list=PLeF9GF96N91JMYGp5ylagtH8rPlgmj18g')
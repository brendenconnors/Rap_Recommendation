# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:56:24 2020

@author: conno
"""
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen
import re
from concurrent.futures import ProcessPoolExecutor, as_completed
import time

def get_lyrics(url):
    req = Request(url,headers = {'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")
    try:
        lyrics = soup.find('div', {"class": "lyrics"}).getText()
    except:
        return "No lyrics found"
    
    #remove bracketed sections like [Chorus]
    lyrics = re.sub("[\(\[].*?[\)\]]", "", lyrics)  
    #remove repeated line breaks. We will break by line for analysis
    lyrics = re.sub("\n{2,}", "\n", lyrics)
    
    if lyrics[:1] =='\n':
        lyrics=lyrics[1:]
    
    
    return lyrics


def find_lyric_progress(output_file):
    try:
        df=pd.read_csv(output_file,sep='\t')
        completed_songs = list(df.song_id.unique())
        mode='a'
    except:
        mode='w'
        completed_songs=None
        
    return completed_songs,mode
        
def get_song_duration(url):
    req = Request(url,headers = {'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "lxml")
    music_player = soup.find('apple-music-player')
    
    try:
        duration =music_player['preview_track'].split('duration":')[1] #imports dictionary as string, won't convert
        duration = duration.split(',')[0]
        
        
    except:
        duration=0
    
    if duration==None:
        duration=0
    return duration


def master_scraper(row):
    base_url_player = r'https://genius.com/songs/'
    end_url_player ='/apple_music_player'
    base_url_lyrics = r'https://genius.com'
    song_id = str(row.song_id)
    url_player = base_url_player+song_id+end_url_player
    duration = get_song_duration(url_player)

    try:
        lyrics = get_lyrics(base_url_lyrics+row.url_extension)
        
    except:
        pass

    return lyrics,duration,song_id


file = r'C:\Users\conno\Documents\text_mining\repos\Lyric Scraper\song_ids_full.txt'
duration_file = r'C:\Users\conno\Documents\text_mining\repos\Lyric Scraper\song_durations.txt'

#get our progress in case we start/stop the process
try:
    completed_songs,mode = find_lyric_progress(duration_file)
except:
    completed_songs=[]
    mode='w'

#remove songs we have completed    
df = pd.read_csv(file,sep='\t')
df = df[~df.song_id.isin(completed_songs)]


#create a nice iterable for our multi-threaded scraper
rows=[row for index,row in df.iterrows()]

#chunk our iterator so we don't get a drone strike sent to our house for blowing up their server
batch_size=500
row_chunks =[rows[step:step+batch_size] for step in range(0, len(rows), batch_size)]

        
n=0        
        
if  __name__ == '__main__':
    
    with ProcessPoolExecutor(max_workers=5) as executor:
        for chunk in row_chunks:
            futures = [executor.submit(master_scraper, row) for row in chunk]
            for result in as_completed(futures):
                
                try:
                    lyrics,duration,song_id=result.result()
                    
                except:
                    continue
                
                print(duration)

                duration=str(duration)
                

                
                with open(r'C:\Users\conno\Documents\text_mining\repos\Lyric Scraper\Lyrics\\' + song_id+'_lyrics'+'.txt','w',encoding='utf-8') as outfile:
                    outfile.write(lyrics)
                    
                if mode=='a':
                    with open(duration_file,'a',encoding='utf-8') as outfile:
                        outfile.write(song_id+'\t'+duration+'\n')
                        
                else:
                    with open(duration_file,'w',encoding='utf-8') as outfile:
                        outfile.write('song_id'+'\t'+'duration'+'\n')
                        outfile.write(song_id+'\t'+duration+'\n')
                    mode = 'a'  

            time.sleep(60) #give a little time to rest/sleep

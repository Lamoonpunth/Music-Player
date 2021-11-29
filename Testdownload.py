import youtube_dl
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem



def run():
    video_url = input("please enter youtube video url: ")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':f'archive/song/{filename}',
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl._ies = [ydl.get_info_extractor('Youtube')]
        ydl.download([video_info['webpage_url']])
    
    print("Download complete... {}".format(filename))   
   
    g = open("archive/song/yoursongpath.txt", "r+",encoding='utf-8')
    Write = True
    for i in g:                 
        if filename in i:
            Write = False
            break  
    g.close()      
    #write
    if Write: 
        f = open("archive/song/yoursongpath.txt", "a",encoding='utf8')  
        f.write(f'archive/song/{filename}\n')
        f.close()
    
if __name__=='__main__':
    run()
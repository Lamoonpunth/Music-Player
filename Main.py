from re import search
from kivy.config import Config
Config.set('graphics','resizable', False)
from os import stat
from kivy import clock
from kivy.app import App
from kivy.core import text
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.button import MDIconButton
from kivy.clock import Clock
from kivy.animation import Animation
import threading 
from playlist import playlist
from playingqueue import playingqueue
from song import song
from HoverImage import HoverImage
import SlideNorn
from kivymd.app import MDApp
from SongBox import SongBox
import pyautogui
from PlaylistBox import PlaylistBox
from kivy.core.text import LabelBase
from DownLoadButton import DownloadURL
# from SongBrowser import AddSong
from SongBrowser import Browser
import time
import random
import PlayButton
import NextPrevButton
import ShuffleButton
import RepeatButton
import QueueButton
import nltk
from sort import quick_sort

# Add Font
LabelBase.register(name='sf',fn_regular='archive/finalFontV2.ttf')

# Load KV File
Builder.load_file('main.kv')
# Get user screen display size
user_width, user_height = pyautogui.size()
# # Adjust Window size when start

Window.maximize()

class MainGridLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f'Main width = {self.width}')
        print(f'Main height = {self.height}')
        self.yoursong=[]
        self.playlistlist=[]
        self.reload()
        # self.start_stop.bind(on_press=self.press)
        self.play.bind(on_press=self.press)
        self.next.bind(on_press=self.nextpress)
        self.prev.bind(on_press=self.prevpress)
        self.shuffle.bind(on_press=self.shuffleState)
        self.bool = False
        Clock.schedule_interval(lambda dt: self.playtimeUpdate(), 0.1)
        self.queue = playingqueue()
        self.queue.chooseplaylist(self.yoursong)
        self.queue.addfromqueuefirstsong()
        #Load Song
        self.soundpath = self.queue.nowplaying.getpath()
        print(self.queue.nowplaying)
        self.sound = SoundLoader.load(self.soundpath)
        self.ids.song_name.text=self.queue.nowplaying.getname()
        self.ids.song_name.font_name = 'sf'
        # anim = Animation(x=-100,duration=10)
        # anim.repeat = True
        # anim.start(self.ids.song_name)
        self.volume = 0.25
        #seek
        self.seekvalue = 0
        self.playtimeUpdateBool = True
        #slidenorninit
        self.playlistindex=0
        self.showsong(self.yoursong)
        self.showplaylist(self.playlistlist)
        self.ids.playlist_name.text = f'{self.playlistlist[self.playlistindex].name}'
        #Add file and Download Components
        download_box = DownloadURL()
        song_browser = Browser().AddSong()
        self.ids.playlist_name_box.add_widget(download_box)
        self.ids.playlist_name_box.add_widget(song_browser)
        #search
        self.searchedPlaylist = playlist('sPlaylist')       
        self.searchedShow = False

    class Refresh(MDIconButton):
        pass

    def showplaylist(self,playlistlist):
        self.ids.playlistslide.clear_widgets()
        for i in range(len(playlistlist)):
            lb = PlaylistBox(i,playlistlist[i].name)
            self.ids.playlistslide.add_widget(lb)
            lb.bind(on_press=self.selectplaylist)

    def showqueue(self,source):
        if source is "touch" and self.ids.queue_list.queueshownow is True:
            return
        else:   
            self.ids.queue_list.queueshownow = True
            self.ids.queue_list.text_color=(1,0.60,0.75,1)
            self.ids.playlist_name.text='Queue'
            self.ids.sn.clear_widgets()
            for i in range(len(self.queue.musicqueue)):
                t = self.queue.musicqueue[i].time
                new_t = (t//60) + ((t%60)/100)
                new_t = format(new_t,'.2f')
                time_text = f'{new_t}'
                lb = SongBox(i+1,self.queue.musicqueue[i].name,time_text)
                self.ids.sn.add_widget(lb)

    def showsong(self,playlist): #spiderman
        self.ids.queue_list.queueshownow = False
        self.ids.queue_list.text_color=(0.6,0.6,0.6,1)
        self.ids.sn.clear_widgets()
        for i in range(len(playlist.playlist)):
            t = playlist.playlist[i].time
            new_t = (t//60) + ((t%60)/100)
            new_t = format(new_t,'.2f')
            time_text = f'{new_t}'
            lb = SongBox(i+1,playlist.playlist[i].name,time_text)
            self.ids.sn.add_widget(lb)
            lb.bind(on_press=self.selectsong)

    # Volume Bar(เพิ่มลดเสียง)
    def slide_it(self, *args):
        self.volume = float(args[1]/100)
        self.sound.volume = self.volume

    # Update ProgressBar in Volume bar(แสดงผลระดับเสียง)
    def valuechange(self,*args):
        self.seekvalue=args[1]

    # Not update song time when hold(ดักไว้ให้ค่าไม่เปลี่ยนตอนกำลังเลื่อนเวลาเพลง)
    def notupdate(self,*args):
        print("ontouchdown")
        self.playtimeUpdateBool=False

    # Seek song time(เลื่อนเวลาในเพลง)
    def seek(self, *args):
        if self.playtimeUpdateBool is False:
            self.playtimeUpdateBool = True
            print("ontouchup")
            #print (sound.state)
            #print (sound.length)
            if (self.sound.state=='play'):
                print(self.seekvalue)
                self.sound.seek(self.seekvalue*self.sound.length/10000)
            else:
                self.sound.play()
                self.sound.seek(self.seekvalue*self.sound.length/10000)
                self.sound.stop()

    # Play button(ปุ่มเปิด-ปิดเพลง)
    def press(self, instance):
            self.ids.play.user_font_size= 80

            if self.bool is False:
                self.play = Button(text='Play')
                self.bool = True
                self.sound.volume = self.volume+0.001
                self.sound.volume = self.volume
                self.sound.play()
                self.sound.volume = self.volume+0.001
                self.sound.volume = self.volume
                self.ids.play.icon = 'pause-circle'
            else:
                self.play = Button(text='Stop')
                self.bool = False
                self.sound.stop()
                self.ids.play.icon = 'play-circle'

    # Forward song(เปลี่ยนเพลงไปคิวถัดไป)
    def nextpress(self,instance):
        if self.queue.isEmpty() and self.ids.repeat.repeatstate == "repeatplaylist":
            self.queue.chooseplaylist(self.queue.originalplaylist)
        elif self.queue.isEmpty():
            print("QueueIsEmpty")
            return
        self.sound.stop()
        self.queue.addfromqueue()
        self.soundpath = self.queue.nowplaying.getpath()
        self.sound = SoundLoader.load(self.soundpath)
        self.ids.song_name.text=self.queue.nowplaying.getname()
        self.sound.volume = self.volume+0.001
        self.sound.volume = self.volume
        self.sound.play()
        self.sound.volume = self.volume+0.001
        self.sound.volume=self.volume
        self.playtimeUpdate()
        self.bool = True
        self.ids.play.icon = 'pause-circle'
        if self.ids.queue_list.queueshownow is True:
            self.showqueue("auto")
    
    # Backward song(เปลี่ยนเพลงย้อนไปคิวก่อนหน้านี้)
    def prevpress(self,instance):
        if self.queue.isStackEmpty():
            print("StackIsEmpty")
            return
        self.sound.stop()
        self.queue.addfromstack()
        self.soundpath = self.queue.nowplaying.getpath()
        self.sound = SoundLoader.load(self.soundpath)
        self.ids.song_name.text=self.queue.nowplaying.getname()
        self.sound.play()
        self.sound.volume = self.volume+0.001
        self.sound.volume=self.volume
        self.playtimeUpdate()

    # Update ProgressBar in SongTime bar(แสดงผลช่วงเวลาในเพลง)
    def playtimeUpdate(self):        
        self.sound.volume = self.volume+0.001
        self.sound.volume = self.volume       
        if self.playtimeUpdateBool is True:
            #print(self.ids.playtime.value_pos)
            value=int(self.sound.get_pos()*10000/self.sound.length)
            if value>=9990:
                if self.ids.repeat.repeatstate == "repeatsong":
                    self.sound.seek(0)
                else:
                    self.nextpress("instance")
                value=0
            self.ids.playtime.value=value

    # Shuffle song toggle button(เลือกเพื่อสุ่มเพลง)
    def shuffleState(self, instance):
        if self.ids.shuffle.state is 'down':
            self.ids.shuffle.text_color = [0.6,0.6,0.6,1]
            print(f'Shuffle is ON')
            random.shuffle(self.queue.musicqueue)
        else:
            self.ids.shuffle.text_color = [1,0.41,0.69,1]
            print(f'Shuffle is OFF')
            index=self.queue.nowplayingindex
            self.queue.chooseplaylist(self.queue.originalplaylist)
            self.queue.addfromqueuefirstsong()
            for i in range(index):
                self.queue.addfromqueue()   

    # Choose song from songlist(ฟังก์ชันเมื่อกดเลือกเพลงจากในเพลย์ลิสต์)
    def selectsong(self,*args):
        self.sound.stop()
        index=args[0].index
        if self.searchedShow is True:
            self.queue.chooseplaylist(self.searchedPlaylist)
        else:
            self.queue.chooseplaylist(self.playlistlist[self.playlistindex])
        self.queue.addfromqueuefirstsong()
        for i in range(index):
            self.queue.addfromqueue()
        self.soundpath = self.queue.nowplaying.getpath()
        self.sound = SoundLoader.load(self.soundpath)
        self.ids.song_name.text=self.queue.nowplaying.getname()
        self.sound.volume = self.volume+0.001
        self.sound.volume=self.volume
        self.sound.play()
        self.sound.volume = self.volume+0.001
        self.sound.volume=self.volume
        self.playtimeUpdate()
        self.bool = True
        self.ids.play.icon = 'pause-circle'
        #print(self.searchedShow,' ooo o oo ')

    # Choose playlist(ฟังก์ชันสำหรับเลือกเพลย์ลิสต์)
    def selectplaylist(self,*args):
        index=args[0].index 
        self.playlistindex=index
        self.showsong(self.playlistlist[index])
        self.ids.playlist_name.text = f'{self.playlistlist[index].name}'
        self.searchedShow = False
    
    # Search song in Playlist(ค้นหาเพลงในเพลย์ลิสต์)
    def Searched_Song(self, text="", search=False):               
        # t3 = threading.Thread(target=self.searchT3,args=(text,search,), name='t3')              
        # t3.start()    
        # print(f'Active Threads: {threading.active_count()}')                 
        self.searchedPlaylist.clearSong()
        ListofSong =[]
        ListofSim =[]
        temp = None
        for songg in self.playlistlist[self.playlistindex].playlist:
            #slidingwindow
            if range(len(songg.name.casefold())<len(text.casefold())):
                val=999
            else:
                val=999
                for i in range(len(songg.name.casefold())-len(text.casefold())):
                    temp = nltk.edit_distance(text.casefold(),songg.name.casefold()[i:i+len(text.casefold())])
                    if temp<val:
                        val=temp
            ListofSong.append(songg)
            ListofSim.append(val)                          
        temp = list(zip(ListofSim,ListofSong))
        quick_sort(0,len(temp)-1,temp)
        for i in range(len(temp)):        
            self.searchedPlaylist.addsong(temp[i][1])                                    
        # print('------------')           
        self.searchedShow = search
        if text =='':
            self.searchedShow = False
        if self.searchedShow:
            self.showsong(self.searchedPlaylist)
        else:
            self.showsong(self.playlistlist[self.playlistindex])
        
    def searchT3(self,text,search):
        self.searchedPlaylist.clearSong()
        ListofSong =[]
        ListofSim =[]
        temp = None
        for songg in self.playlistlist[self.playlistindex].playlist:
            #slidingwindow
            if range(len(songg.name.casefold())<len(text.casefold())):
                val=999
            else:
                val=999
                for i in range(len(songg.name.casefold())-len(text.casefold())):
                    temp = nltk.edit_distance(text.casefold(),songg.name.casefold()[i:i+len(text.casefold())])
                    if temp<val:
                        val=temp
            ListofSong.append(songg)
            ListofSim.append(val)                          
        temp = list(zip(ListofSim,ListofSong))
        quick_sort(0,len(temp)-1,temp)
        for i in range(len(temp)):        
            self.searchedPlaylist.addsong(temp[i][1])                                    
        # print('------------')           
        self.searchedShow = search
        if text =='':
            self.searchedShow = False
        if self.searchedShow:
            self.showsong(self.searchedPlaylist)
        else:
            self.showsong(self.playlistlist[self.playlistindex])
      
    def refresh(self):
        self.reload()
        self.showplaylist(self.playlistlist)
        self.showsong(self.yoursong)
        print(self.playlistlist)
        print(self.playlistlist[0])
        self.queue.chooseplaylist(self.yoursong)
        

    def reload(self):
        fullpath=[]
        f = open("archive/song/yoursongpath.txt", "r+",encoding='utf-8')
        index=0
        for x in f:    
            if x[-1:] == "\n":
                s=song(x[:-1],index)
                index+=1
                fullpath.append(s)
        f.close()
        self.yoursong = playlist("yoursong",fullpath)

        templist=[]
        self.playlistlist=[]
        self.playlistlist.append(self.yoursong)
        f = open("archive/song/playlist.txt", "r+",encoding='utf-8')
        index=0
        for x in f:
            if x[-1:] == "\n":
                if x[0] is "%":
                    self.playlistlist.append(playlist(x[1:-1],templist.copy()))
                    templist=[]
                    index=0
                    continue
                s=song(x[:-1],index)
                index+=1
                templist.append(s)
        f.close()

# Main Application running Function
class MainApp(MDApp):
    def build(self):
        self.title = 'Wanwai Player'
        self.icon = 'Icon/title.png'
        #=========== theme ===========#
        self.theme_cls.primary_palette = "Gray"
        #=========== theme ===========#

        #=========== Icon ============#
        
        #=========== Icon ============#

        return MainGridLayout()

# Main Function to run App
if __name__ == "__main__":
    MainApp().run()
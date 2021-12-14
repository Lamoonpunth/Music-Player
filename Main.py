from re import search
from kivy.config import Config
from kivymd.uix import boxlayout
from ClearQueueBox import ClearQueueBox
#from kivymd.uix.button.button import MDFlatButton
from PlaylistDialogBox import PlaylistDialogBox
Config.set('graphics','resizable', False)
from os import stat
from kivy import clock
from kivy.app import App
from kivy.core import text
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix import boxlayout
#from kivymd.uix.button.button import MDFlatButton
from kivymd.uix.button import MDIconButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.slider import MDSlider
from kivy.clock import Clock
from kivy.animation import Animation
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
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
from kivy.core.text import Label, LabelBase
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
import AddPlaylistButton
from PlaylistDialogBox import PlaylistDialogBox
from AddSongBox import AddSongBox
import nltk
from sort import quick_sort
# Add Font
LabelBase.register(name='sf',fn_regular='archive/finalFontV2.ttf')
Config.set('input', 'mouse', 'mouse,disable_multitouch')
# Load KV File
# Builder.load_file('main.kv')
# Get user screen display size
user_width, user_height = pyautogui.size()
# # Adjust Window size when start

Window.maximize()

class MainGridLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #print(f'Main width = {self.width}')
        #print(f'Main height = {self.height}')
        # Window.bind(on_maximize=self.fixscroll)
        # Window.bind(on_minimize=self.fixscroll)
        self.yoursong=[]
        self.playlistlist=[]
        self.menu_playlist=[]
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
        #print(self.queue.nowplaying)
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
        #Add file and Download Components
        download_box = DownloadURL()
        song_browser = Browser().AddSong()
        self.ids.change_position1.add_widget(download_box)
        self.ids.change_position2.add_widget(song_browser)
        #search
        self.searchedPlaylist = playlist('sPlaylist')       
        self.searchedShow = False 
        self.searchThread = False
        self.isSearched = False
        self.searchQueue = []
        #dropdownmenu
        self.menu = MDDropdownMenu(
            width_mult=4,
            background_color=(0.2,0.2,0.2,1),
            hor_growth = 'right',

        )
        self.dropdownplaylist = MDDropdownMenu(
            width_mult=4,
            background_color=(0.2,0.2,0.2,1),
        )
        #addsongtoplaylist
        self.selectedsongpath=""
        self.dialogitems=[]
        for i in range(len(self.playlistlist)):
            if i==0:
                continue
            else:
                lb=PlaylistDialogBox(i,self.playlistlist[i].name)
                lb.index=i
                self.dialogitems.append(lb)
        self.dialog=MDDialog(
                title="Choose Playlist",
                type="simple",
                items=self.dialogitems,
                radius=[20, 7, 20, 7],                
            )
        Window.maximize()
        #slidenorninit
        self.playlistindex=0
        self.showsong(self.yoursong)
        self.showplaylist(self.playlistlist)
        self.ids.playlist_name.text = f'{self.playlistlist[self.playlistindex].name}'

    class Refresh(MDIconButton):
        pass

    def showplaylist(self,playlistlist):
        self.ids.playlistslide.clear_widgets()
        for i in range(len(playlistlist)):
            lb = PlaylistBox(i,playlistlist[i].name)
            self.ids.playlistslide.add_widget(lb)
            lb.bind(on_touch_down=self.selectplaylist)

    def showqueue(self,source):
        if source is "touch" and self.ids.queue_list.queueshownow is True:
            return
        else:   
            self.ids.queue_list.queueshownow = True
            self.ids.queue_list.text_color=(1,0.60,0.75,1)
            self.ids.playlist_name.text='Queue'
            self.ids.sn.clear_widgets()
            lb =ClearQueueBox()
            self.ids.sn.add_widget(lb)
            lb.bind(on_touch_down=self.clearqueue)
            for i in range(len(self.queue.musicqueue)):
                t = self.queue.musicqueue[i].time
                new_t = (t//60) + ((t%60)/100)
                new_t = format(new_t,'.2f')
                time_text = f'{new_t}'
                lb = SongBox(i+1,self.queue.musicqueue[i].name,time_text)
                self.ids.sn.add_widget(lb)
                lb.bind(on_touch_down=self.selectsonginqueue)

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
            lb.bind(on_touch_down=self.selectsong)
            #dropdown
        lb = AddSongBox()
        self.ids.sn.add_widget(lb)
    
    def clearqueue(self,instance,touch):
        if instance.collide_point(touch.x,touch.y):
            self.queue.clearqueue()
            self.showqueue("auto")
    def addsongtoplaylist(self,instance,touch):
        if instance.collide_point(touch.x,touch.y):
            self.dialog.dismiss()
            playlistindex=instance.index
            self.playlistlist[playlistindex].addsong(self.selectedsongpath)
            #write
            self.updateplaylistfile()
    
    def updateplaylistfile(self):
        f = open("archive/song/playlist.txt", "w",encoding='utf-8')
        for i in range(len(self.playlistlist)): 
            if i ==0:
                continue
            else:
                for j in range(len(self.playlistlist[i].playlist)):
                    f.write(self.playlistlist[i].playlist[j].path+"\n")
                f.write("%"+self.playlistlist[i].name+"\n")
        f.close()
    # Volume Bar(เพิ่มลดเสียง)
    def slide_it(self, *args):
        self.volume = float(args[1]/100)
        self.sound.volume = self.volume

    # Update ProgressBar in Volume bar(แสดงผลระดับเสียง)
    def valuechange(self,*args):
        self.seekvalue=args[1]

    # Not update song time when hold(ดักไว้ให้ค่าไม่เปลี่ยนตอนกำลังเลื่อนเวลาเพลง)
    def notupdate(self,*args):
        #print("ontouchdown")
        self.playtimeUpdateBool=False

    # Seek song time(เลื่อนเวลาในเพลง)
    def seek(self, *args):
        if self.playtimeUpdateBool is False:
            self.playtimeUpdateBool = True
            #print("ontouchup")
            #print (sound.state)
            #print (sound.length)
            if (self.sound.state=='play'):
                #print(self.seekvalue)
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
        added=False
        if self.queue.isEmpty() and self.ids.repeat.repeatstate == "repeatplaylist":
            self.queue.chooseplaylist(self.queue.originalplaylist)
            self.queue.addfromqueuefirstsong()
            added=True
        elif self.queue.isEmpty():
            print("QueueIsEmpty")
            return
        self.sound.stop()
        if added is False:
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
        if self.searchQueue != [] and self.searchThread is False:
            t3 = threading.Thread(target=self.StartSearchThread,args=(self.searchQueue.pop(0),search,), name='SearchingThread')              
            t3.start()                
        self.sound.volume = self.volume+0.001
        self.sound.volume = self.volume       
        if self.playtimeUpdateBool is True:
            #print(self.ids.playtime.value_pos)
            value=int(self.sound.get_pos()*10000/self.sound.length)
            if self.sound.length-self.sound.get_pos()<=0.2:
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

    def addtoqueue(self):
        self.queue.enqueue(self.playlistlist[self.playlistindex].playlist[self.menu.caller.index])
        self.menu.dismiss()
    def removesongfromplaylist(self):
        for i in self.playlistlist:
            print(i.name,end=" ")
        self.playlistlist[self.playlistindex].removesong(self.menu.caller.index)
        print("")
        for i in self.playlistlist:
            print(i.name,end=" ")
        #write
        self.menu.dismiss()
        self.updateplaylistfile()
        self.showsong(self.playlistlist[self.playlistindex])
    def removefromqueue(self,instance):
        self.queue.clearonesong(instance.index)
        self.showqueue("auto")
        self.menu.dismiss()

    def selectsonginqueue(self,instance,touch):
        if instance.collide_point(touch.x,touch.y):
            if touch.button == 'right':
                self.menu_items = [{
                            "text": f"Remove from queue",
                            "viewclass": "OneLineListItem",
                            "on_release": lambda x=0:self.removefromqueue(instance),
                            "theme_text_color" : "Custom",
                            "text_color" : (1,.41,.69,1),
                           
                        },]
                self.menu.caller = instance
                self.menu.items = self.menu_items
                self.menu.open()

    # Choose song from songlist(ฟังก์ชันเมื่อกดเลือกเพลงจากในเพลย์ลิสต์)
    def selectsong(self,instance,touch):
        #print("instance {}".format(instance))
        #print("touch {}".format(touch))
        if instance.collide_point(touch.x,touch.y):
            if touch.button == 'right':
                self.selectedsongpath=self.playlistlist[self.playlistindex].playlist[instance.index]
                if self.playlistindex == 0:
                    self.menu_items = [
                        {
                            "text": f"Add to queue",
                            "viewclass": "OneLineListItem",
                            "on_release": lambda x=0:self.addtoqueue(),
                            "theme_text_color" : "Custom",
                            "text_color" : (1,.41,.69,1),
                           
                        },
                        {
                            "text": f"Add to playlist",
                            "viewclass": "OneLineListItem",
                            "on_release": self.show_confirmation_dialog,
                            #"on_release": lambda x=0:self.show_confirmation_dialog(),
                            "theme_text_color" : "Custom",
                            "text_color" : (1,.41,.69,1),
                            
                            # "on_leave": lambda x=0:self.dropdownplaylist.dismiss(),
                        },

                    ]
                else:
                    self.menu_items = [
                        {
                            "text": f"Add to queue",
                            "viewclass": "OneLineListItem",
                            "on_release": lambda x=0:self.addtoqueue(),
                            "theme_text_color" : "Custom",
                            "text_color" : (1,.41,.69,1),
                        },
                        {
                            "text": f"Remove from playlist",
                            "viewclass": "OneLineListItem",
                            "on_release": lambda x=0:self.removesongfromplaylist(),
                            "theme_text_color" : "Custom",
                            "text_color" : (1,.41,.69,1),
                        },
                    ]
                print("open")
                print(instance)
                self.menu.caller = instance
                self.menu.items = self.menu_items
                self.menu.open()
            else:
                self.sound.stop()
                index=instance.index
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
    def show_confirmation_dialog(self):
        self.dialogitems=[]
        for i in range(len(self.playlistlist)):
            if i==0:
                continue
            else:
                lb=PlaylistDialogBox(i,self.playlistlist[i].name)
                lb.index=i
                self.dialogitems.append(lb)
                lb.bind(on_touch_down=self.addsongtoplaylist)
        self.dialog=MDDialog(
                title="Choose Playlist",               
                type="simple",
                items=self.dialogitems,
                radius=[20, 7, 20, 7],
                md_bg_color=(.85,.85,.85,1),                
            )
        self.dialog.open()

    def close_dialog(self,*args):
        self.dialog.dismiss()

    def changeselectedplaylist(self,index):
        self.playlistindextoaddsong=index
        print(index)
    # Choose playlist(ฟังก์ชันสำหรับเลือกเพลย์ลิสต์)
    def selectplaylist(self,instance,touch):
        if instance.collide_point(touch.x,touch.y):
            if touch.button == 'right':
                if instance.index==0:
                    return
                self.playlistoption = [
                    {
                        "text": f"Remove Playlist",
                        "viewclass": "OneLineListItem",
                        "on_release": lambda x=0:self.removeplaylist(instance.index),
                        "theme_text_color" : "Custom",
                        "text_color" : (1,.41,.69,1),
                    },
                    {
                        "text": f"Rename Playlist",
                        "viewclass": "OneLineListItem",
                        "on_release": lambda x=0:self.removeplaylist(instance.index),
                        "theme_text_color" : "Custom",
                        "text_color" : (1,.41,.69,1),
                    },
                ]                                            
                
                self.dropdownplaylist.caller = instance
                self.dropdownplaylist.items = self.playlistoption         
                self.dropdownplaylist.open()
            else:
                index=instance.index 
                self.playlistindex=index
                
                self.ids.playlist_name.text = f'{self.playlistlist[index].name}'
                self.showsong(self.playlistlist[index])
                self.searchedShow = False

    def removeplaylist(self, playlistindex):
        self.playlistlist.pop(playlistindex)
        self.updateplaylistfile()
        self.ids.playlist_name.text = f'{self.playlistlist[0].name}'
        self.showsong(self.playlistlist[0])
        self.showplaylist(self.playlistlist)
        self.dropdownplaylist.dismiss()
        
    def IsPressEnter(self,text=''):   
        search = True       
         # print(f'{type(yoursong)}')        
        self.searchQueue.append(text)
        self.isSearched = True
        #print(text,'this is text')                           
        if self.searchThread is False:
            t3 = threading.Thread(target=self.StartSearchThread,args=(self.searchQueue.pop(0),search,), name='SearchingThread')              
            t3.start()      
            if text == '':
                self.searchQueue =[]
            return                   
        elif self.searchThread is True:
            if self.searchQueue != []:
                self.searchQueue.pop(0)
            self.searchQueue.append(text)               
        
    # Search song in Playlist(ค้นหาเพลงในเพลย์ลิสต์)
    def Searched_Song(self, text="", search=False):
        # print(f'{type(yoursong)}')   
        if text =='' and self.isSearched:
            self.searchQueue.append(text)
            self.isSearched = False
            #print(text,'this is text')                           
            if self.searchThread is False:
                t3 = threading.Thread(target=self.StartSearchThread,args=(self.searchQueue.pop(0),search,), name='SearchingThread')              
                t3.start()      
                if text == '':
                    self.searchQueue =[]
                return                   
            elif self.searchThread is True:
                if self.searchQueue != []:
                    self.searchQueue.pop(0)
                self.searchQueue.append(text)         
            
     
    def StartSearchThread(self,text,search):
        self.searchThread = True
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
        
        self.searchedShow = True   
        if text =='':
            self.searchedShow = False  
            self.showsong(self.playlistlist[self.playlistindex])     
        elif self.searchedShow is True:   
            self.showsong(self.searchedPlaylist)             
        self.searchThread = False
        
    def refresh(self):
        self.reload()
        self.showplaylist(self.playlistlist)
        self.showsong(self.yoursong)
        #print(self.playlistlist)
        #print(self.playlistlist[0])
        self.queue.chooseplaylist(self.yoursong)
        self.ids.playlist_name.text = f'{self.playlistlist[0].name}'

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
        self.menu_playlist=[
                        {
                            "text": self.playlistlist[i].name,
                            "viewclass": "OneLineListItem",
                        }for i in range(len(self.playlistlist))
                    ]
    
    def EnterPlaylistName(self,name):
        f = open("archive/song/playlist.txt", "r+",encoding='utf-8')
        for x in f:
            continue
        f.write("%"+name+"\n")
        f.close()
        self.playlistlist.append(playlist(name))
        self.updateplaylistfile()
        self.showplaylist(self.playlistlist)
        
    # def fixscroll(self,*args):
    #     self.showplaylist(self.playlistlist)
    #     self.showsong(self.playlistlist[self.playlistindex])
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
import os
from kivy.core import text
import win32api
from kivy.lang import Builder
from kivy.utils import platform
from kivy.core.text import LabelBase
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import GridLayout

# Add Font
LabelBase.register(name='sf',fn_regular='archive/finalFontV2.ttf')
# Load .KV file
Builder.load_file('SongBrowser.kv')

class Browser():
    # Variable 
    choosed = None #ไฟล์ที่เลือก
    choosed_drive = "C:\\" #เก็บชื่อไดรฟ์ที่เลือก
    path_file = None #ตำแหน่งไฟล์ที่เลือก

    class SongBrowser(BoxLayout):  
        # ตั้งค่าคลาส
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.ids.lv.path = Browser.choosed_drive
        # ฟังก์ชันเลือกไฟล์
        def selected(self,path,filename):
            Browser.choosed = filename
            Browser.path_file = path
            print(f'Selected File = {Browser.choosed}')
    # คลาสสำหรับเพิ่มเพลง
    class AddSong(MDFloatLayout):   
        def __init__(self, **kwargs):
            super(MDFloatLayout, self).__init__(**kwargs)
            # ตั้งค่าคลาส 
            self.orientation='horizontal'
            self.size_hint=(None,None)
            print(f'all drive = {self.get_win_drives()}')
            # สร้างออบเจกต์สำหรับเลือกไฟล์เพลง
            self.songbrowser = Browser().SongBrowser()
            # กล่องใส่ออบเจกต์เลือกไฟล์เพลง
            self.box = None
            self.drives = MDDialog(                
                    type="custom",
                    title="Choose Drive",
                    buttons = []
                )
            # กล่องแจ้งเตือนสำหรับ Error
            self.warning = MDDialog(                
                    type="custom",
                    title="Please choose .MP3 file",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            font_size = 18,
                            font_name = 'sf',
                            theme_text_color="Custom",
                            text_color = (0,0,0,1),
                            on_release = self.warningConfirm
                        ),
                    ],
                )
        # ฟังก์ชันสำหรับแสดงกล่องเลือกไฟล์เพลง
        def show_songbrowser(self):
            if not self.box:
                self.box = MDDialog(                
                    type="custom",
                    content_cls = Browser().SongBrowser(),
                    buttons=[
                        MDFlatButton(
                            text="Browse from other drives",
                            font_size = 18,
                            font_name = 'sf',
                            theme_text_color="Custom",
                            on_release = self.browse_other
                        ),
                        MDFlatButton(
                            text="OK",
                            font_size = 18,
                            font_name = 'sf',
                            theme_text_color="Custom",
                            on_release = self.clickConfirm
                        ),
                        MDFlatButton(
                            text="CANCEL",
                            font_size = 18,
                            font_name = 'sf',
                            theme_text_color="Custom",              
                            on_release = self.clickCancel                           
                        ),
                    ],
                )
            self.box.open()
        # เลือกไดรฟ์อื่นๆ
        def browse_other(self,instance):
            current_drive = self.get_win_drives()
            list = []
            for i in current_drive:
                butt = MDFlatButton(
                        text=f"{i}",
                        font_size = 24,
                        font_name = 'sf',
                        theme_text_color="Custom",
                        on_release = self.drive_selection_changed
                        )
                list.append(butt)
            self.drives = MDDialog(                
                    type="custom",
                    title="Choose Drive",
                    buttons = list
                )
            self.box.dismiss()
            self.drives.open()
        # ยกเลิกการเลือกไฟล์
        def clickCancel(self,instance):
            self.box.dismiss()
        # ตกลงเลือกไฟล์
        def clickConfirm(self,instance):
            song = Browser.choosed
            # กรณีกดเลือกไฟล์
            if song != None:
                # Check if file is .mp3 or not
                song = song[0]
                check_mp3 = ''
                for i in range(3):
                    check_mp3 = song[-(i+1)] + check_mp3
                print(f'Choosed File type = --{check_mp3}--')
                if check_mp3 == 'mp3':
                    name = os.path.join(Browser.path_file, Browser.choosed[0])[len(Browser.path_file)+1:]
                    #คัดลอกไฟล์เพลงไปยัง archive/song/
                    song = Browser.choosed[0]
                    import shutil
                    original = song
                    target = os.path.join("archive/song/",name)
                    shutil.copyfile(original, target)
                    # เช็คว่ามีเพลงซ้ำมั้ย
                    g = open("archive/song/yoursongpath.txt", "r+",encoding='utf-8')
                    Write = True
                    for i in g:                 
                        if song in i:
                            Write = False
                            break  
                    g.close()  
                    #ถ้าไม่ซ้ำจะทำการเก็บตำแหน่งและบันทึกชื่อเพลง
                    if Write: 
                        f = open("archive/song/yoursongpath.txt", "a",encoding='utf8')  
                        f.write(f'{target}\n')
                        f.close()
                    self.box.dismiss()
                # กรณีไฟล์ที่เลือกไม่ใช่ .mp3
                elif check_mp3 != 'mp3':
                    # self.box.dismiss()
                    self.warning.open()
            # กรณีไม่ได้กดเลือกไฟล์ใดๆ
            else:
                self.warning.open()
        # ยืนยันข้อผิดพลาด
        def warningConfirm(self,instance):
            self.warning.dismiss()
        # ดูจำนวนไดรฟ์ในเครื่อง
        def get_win_drives(self):
            if platform == 'win':
                drives = win32api.GetLogicalDriveStrings()
                drives = drives.split('\000')[:-1]
                return drives
            else:    
                return []
        # ฟังก์ชันสำหรับเลือกไดรฟ์
        def drive_selection_changed(self,instance):
            selected_item = instance.text
            selected_change = selected_item+'\\'
            print(selected_item)
            print(str(selected_change))
            self.drives.dismiss()
            Browser.SongBrowser().ids.lv.path = selected_item
            self.box.open()
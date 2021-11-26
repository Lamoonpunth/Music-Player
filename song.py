from kivy.core.audio import SoundLoader
class song():
    def __init__(self,path):
        self.path=path
        temp=path[13:]
        self.name=temp[:-4]
        sound=SoundLoader.load(self.path)
        self.time=sound.length
    def getpath(self):
        return self.path
    def getname(self):
        return self.name
    def gettime(self):
        return self.time
    def __str__(self):
        return str(self.getpath())+"\t"+str(self.getname())+"\t"+str(self.gettime())
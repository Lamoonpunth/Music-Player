import playlist
class playingqueue(list):
    def __init__(self):
        self.originalplaylist=[]
        self.musicqueue=[]
        self.nowplaying=""
        self.nowplayingindex=0
        self.playedstack=[]
        self.random=False
        self.Loop=False
    def clearqueue(self):
        self.musicqueue=[]
    def dequeue(self):
        if self.isEmpty():
            return ""
        temp=self.musicqueue[0]
        self.musicqueue.pop(0)
        return temp
    def enqueue(self,song):
        self.musicqueue.append(song)
    def addfromqueuefirstsong(self):
        self.nowplayingindex=self.musicqueue[0].indexinplaylist
        self.nowplaying=self.dequeue()
    def addfromqueue(self):
        self.playedstack.append(self.nowplaying)
        print(self.musicqueue)
        self.nowplayingindex=self.musicqueue[0].indexinplaylist
        self.nowplaying=self.dequeue()
    def addfromstack(self):
        self.musicqueue.insert(0,self.nowplaying)
        self.nowplayingindex=self.playedstack[-1].indexinplaylist
        self.nowplaying=self.playedstack.pop()
    def copyOriginal(self):
        self.musicqueue=self.originalplaylist.copy()
        self.nowplaying=""
        self.playedstack=[]
    def isStackEmpty(self):
        return len(self.playedstack)==0
    def chooseplaylist(self,playlist):
        self.musicqueue=playlist.playlist.copy()
        self.originalplaylist=playlist
        self.nowplaying=""
        self.playedstack=[]
    def isEmpty(self):
        return len(self.musicqueue)==0
    def __str__(self):
        str=""
        for i in self.musicqueue:
            str += i +"\n"
        return str
    
q=playingqueue()
q.enqueue("1")
print(q)
import playlist
class playingqueue(list):
    def __init__(self):
        self.musicqueue=[]
        self.nowplaying=""
    def dequeue(self):
        temp=self.musicqueue[0]
        self.musicqueue.pop()
        return temp
    def enqueue(self,path):
        self.musicqueue.append(path)
    def addfromqueue(self):
        self.nowplaying=self.dequeue()
    def chooseplaylist(self,playlist):
        self.musicqueue=playlist.playlist.copy()
    def __str__(self):
        str=""
        for i in self.musicqueue:
            str += i+"\n"
        return str
q=playingqueue()
q.enqueue("1")
print(q)
class playlist(list):
    def __init__(self,name,playlist=[]):
        self.playlist=playlist
        self.name=name
    def addsong(self,song):
        self.playlist.append(song)
    def clearSong(self):
        self.playlist = []
    def removesong(self,index):
        self.playlist.pop(index)
    def __str__(self):
        str = ""
        for i in self.playlist:
            str+= i.getname() +"\n"
        return str
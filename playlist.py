class playlist(list):
    def __init__(self,name,playlist=[]):
        self.playlist=playlist
        self.name=name
    def addsong(self,path):
        self.playlist.append(path)
    def clearSong(self):
        self.playlist = []
    def __str__(self):
        str = ""
        for i in self.playlist:
            str+= i.getname() +"\n"
        return str
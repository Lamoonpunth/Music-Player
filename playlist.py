class playlist(list):
    def __init__(self,playlist=[]):
        self.playlist=playlist
    def addsong(self,path):
        self.playlist.append(path)
    def __str__(self):
        str = ""
        for i in self.playlist:
            str+= i.getname() +"\n"
        return str
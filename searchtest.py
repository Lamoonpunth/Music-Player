class pair():
    def __init__(self,name,sim):
        self.name=name
        self.sim=sim
    def __str__(self):
        return str(self.name)+"\t"+str(self.sim)+"\n"
def sim(pair):
    return pair.sim
import nltk
alphabet="abcdefghijklmnopqrstuvwxyz"
searchword="az"
songlist=[]
for i in alphabet:
    for j in alphabet:
        songlist.append(i+j)
newlist=[]
for i in songlist:
    newlist.append(pair(i,nltk.edit_distance(searchword, i)))
print(*newlist)
newlist.sort(key=sim)
print(*newlist)
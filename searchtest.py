import nltk
class pair():
    def __init__(self,name,sim):
        self.name=name
        self.sim=sim
    def __str__(self):
        return str(self.name)+"\t"+str(self.sim)+"\n"
def sim(pair):
    return pair.sim

alphabet    =   "abcdefghijklmnopqrstuvwxyz"
searchword  = "az"
songlist=[]
sslist=[]
for i in alphabet:
    for j in alphabet:
        sslist.append(i+j)
        for k in alphabet:            
                songlist.append(i+j+k)
newlist=[]

# for i in songlist:
#     if nltk.edit_distance(searchword, i) ==1:
#         newlist.append(pair(i,nltk.edit_distance(searchword, i)))
# for i in sslist:
#     if nltk.edit_distance(searchword, i) ==1:     
#         newlist.append(pair(i,nltk.edit_distance(searchword, i)))        
# print(*newlist)
# newlist.sort(key=sim)
# print(*newlist)

newlist.append(pair(i,nltk.edit_distance('za', 'asdfjkl'))) 
newlist.append(pair(i,nltk.edit_distance('searchword', 'i')))   
print(*newlist)
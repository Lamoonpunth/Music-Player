print(f'{type(yoursong)}')             
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
        # print('------------')               
        self.showsong(self.searchedPlaylist)
        self.searchedShow = search
        if text =='':
            self.searchedShow = False
            return
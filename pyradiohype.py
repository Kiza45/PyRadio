# AUTO RADIO PLAYER SCRIPT WRITTEN BY MASON JOHNSON-COOPER 



from ast import While
from asyncore import loop
import requests
import vlc
from time import sleep
from datetime import datetime
now = datetime.now()

#below is a list of URL/m3u/plsd files to play
urls = [
    #'file:///radio1xtra.pls',
    'file:///C:/PyRadio/radio1.pls',
    'file:///C:/PyRadio/virgin.m3u',
   # 'file:///C:/PyRadio/magic.pls',
    #'file:///C:/PyRadio/jassfm.pls',
    'file:///C:/PyRadio/captialfm.m3u',
    'file:///C:/PyRadio/capitalxtra.m3u',
    
    

]
    

playlists = set(['pls','m3u'])

while True:

    Instance = vlc.Instance()
   

    for url in urls:
        
        player = Instance.media_player_new()
        Media = Instance.media_new(url)
        Media_list = Instance.media_list_new([url])
        Media.get_mrl()
        player.set_media(Media)
         
        list_player = Instance.media_list_player_new()
        list_player.set_media_list(Media_list)
        player.audio_set_volume(100)
        if list_player.play() == -1:
            print ("Error playing")
        else:
            s2 = "Playing Radio"
            print(s2)  
    
    
    #sleep(10)
    #player.audio_set_volume(50)
    #sleep(10)
    #player.audio_set_volume(100)
        sleep(1800)
        list_player.stop()
    

    


       
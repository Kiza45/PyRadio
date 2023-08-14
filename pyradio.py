import vlc
import time
import schedule
from itertools import cycle
import datetime as d


# below is a list of URL/m3u/plsd files to play
urls = [

    # 'file:///C:/PyRadio/heartxmas.m3u',
    'file:///C:/PyRadio/radio1.pls',
    'file:///C:/PyRadio/virgin.m3u',
    'file:///C:/PyRadio/jassfm.pls',
    'file:///C:/PyRadio/kerrang.pls',
    'file:///C:/PyRadio/captialfm.m3u',
    'file:///C:/PyRadio/capitalxtra.m3u',
    # 'file:///C:/PyRadio/magic.pls',
    

]
    
# days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
# playlists = set(['pls','m3u'])


def radio_player():
    print(d.datetime.now().hour)
    print(d.datetime.now().minute)
    today = d.date.today()
    #if today.weekday() < 5 & today.weekday() >= 0:
        # setting how long to run the radio for
        # day_start = time.time()
        # day_end = day_start + 8.5*3600
        # while time.time() <= day_end:
    #if d.datetime.now().hour >= 9:
    #TODO Fix the minute check for while loop
    while d.datetime.now().hour < 18:
        #& d.datetime.now().minute < 30
        print("test2")
        #instance = vlc.Instance()
        for url in cycle(urls):
            print(url)
            skip_station = False
            start = time.time()
            change = start + 3

            print("station switched")
            while time.time() <= change:
                player = vlc.MediaPlayer()
                Media = vlc.Media(url)
                #Media_list = vlc.media_list_new([url])
                Media.get_mrl()
                player.set_media(Media)

                #list_player = instance.media_list_player_new()
                #list_player.set_media_list(Media_list)
                player.audio_set_volume(100)
                if player.play() == -1:
                    print("Error playing")




   # else:
    print("radio stopped")


def skip():
    skip_station = True




radio_player()
#schedule.every().at("09:00").do(radio_player())


#while True:
    # Checks whether a scheduled task
    # is pending to run or not
 #   schedule.run_pending()
  #  time.sleep(1)

    

    


       

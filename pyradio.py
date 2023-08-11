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
    
days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
# playlists = set(['pls','m3u'])


def radio_player():
    today = d.date.today()
    if today.weekday() < 5 & today.weekday() >= 0:
        # setting how long to run the radio for
        day_start = time.time()
        day_end = day_start + 8.5*3600
        while time.time() <= day_end:
            while True:
                instance = vlc.Instance()

                # cycle through the list of urls
                # repeatedly until 17:30
                for url in cycle(urls):
                    start = time.time()
                    change = start + 30 * 60
                    while start <= change:
                        player = instance.media_player_new()
                        media = instance.media_new(url)
                        media_list = instance.media_list_new([url])
                        media.get_mrl()
                        player.set_media(media)

                        list_player = instance.media_list_player_new()
                        list_player.set_media_list(media_list)
                        player.audio_set_volume(100)
                        if list_player.play() == -1:
                            print("Error playing")
                        else:
                            s2 = "Playing Radio"
                            print(s2)


schedule.every().at("09:00").do(radio_player())
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)

    

    


       

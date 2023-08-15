import vlc
import time
import subprocess
from itertools import cycle
import datetime as d


# below is a list of URL/m3u/plsd files to play
urls = [

    # 'file:///C:/PyRadio/heartxmas.m3u',
    'C:/PyRadio/radio1.pls',
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
    vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
    print(d.datetime.now().hour)
    print(d.datetime.now().minute)


    # setting how long to run the radio for
    day_start = time.time()
    day_end = day_start + 8.5*3600
    while time.time() <= day_end:
        while True:
            instance = vlc.Instance()

            for url in cycle(urls):
                print("station switched")
                start = time.time()
                change = start + 20
                while start <= change:
                    subprocess.Popen([vlc_path, url])
                    time.sleep(19)

radio_player()
#schedule.every().at("09:00").do(radio_player())


#while True:
    # Checks whether a scheduled task
    # is pending to run or not
 #   schedule.run_pending()
  #  time.sleep(1)

    

    


       

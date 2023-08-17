import time
import subprocess
import datetime as d


# below is a list of URL/m3u/pls files to play
urls = [
    'C:/PyRadio/radio_stations/jassfm.pls',
    # 'C:/PyRadio/heartxmas.m3u',
    "C:/PyRadio/radio_stations/capitalxtra.m3u",
    'C:/PyRadio/radio_stations/virgin.m3u',
    'C:/PyRadio/radio_stations/kerrang.pls',
    'C:/PyRadio/radio_stations/bbc_radio_one.m3u8',
    'C:/PyRadio/radio_stations/captialfm.m3u'


    # 'file:///C:/PyRadio/magic.pls',
    

]
    
# days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
# playlists = set(['pls','m3u'])


def radio_player():
    current_index = 0
    vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
    print(d.datetime.now().hour)
    print(d.datetime.now().minute)
    run_time = 10

    while True:
        playlist_url = urls[current_index]
        with open(playlist_url, "r") as radio_file:
            radio_content = radio_file.read()

        if "m3u" in playlist_url:

            radio_lines = radio_content.splitlines()
            radio_entries = [line for line in radio_lines if line and not line.startswith("#")]

            # stream_url = None
            # for line in radio_content.splitlines():
            #    if line.startswith("File1="):
            #      stream_url = line[len("File1="):]
            #      print(stream_url)
            #     break

            if radio_entries:
                start_time = time.time()
                stream_url = radio_entries[0]
                print(stream_url)
                while time.time() - start_time < run_time:
                    user_input = input("Type 's' to skip stations: ")
                    vlc_process = subprocess.Popen([vlc_path, "--playlist-autostart", stream_url])
                    # time.sleep(15)   Sleep for 30 minutes (1800 seconds)
                    if user_input.lower() == 'skip':
                        vlc_process.terminate()
                        print("Skipping stations.")
                        break

                vlc_process.terminate()  # Terminate the current VLC instance

                if current_index == (len(urls)-1):
                    current_index = 0
                else:
                    current_index = (current_index + 1)

        if "pls" in playlist_url:
            stream_url = None
            for line in radio_content.splitlines():
                if line.startswith("File1="):
                    stream_url = line[len("File1="):]
                    print(stream_url)
                    break

            if stream_url:
                start_time = time.time()
                while time.time() - start_time < run_time:
                    user_input = input("Type 's' to skip stations: ")
                    vlc_process = subprocess.Popen([vlc_path, "--playlist-autostart", stream_url])
                    # time.sleep(15)   Sleep for 30 minutes (1800 seconds)
                    if user_input.lower() == 'skip':
                        vlc_process.terminate()
                        print("Skipping stations.")
                        break
                vlc_process.terminate()  # Terminate the current VLC instance

                if current_index == (len(urls) - 1):
                    current_index = 0
                else:
                    current_index = (current_index + 1)


radio_player()

    

    


       

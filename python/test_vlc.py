import vlc
import time
song_list=['/home/pmoracho/Descargas/SampleAudio_0.4mb.mp3']
instance=vlc.Instance()
for song in song_list:
    player=instance.media_player_new()
    media=instance.media_new(song)
    print(song)
    media.get_mrl()
    player.set_media(media)
    player.play()
    playing = set([1,2,3,4])
    time.sleep(1) #Give time to get going
    while True:
        duration = player.get_length() / 1000
        mm, ss = divmod(duration, 60)
        print("Playing %s Length: %02d:%02d %02d%%" % (song,mm,ss,player.get_position()))
        time.sleep(1) 
        state = player.get_state()
        if state not in playing:
            break
        continue


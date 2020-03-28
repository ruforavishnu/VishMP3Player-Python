from mutagen.mp3 import MP3

audio = MP3("bumbro.mp3")
print("audio length:"+str(audio.info.length))
print("audio bitrate:"+str(audio.info.bitrate))

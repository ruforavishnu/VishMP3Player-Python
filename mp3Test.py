from  pygame import mixer

file = 'bumbro.mp3'
mixer.init()
mixer.music.load(file)
print("loaded file:"+file)
mixer.music.play()

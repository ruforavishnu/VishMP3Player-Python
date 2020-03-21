from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_wav('bumbro.mp3')
play(sound)
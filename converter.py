from os import path
from pydub import AudioSegment

src = "rj2.mp3"
dst = "play.wav"

sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
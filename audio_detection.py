import numpy as np
import sounddevice as sd

samplerate = 44100
duration = 1  # seconds

def detect_audio():
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()

    volume = np.linalg.norm(audio) * 10

    if volume > 40:
        return True
    return False

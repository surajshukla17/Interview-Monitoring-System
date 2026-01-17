import sounddevice as sd
import numpy as np

DURATION = 2
SAMPLE_RATE = 44100

def detect_audio():
    print("Listening... (Press Ctrl+C to stop)")
    try:
        while True:
            audio = sd.rec(
                int(DURATION * SAMPLE_RATE),
                samplerate=SAMPLE_RATE,
                channels=1,
                dtype='float64'
            )
            sd.wait()

            audio_data = audio.flatten()
            energy = np.sum(audio_data ** 2)

            if energy > 50:
                print("ALERT: Multiple / Loud Voices Detected ❌")
            else:
                print("Audio Normal ✅")

    except KeyboardInterrupt:
        print("\nAudio Detection Stopped Safely")

if __name__ == "__main__":
    detect_audio()

import cv2
import sounddevice as sd
import numpy as np
import threading

# -------- FACE SETUP --------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
cap = cv2.VideoCapture(0)

# -------- AUDIO SETUP --------
DURATION = 2
SAMPLE_RATE = 44100
audio_alert = False
running = True   # 🔥 IMPORTANT FLAG

def audio_detection():
    global audio_alert, running
    while running:
        try:
            audio = sd.rec(
                int(DURATION * SAMPLE_RATE),
                samplerate=SAMPLE_RATE,
                channels=1,
                dtype='float64'
            )
            sd.wait()

            audio_data = audio.flatten()
            energy = np.sum(audio_data ** 2)

            audio_alert = energy > 50

        except:
            break

# -------- START AUDIO THREAD --------
audio_thread = threading.Thread(target=audio_detection)
audio_thread.start()

# -------- MAIN LOOP --------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if len(faces) > 1:
        cv2.putText(
            frame,
            "ALERT: Multiple Faces Detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

    if audio_alert:
        cv2.putText(
            frame,
            "ALERT: Multiple Voices Detected",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

    cv2.imshow("Interview Monitoring System", frame)

    # 🔴 SAFE EXIT
    if cv2.waitKey(1) & 0xFF == ord('q'):
        running = False
        break

# -------- CLEAN EXIT --------
cap.release()
cv2.destroyAllWindows()
audio_thread.join()
print("Program Closed Safely ✅")

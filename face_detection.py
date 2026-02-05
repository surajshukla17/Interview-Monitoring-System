import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

prev_center = None
movement_threshold = 25

def process_faces(frame):
    global prev_center

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    movement = False

    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        center = (x + w//2, y + h//2)

        if prev_center is not None:
            dist = np.linalg.norm(np.array(center) - np.array(prev_center))
            if dist > movement_threshold:
                movement = True

        prev_center = center

        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.circle(frame, center, 5, (0,0,255), -1)

    return len(faces), movement

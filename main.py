import cv2
import time
from face_detection import process_faces
from audio_detection import detect_audio
from report import print_report

start_time = time.time()

multi_face_count = 0
multi_voice_count = 0
movement_count = 0

cap = cv2.VideoCapture(0)

print("\n🎤 Interview Monitoring System Started...\n")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    face_count, movement = process_faces(frame)

    if face_count > 1:
        multi_face_count += 1

    if movement:
        movement_count += 1

    audio_alert = detect_audio()
    if audio_alert:
        multi_voice_count += 1

    elapsed = int(time.time() - start_time)

    print(f"Time: {elapsed}s | Faces: {face_count} | Audio Alert: {audio_alert} | Movement: {movement}")

    cv2.putText(frame, f"Faces: {face_count}", (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(frame, f"Movement: {movement}", (10,70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

    cv2.imshow("Interview Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

total_time = int(time.time() - start_time)

print_report(total_time, multi_face_count, multi_voice_count, movement_count)

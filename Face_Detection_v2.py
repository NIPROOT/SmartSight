import cv2
from deepface import DeepFace
import pyttsx3
import threading
import datetime


eng = pyttsx3.init()
eng.setProperty('rate', 170)

cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('face_analysis_output.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (frame_width, frame_height))

def speak(text):
    threading.Thread(target=lambda: (eng.say(text), eng.runAndWait())).start()

def apply_filter(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    return cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = apply_filter(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    detected_faces = faces.detectMultiScale(gray, 1.3, 5)

    try:
        results = DeepFace.analyze(frame, actions=['emotion', 'age', 'gender', 'race'], detector_backend='opencv', enforce_detection=False)

        for i, face in enumerate(results):
            x, y, w, h = detected_faces[i] if i < len(detected_faces) else (50, 50, 100, 100)

            emotion = face['dominant_emotion']
            age = face['age']
            gender = face['dominant_gender']
            race = face['dominant_race']

            color = (0, 255, 0) if emotion == 'happy' else (0, 0, 255)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

            cv2.rectangle(frame, (x, y - 40), (x + w, y), color, -1)
            cv2.putText(frame, f"{emotion} | Age: {age} | Gender: {gender} ", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            with open("face_data_log.txt", "a") as file:
                file.write(f"{datetime.datetime.now()} - Emotion: {emotion}, Age: {age}, Gender: {gender}, Race: {race}\n")

            if emotion in ["angry", "sad"]:
                speak(f"Alert: The person looks {emotion}!")

            speak(f"Detected: Emotion {emotion}, Age {age}, Gender {gender}")

    except Exception as e:
        print(f"Error: {e}")

    cv2.imshow('Advanced Face Analysis', frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
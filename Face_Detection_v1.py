from deepface import DeepFace
import cv2
import pyttsx3

eng=pyttsx3.init()

# Start the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Perform face detection and emotion detection with DeepFace
    # You can analyze emotions on the image as well
    try:
        result = DeepFace.analyze(frame, actions=['emotion','age', 'gender', 'race'])

        # Get the emotion prediction
        emotion = result[0]['dominant_emotion']
        age = result[0]['age']
        gender = result[0]['gender']
        race = result[0]['dominant_race']

        eng.say(f"Emotion is {emotion} Age is {age} gender is {gender} race is {race}")
        eng.runAndWait()

        emotion_color = (0,255,0) if emotion == 'happy' else (0,0,255)
        cv2.rectangle(frame, (10,10), (400,100), emotion_color, -1)

        # Draw the emotion on the frame
       
        cv2.putText(frame, f"Emotion: ", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, f"Age: {age}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, f"Gender: {max(gender, key=gender.get)}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame,f"race: {race}", (10,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),2)

    except Exception as e:
        print(f"Error: {e}")

    # Show the image with detected emotion
    cv2.imshow('Emotion Detection', frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
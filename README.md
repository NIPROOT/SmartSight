
# Real-Time Face, Emotion, Age, Gender, and Race Detection

This project demonstrates the use of **DeepFace** for real-time face and emotion detection along with age, gender, and race classification from a live webcam feed. Additionally, the project integrates **pyttsx3** for speech synthesis to announce the detected attributes. The project is available in two versions:

- **Version 1**: Basic face and emotion detection with speech output.
- **Version 2**: Advanced face analysis with additional features like video filtering, real-time logging, and speech alerts for specific emotions.

---

## Features

### Version 1
- **Real-time Face Detection**: Detects face, emotion, age, gender, and race.
- **Speech Output**: Announces the detected attributes such as emotion, age, gender, and race.
- **Emotion Color Coding**: Green rectangle for happy emotion and red for other emotions.
- **Overlay Text**: Displays emotion, age, gender, and race information on the video feed.

### Version 2
- **Grayscale and Gaussian Blur Filter**: Applies a grayscale filter and Gaussian blur effect on the video feed for added visual effects.
- **Real-time Logging**: Logs detected face attributes into a text file (`face_data_log.txt`) with timestamps.
- **Speech Alerts**: If the emotion detected is "angry" or "sad", the system provides an alert.
- **Video Output**: Captured video is saved as an `.avi` file (`face_analysis_output.avi`).
- **Advanced Face Detection**: Uses **OpenCV** for detecting faces and **DeepFace** for analyzing emotions, age, gender, and race.

---

## Requirements

- Python 3.x
- **DeepFace**: To analyze facial features and emotions.
- **OpenCV**: For video capture and processing.
- **pyttsx3**: For text-to-speech functionality.
- **threading**: For running speech synthesis in parallel with video processing.

To install the necessary dependencies, run:

```bash
pip install deepface opencv-python pyttsx3 or pip install -r req.txt
```

---

## Usage

### Version 1:
1. Run the Python script.
2. The webcam will open, and the system will begin detecting the face, emotion, age, gender, and race.
3. Detected attributes will be announced through the speakers and displayed on the video feed.
4. Press `q` to quit the webcam feed.

### Version 2:
1. Run the Python script.
2. The system will process the webcam feed, apply visual effects (grayscale and blur), and analyze faces for emotions, age, gender, and race.
3. Detected data will be logged into `face_data_log.txt` with timestamps.
4. If "angry" or "sad" emotion is detected, an alert will be spoken.
5. Captured video will be saved as `face_analysis_output.avi`.
6. Press `q` to quit the webcam feed.

---

## How it Works

### Version 1
1. **Face Detection**: The `DeepFace.analyze()` function detects the face in real-time from the webcam feed.
2. **Emotion, Age, Gender, and Race Detection**: DeepFace analyzes the detected face for various attributes like emotion, age, gender, and race.
3. **Speech Feedback**: **pyttsx3** converts the text information into speech and announces it to the user.
4. **Overlay Text**: The detected attributes (emotion, age, gender, race) are displayed on the video frame using **OpenCV**.

### Version 2
1. **Grayscale and Gaussian Blur**: The frame is converted to grayscale and a blur effect is applied for aesthetic purposes.
2. **Face Detection**: The **OpenCV Haar Cascade** is used to detect faces in the video feed.
3. **DeepFace Analysis**: After detecting faces, **DeepFace** is used to analyze the emotion, age, gender, and race.
4. **Logging**: The detected data is logged with a timestamp into a text file (`face_data_log.txt`).
5. **Speech Alerts**: If specific emotions (angry/sad) are detected, an alert is spoken through **pyttsx3**.
6. **Video Output**: The processed video is saved to a file (`face_analysis_output.avi`).

---

## Sample Output

- **Text on Screen**: The detected emotion, age, gender, and race are displayed on the screen.
- **Speech Output**: The system announces the detected information. Example: 
  - *"Emotion: Happy. Age: 25. Gender: Male. Race: Caucasian."*
  - If the person appears angry or sad: *"Alert: The person looks angry!"*
  
---

## Troubleshooting

- **Webcam not working**: Make sure your webcam is properly connected and recognized by OpenCV.
- **Module Not Found**: Ensure you have installed the necessary Python modules using `pip install`.
- **DeepFace errors**: DeepFace uses pre-trained models which may occasionally throw errors if the models are not properly loaded.


---

## Contributions

Feel free to fork the repository and submit pull requests to improve the functionality or add new features. If you have any suggestions or issues, please create an issue on the GitHub repository.

---

## Acknowledgments

- **DeepFace**: For providing advanced facial analysis using deep learning.
- **OpenCV**: For real-time computer vision and video processing.
- **pyttsx3**: For text-to-speech functionality.


import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the pre-trained face mask detection model
model = load_model('mask_detection_model.h5')

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Function to detect and classify faces in real-time
def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))

    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        resized_roi = cv2.resize(face_roi, (100, 100))
        normalized_roi = resized_roi / 255.0
        reshaped_roi = np.reshape(normalized_roi, (1, 100, 100, 1))
        result = model.predict(reshaped_roi)

        label = "Mask" if result[0][0] > 0.5 else "No Mask"
        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
        
        cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
        cv2.putText(frame,label,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,color)

    return frame

# Open the webcam or video file
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = detect_faces(frame)

    # Display the output frame
    cv2.imshow('Face Mask Detection', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
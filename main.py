import pickle
import numpy as np
import cv2
import mediapipe as mp
from fastapi import FastAPI, File, UploadFile
from collections import Counter

app = FastAPI()


model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)


labels_dict = {0: 'A', 1: 'B', 2: 'L'}


max_len = model.n_features_in_ // 2

# Define a function to process a single frame and predict the hand sign
def process_frame(frame: np.ndarray) -> str:
    data_aux = []
    x_ = []
    y_ = []

    H, W, _ = frame.shape

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

        # Pad the data_aux array to match the expected input length
        if len(data_aux) < max_len * 2:
            data_aux.extend([0] * (max_len * 2 - len(data_aux)))

        # Make predictions using the trained model
        prediction = model.predict([np.asarray(data_aux)])

        predicted_character = labels_dict[int(prediction[0])]
        return predicted_character
    return "No hand detected"

# Define a POST request endpoint for video file upload
@app.post("/predict")
async def predict_video(file: UploadFile = File(...)):
    # Save the uploaded video file
    temp_file_path = f"./temp_video/{file.filename}"
    with open(temp_file_path, "wb") as f:
        contents = await file.read()
        f.write(contents)

    # Process the video file
    cap = cv2.VideoCapture(temp_file_path)
    if not cap.isOpened():
        return {"error": "Could not open video file"}

    predictions = []
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret or frame_count >= 60:
            break
        predicted_character = process_frame(frame)
        if predicted_character != "No hand detected":
            predictions.append(predicted_character)
        frame_count += 1
    cap.release()
    
    # Optionally, delete the temporary video file
    import os
    os.remove(temp_file_path)

    # Determine the most frequent prediction
    if predictions:
        most_common = Counter(predictions).most_common(1)
        final_prediction = most_common[0][0]
    else:
        final_prediction = "No hand detected"

    return {"prediction": final_prediction}

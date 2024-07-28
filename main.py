from ultralytics import YOLO
import cv2
import math
import time
import numpy as np


cap = cv2.VideoCapture(0)
model = YOLO('id_card_v5.pt')


classnames = ['Id Card']

confidence_threshold = 0.6  


focal = 450
pixels = 30
width = 4


def calculate_distance(pixels):
    return (width * focal) / pixels

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    result = model(frame, stream=True)

    
    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = box.conf[0]
            confidence = math.ceil(confidence * 100)
            Class = int(box.cls[0])
            if confidence > confidence_threshold * 100:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
                if Class < len(classnames):  
                    class_name = classnames[Class]

                    
                    pixels_covered = x2 - x1
                    distance = calculate_distance(pixels_covered)

                    label = f'{class_name} {confidence}%'
                    (label_width, label_height), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
                    cv2.rectangle(frame, (x1, y1), (x1 + label_width, y1 - label_height - 10), (0, 0, 255), -1)
                    cv2.putText(frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                    distance_label = f'Distance: {round(distance, 2)} cm'
                    cv2.putText(frame, distance_label, (x1, y2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow('frame', frame)
    cv2.waitKey(1)
cv2.destroyAllWindows()


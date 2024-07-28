# YOLO Object Detection for ID Card
![face_capturing](https://github.com/user-attachments/assets/53d8452a-93cf-454e-913e-ed8d86301ff3)
![with_id_card](https://github.com/user-attachments/assets/3ca65788-4df6-4071-ae1b-71b34df620fc)

Overview
This project demonstrates an application of YOLO (You Only Look Once) for real-time object detection and distance measurement of ID cards using a webcam. The application utilizes a pre-trained YOLO model to detect ID cards, draw bounding boxes around detected objects, and calculate the distance from the camera based on the size of the detected object.

Features
Real-Time Object Detection: Uses the YOLO model to detect ID cards in real-time from a webcam feed.
Bounding Boxes: Draws bounding boxes around detected ID cards with confidence scores.
Distance Calculation: Computes the approximate distance of the ID card from the camera based on the size of the detected object.
Dynamic Labels: Displays confidence percentage and distance information on the video feed.
Customizable Thresholds: Allows adjustment of confidence thresholds for detection accuracy.
Technologies Used
Python: Programming language used for scripting.
Ultralytics YOLO: YOLO model for object detection.
OpenCV: Library for image processing and video capture.
NumPy: Library for numerical operations.
Getting Started
To get started with this project, follow these steps:

Clone the Repository:

bash
Copy code
git clone [https://github.com/yourusername/your-repository.git](https://github.com/pradeeshkumareu/Object-detection--ID-Card.git)
Install Dependencies:
Ensure you have the required libraries installed. You can install them using pip:

bash
Copy code
pip install ultralytics opencv-python numpy
Download YOLO Model:

Download the pre-trained YOLO model (id_card_v5.pt) from the provided source or train your own model and place it in the project directory.
Run the Script:

Execute the script using Python:
bash
Copy code
python your_script_name.py
View Results:

The webcam feed will open in a window displaying detected ID cards, bounding boxes, confidence scores, and calculated distances.
Configuration
Confidence Threshold: Adjust the confidence_threshold variable in the script to filter detections based on confidence level.
Camera Calibration: Modify focal, pixels, and width variables if needed to calibrate distance calculations based on your camera setup.
How It Works
Video Capture: Captures video frames from the webcam.
Object Detection: Processes each frame with the YOLO model to detect ID cards.
Bounding Boxes: Draws bounding boxes around detected objects with confidence scores.
Distance Calculation: Calculates the distance of the detected object from the camera using the width of the bounding box.
Display Information: Overlays labels and distance information on the video feed.
Usage
Detect ID Cards: Point your webcam towards an ID card to detect and measure its distance.
Adjust Parameters: Modify the script to adjust detection thresholds and calibration settings according to your needs.
Contributing
Feel free to contribute by forking the repository and making improvements. Open issues or submit pull requests for any bugs or feature requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For questions or support, please contact: pradeeshkumareu@gmail.com

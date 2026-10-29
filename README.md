# Weapon Detection System

A Python computer vision project that explores gun detection from a live webcam feed using OpenCV and a Haar cascade classifier.

## Features

- Captures video from the computer's webcam.
- Processes video frames using OpenCV.
- Converts frames to grayscale for detection.
- Uses a cascade classifier to identify potential gun-like objects.
- Draws bounding boxes around detected regions.
- Prints detection status in the terminal.

## Technologies Used

- Python 3
- OpenCV
- NumPy
- imutils
- Haar Cascade Classifier

## Requirements

Install the required libraries:

```bash
pip install opencv-python numpy imutils
```

You also need a working webcam and the `cascade.xml` classifier file supplied with this project.

## Project Structure

```text
Weapon-Detection-System/
├── gun_detection.py
├── cascade.xml
├── README.md
└── .gitignore
```

## How to Run

1. Clone or download this repository.
2. Install the required Python packages.
3. Ensure `cascade.xml` is in the same directory as the Python script.
4. Connect or enable your webcam.
5. Run the application:

```bash
python gun_detection.py
```

Press `q` to quit the video feed when the display loop is active.

## Important Limitations

This project uses a cascade classifier and should be treated as an educational demonstration. Its detections may be inaccurate, and it should not be relied upon as a real-world security or threat-detection system.

## Learning Outcomes

- Basic computer vision with OpenCV.
- Webcam video capture and frame processing.
- Grayscale image conversion.
- Cascade classifier usage.
- Bounding-box drawing and detection output.

## Author

Aditi Vaidya

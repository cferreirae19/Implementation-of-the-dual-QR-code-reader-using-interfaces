# Implementation-of-the-dual-QR-code-reader-using-interfaces
It consists of five separate scripts:

- interface.py: This is the interface implemented by both readers.
- main.py: Main script of the project.
- qr_code_detector_v1.py: This is the QReader detector.
- qr_code_detector_v2.py: This is the OpenCV detector.
- readingQR_cv2.py: Custom Python module needed for the OpenCV reader.

## Behavior

The code starts a video capture (webcam) and, for every frame, calls the detect_and_decode function, searching for any QR code that could be on scene. When a code is detected, the program reads it to extract its data and draws a bounding box around it. To make comparisons easier, the FPS count is displayed in the upper left corner of the window; Below it, when a QR code is detected, its size (in pixels) is also displayed.

## Usage

In this case, the user only has to specify (at the main.py script) which detector he/she wants to use, by commenting/uncommenting lines 7/8.

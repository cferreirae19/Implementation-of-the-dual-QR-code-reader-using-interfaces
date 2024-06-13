# Implementation-of-the-dual-QR-code-reader-using-interfaces
It consists of six separate scripts:

- interface.py: This is the interface implemented by both readers.
- main.py: Main script of the project.
- qr_code_detector_v1.py: This is the QReader detector.
- qr_code_detector_v2.py: This is the OpenCV detector.
- readingQR_cv2.py: Custom Python module needed for the OpenCV reader.
- main_single_load.py: Usually, this script never takes part pn the code execution; it was created for convenience purposes, to execute the detection on a single image at a time.

## Behavior

The main.py script processes twice all the images contained in the folder specified by the route at line 77, one for each detector. While doing this, it keeps track of the execution time it takes for each detector to fully process each image, and the size of any QR code that appears to be in the image. This results are stored on the qr_code_detection_results.txt file. The advantage of this code is that is infinitelly scalable in terms of images, which means that the user can execute it the same way all the time regardless of the number of pictures.

## Usage

As mentioned previously, the only thing the user has to do is specify at line 77 (in the main.py script) the folder he/she wants to read the images from, save it and then run it.

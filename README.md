# Implementation-of-the-dual-QR-code-reader-using-interfaces
It consists of five separate files:

- interface.py: This is the interface implemented by both readers.
- main.py: Main script of the project; here we can choose between both readers, by commenting/uncommenting lines 6/7
- qr_code_detector_v1.py: This is the QReader detector.
- qr_code_detector_v2.py: This is the OpenCV detector.
- readingQR_cv2.py: Custom Python module needed for the OpenCV reader.

## Installation

- OpenCV 
    
    ```
    pip install opencv-python
    ```

- pyzbar

    ```
    pip install pyzbar
    ```

- Dynamsoft Barcode Reader

    ```
    pip install dbr
    ```

- QReader

    ```
    pip install qreader
    ```

## Usage

As mentioned previously, the only thing the user has to do is select the reader he/she wants to use by commenting/uncommenting its corresponding code line (specifically, lines 6 and/or 7 from the main.py script), save it and then run the main script.

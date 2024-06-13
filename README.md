# Implementation-of-the-dual-QR-code-reader-using-interfaces
It consists of two separate folders:

- VideoCapture: it contains the executable code to launch the webcam and start detecting QR codes.
- FilesReadFromDisk: it contains the executable code to test the dual detector by reading images from memory, evaluating its performance in terms of area (in pixels) and execution time and saving the results on a txt file.

More detailed instructions about both modes/folders are included in their own readme files.

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

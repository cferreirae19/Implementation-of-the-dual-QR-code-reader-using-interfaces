# Implementation-of-the-dual-QR-code-reader-using-interfaces
It consists of two separate folders:

- VideoCapture: it contains the executable code to launch the webcam and start detecting QR codes.
- FilesReadFromDisk: it contains the executable code to test the dual detector by reading images from memory, evaluating its performance in terms of area (in pixels) and execution time and saving the results on a txt file.

More detailed instructions about both modes/folders are included in their own readme files.

## Installation

The only prerequisite is to have an Ubuntu (or any other Debian-based distro), and Python3 and PIP installed on it.

To facilitate the installation of OpenCV, pyzbar, DBR and QReader for the user, a bash script (install_dependencies.sh) is included that performs this task autonomously. Its execution is as follows:

    ./install_dependencies.sh

In case you want to proceed with a manual installation, the steps to perform are as follows:

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

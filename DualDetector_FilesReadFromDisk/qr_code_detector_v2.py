import cv2
from interface import QRCodeDetector
import readingQR_cv2 as rd

class QRCodeDetectorV2(QRCodeDetector):
    def detect_and_decode(self, frame):
        coords_and_area = rd.detect_and_decode(frame)
        
        # Display the frame with detected QR codes
        # cv2.imshow("Detect QR Code from Webcam - OpenCV", frame)
        # cv2.waitKey(1)
        
        return coords_and_area
import cv2
from interface import QRCodeDetector
import readingQR_cv2 as rd

class QRCodeDetectorV2(QRCodeDetector):
    def detect_and_decode(self, frame):
        return rd.detect_and_decode(frame)

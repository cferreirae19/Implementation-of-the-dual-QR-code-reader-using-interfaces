import cv2
from interface import QRCodeDetector
import readingQR_cv2 as rd
import time

class QRCodeDetectorV2(QRCodeDetector):
    def __init__(self):
        self.last_detection_times = {}

    def detect_and_decode(self, frame):
        current_time = time.time()
        qr_codes, qr_data_list = rd.detect_and_decode(frame)
        
        for qr_code, qr_data in zip(qr_codes, qr_data_list):
            if qr_data not in self.last_detection_times or current_time - self.last_detection_times[qr_data] > 5:
                self.last_detection_times[qr_data] = current_time
                print("QR Code Data:", qr_data)
        
        return qr_data_list

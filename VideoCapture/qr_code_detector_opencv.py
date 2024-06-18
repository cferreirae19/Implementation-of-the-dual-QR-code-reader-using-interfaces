import cv2
from interface import QRCodeDetector
import time
import numpy as np
from pyzbar.pyzbar import decode

# Functions from the old readingQR_cv2.py module
def detect_qr_codes(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    qr_codes = decode(gray_frame)
    return qr_codes

def extract_qr_data(qr_codes):
    qr_data_list = []
    if qr_codes:
        for qr_code in qr_codes:
            qr_data = qr_code.data.decode('utf-8')
            qr_data_list.append(qr_data)
    return qr_data_list

def draw_qr_code_rectangles(frame, qr_codes):
    if qr_codes:
        for qr_code in qr_codes:
            points = qr_code.polygon
            rect = qr_code.rect
            
            # Width, height and area of the bounding box
            width = rect[2]
            height = rect[3]
            area = width * height
            
            # Label showing the bounding box size
            dimensions_label = 'Size: %d x %d = %d' % (width, height, area)
            cv2.putText(frame, dimensions_label, (rect[0], rect[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                cv2.polylines(frame, [hull], True, (255, 0, 255), 3)
            else:
                cv2.polylines(frame, [np.array(points, dtype=np.int32)], True, (255, 0, 255), 3)

def detect_and_decode(frame):
    qr_codes = detect_qr_codes(frame)
    qr_data_list = extract_qr_data(qr_codes)
    draw_qr_code_rectangles(frame, qr_codes)
    cv2.imshow("Detect QR Code from Webcam", frame)
    return qr_codes, qr_data_list

# Original class from qr_code_detector_v2.py
class QRCodeDetector_OpenCV(QRCodeDetector):
    def __init__(self):
        self.last_detection_times = {}

    def detect_and_decode(self, frame):
        current_time = time.time()
        qr_codes, qr_data_list = detect_and_decode(frame)
        
        for qr_code, qr_data in zip(qr_codes, qr_data_list):
            if qr_data not in self.last_detection_times or current_time - self.last_detection_times[qr_data] > 5:   # Not necessarily 5 seconds (just testing)
                self.last_detection_times[qr_data] = current_time
                print("QR Code Data:", qr_data)
        
        return qr_data_list

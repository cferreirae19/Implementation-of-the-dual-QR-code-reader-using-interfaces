import cv2
import numpy as np
from pyzbar.pyzbar import decode
from interface import QRCodeDetector

# Function to detect QR codes in a given frame
def detect_qr_codes(frame):
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Decode QR codes from the grayscale frame
    qr_codes = decode(gray_frame)
    return qr_codes

# Function to extract data from detected QR codes
def extract_qr_data(qr_codes):
    qr_data_list = []
    if qr_codes:
        for qr_code in qr_codes:
            # Decode QR code data to a string
            qr_data = qr_code.data.decode('utf-8')
            qr_data_list.append(qr_data)
    return qr_data_list

# Function to draw rectangles around detected QR codes and return their dimensions and areas
def draw_qr_code_rectangles(frame, qr_codes):
    results = []
    if qr_codes:
        for qr_code in qr_codes:
            points = qr_code.polygon
            rect = qr_code.rect
            
            width = rect[2]
            height = rect[3]
            area = width * height
            
            # Label showing the size of the QR code
            label = 'Size: %d x %d = %d' % (width, height, area)
            cv2.putText(frame, label, (rect[0], rect[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                cv2.polylines(frame, [hull], True, (255, 0, 255), 3)
            else:
                cv2.polylines(frame, [np.array(points, dtype=np.int32)], True, (255, 0, 255), 3)
            results.append((width, height, area))
    return results

# Function to detect and decode QR codes from a frame
def detect_and_decode(frame):
    qr_codes = detect_qr_codes(frame)
    qr_data_list = extract_qr_data(qr_codes)
    coords_and_areas = draw_qr_code_rectangles(frame, qr_codes)
    return list(zip(qr_data_list, coords_and_areas))

# Class for an advanced QR code detector inheriting from QRCodeDetector
class QRCodeDetector_OpenCV(QRCodeDetector):
    def detect_and_decode(self, frame):
        return detect_and_decode(frame)

import cv2
import numpy as np
from pyzbar.pyzbar import decode

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
    results = []
    if qr_codes:
        for qr_code in qr_codes:
            points = qr_code.polygon
            rct = qr_code.rect
            width = rct[2]
            height = rct[3]
            area = width * height
            label = 'Size: %d x %d = %d' % (width, height, area)
            cv2.putText(frame, label, (rct[0], rct[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                cv2.polylines(frame, [hull], True, (255, 0, 255), 3)
            else:
                cv2.polylines(frame, [np.array(points, dtype=np.int32)], True, (255, 0, 255), 3)
            results.append((width, height, area))
    return results
                
def detect_and_decode(frame):
    qr_codes = detect_qr_codes(frame)
    qr_data_list = extract_qr_data(qr_codes)
    coords_and_areas = draw_qr_code_rectangles(frame, qr_codes)
    return list(zip(qr_data_list, coords_and_areas))
